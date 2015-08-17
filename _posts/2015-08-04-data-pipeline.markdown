---
layout: post
title:  "Data pipeline and stream processing"
date:   2015-08-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---
A data pipeline is method for shipping data efficiently to various services throughout your system. It provides a framework for enabling stream processing. That means it's now possible to build things like real-time dashboards and recommender systems, at scale, without massive complexity.   

## The producer consumer model

The idea is that you have a set of producer applications that publish data to your pipeline. That published data is available for consumption for a configurable period of time, usually 24 hours. The pipeline provides high availability, allowing multiple consumer applications to consume the same stream of data. 

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


The pipeline is essentially a high-throughput distributed messaging system such as [Apache Kafka](http://kafka.apache.org/) or  [Amazon Kinesis](https://aws.amazon.com/kinesis/). They are built to support a huge number of incoming and outgoing messages. That means that you can transport the streams of data to whichever system without having to implement a complex offline ETL process.
