---
layout: post
title:  "Data pipeline and stream processing"
date:   2015-08-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---
A data pipeline is method for shipping data efficiently to various services throughout your system. It also provides a framework that supports stream processing, enable things like:
 
* Real-time dashboards 
* Iterative recommender systems
* Data warehouses without complex ETL processes

## The producer consumer model

The idea is that you have a set of producer and consumer applications, where the producer will publish data to your pipeline and the consumer will subscribe from your pipeline. That means that you can integrate your pipeline with multiple systems by creating multiple consumer applications. 

{% stylesheet mermaid %}

{% mermaid %}
        graph LR
 
        A(Mobile) -.publish.-> E((Pipeline)) 
        B(Platform) -.publish.-> E((Pipeline))
        C(CRM) -.publish.-> E((Pipeline)) 
        D(Salesforce) -.publish.-> E((Pipeline))
        E -.subscribe.-> G(Data Warehouse)
        E -.subscribe.-> I(Real-time Dashboards)
        E -.subscribe.-> J(Recommender Systems)
        E -.subscribe.-> K(Third-party Integration)
{% endmermaid %}


It also support a _time to live_ (TTL) parameter which allows you to persist data in the pipeline for days to years. As a result you can replay messages as needed. This is particularly useful if your consumer application logic changes. 

The pipeline is essentially a high-throughput distributed messaging system such as [Apache Kafka](http://kafka.apache.org/) or  [Amazon Kinesis](https://aws.amazon.com/kinesis/). They are built to support a huge number of incoming and outgoing messages.
