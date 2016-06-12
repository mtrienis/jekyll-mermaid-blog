---
layout: post
title:  "Pragmatic Guide: Apache Kafka or AWS Kinesis"
date:   2016-05-29 12:00:00
categories: Python
image:
  feature: sample-image-7.jpg
---
{% stylesheet mermaid %}

Building a unified data pipeline means that you will likely need to choose between two of the mainstream messaging systems:

* [AWS Kinesis](http://docs.aws.amazon.com/streams/latest/dev/introduction.html).
* [Apache Kafka](http://kafka.apache.org/documentation.html).

Kinesis and Kafka are distributed publish and subscription messaging systems that are highly scalable and fault-tolerant. A few critical differences between these technologies will be examined more closely: 

* Latency.
* Programming interfaces.
* Reliability.
* Flow control.	
* Security and authorization.

## High latency and dealbreakers

Apache Kafka is open source provides some flexibility in terms of deployment. It allows you to deploy the service local (or close) to your applications yielding extremely low latency for clients producing data. This is often a critical requirement as it minimizes the complexity and overhead of your application. 

Client requests to Kinesis often suffer from double digit latency as each request is sent over a HTTP web server and then synchronously replicated to multiple facilities. This forces the clients to mitigate the latency by:
 
* Forking background threads to avoid interrupting the client.
* Introduce batching to reduce the number of requests.
* Implementing a relay service that is deployed locally.

## Everyone needs a proxy

One reason Kinesis has higher latency is because all communication is done through a high level HTTP proxy. However, a proxy is desirable as it provides a mechanism for: 

* Flow control in terms of requests or bytes per second.
* Authorization for data producers and consumers.
* Easy access for any client who can support HTTP requests.

Kinesis bandwidth and rate limiting is determined by the number of shards in your Kinesis stream. As you increase your shards, you also increase the cost of your stream: 

{% mermaid %}
        graph LR
        A[Client A] -.HTTP.-> E[Shard 1]  
        A[Client A] -.HTTP.-> F[Shard 2] 
        B[Client B] -.HTTP.-> E[Shard 1]
        C[Client C] -.HTTP.-> I[Shard 1]
        subgraph Kinesis Stream A
        E[Shard 1]
        F[Shard 2]
        end   
        subgraph Kinesis Stream B
        I[Shard 1]
        end
{% endmermaid %}

Kafka supports a low level TCP client for high volume and low latency requests. There is a REST library that wraps the low level client, however, it's managed and deployed separately:  

{% mermaid %}
        graph LR
        B[Client B] -.TCP.-> C[Apache Kafka]
        A[Client A] -.HTTP + Auth.-> D[HTTP Proxy]  
        D[HTTP Proxy] -. flow control .-> C[Apache Kafka]
        subgraph Kafka Pipeline
        C[Apache Kafka]
        D[HTTP Proxy]
        end        
{% endmermaid %}

Kafka also has tooling to support authorization and security, see [Apache Kafka Security 101](http://www.confluent.io/blog/apache-kafka-security-authorization-authentication-encryption). As you can see, it's non-trivial to setup and will likely require an additional service for managing certificates.

## Looking forward and facing costs

It's important to factor these components into your cost comparison as it will take serious engineering effort to build and maintain these pieces at large scale. With Kinesis you get everything out-of-the-box:

* High durability and availability for producers and consumers.
* Ability to seamlessly scale out the service by [Resharding](http://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html).
* Built-in monitoring through [Cloud Watch](https://aws.amazon.com/cloudwatch/).

Managing Kafka clusters across multiple DCs with seamless failover is complex and will take a great deal of time and cost. That being said, Kafka is progressing quickly and has a rich set of features and tools that include:

* Fine grain topic config: e.g. retention and replication.
* Purpose built processing framework called [Kafka Streams](http://www.confluent.io/blog/introducing-kafka-streams-stream-processing-made-simple).
* Pre-built sink integrations using [Kafka Connect](http://docs.confluent.io/2.0.0/connect/intro.html).

Kafka is definitely more flexible in terms of bells and whistles. It also introduces a very promising streaming technology. However, if you're looking to quickly bootstrap your pipeline with small operational overhead then Kinesis is probably a better choice.



