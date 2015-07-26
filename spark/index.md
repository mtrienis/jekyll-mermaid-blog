---
layout: page
title: Product Services
tags: [about, Jekyll, theme, responsive]
modified: 2014-08-08T20:53:07.573882-04:00
comments: true
image:
  feature: sample-image-7.jpg
---

{% stylesheet mermaid %}

Data is the new currency and it's going to be an important factor for any business looking to thrive in an increasingly competitive landscape. 

There are quite a few homegrown data solutions that end up creating a large cost to the business due to natural complexites of analytics problems. That is why you should take a serious look at a unified data framework. 

## Why you need a unified data framework

Most businesses that have built a technology platform will eventually include analytics component to their solution. These solutions typically involve the implementation of one or more of the following: 
 
* Real-time dashboards
* Personalization for your users or customers
* Data warehousing and business intelligence
* Complex data integration.

<!-- <img style="float: center; PADDING-LEFT: 150px; height: 75px" src="/assets/images/spark-logo-hd.png"> -->

However, these software problems are non-trivial to solve and usually involve a significant amount of effort and cost to develop. A relatively new technology, known as [Apache Spark](http://spark.apache.org/), can help ease the pain of building out these systems. The framework exposes a set of high-level libraries that enable you to _quickly_ build out analytics features. 

<img style="float: center; PADDING-LEFT: 25px; PADDING-TOP: 25px; PADDING-BOTTOM: 25px; height: 175px" src="/assets/images/spark-stack.png">

All of these libraries are built on top of a very fast compute engine that allow you to quickly scale out the system by simply adding worker nodes into the pool. That means that your engineering team spends less time setting up and maintaining infrastructure and more time building applications that deliver value for your business.

The complexities of distributed fault-tolerant processing are abstracted out by providing [simple APIs](http://spark.apache.org/docs/latest/programming-guide.html) to the application developer. The primary abstraction is known as [Resilient Distributed Datasets (RDDs)](https://spark.apache.org/docs/latest/programming-guide.html#resilient-distributed-datasets-rdds), however, more recently Spark introduced [DataFrames](http://spark.apache.org/docs/latest/sql-programming-guide.html#dataframes) as a way for developers to work tabular data.  



<!--
* Stream processing for in-flight computation
* Fault-tolerance for reliable
* Rich abstraction that enable easy computation through SQL 
* Operational metrics
* Mobile and web usage 
* Sales and pipeline 
-->

# Continuous integration and delivery

* Application deployment 
* Continuous integration
* Configuration management 

# Repeatable and consistent environments

<!-- # Repeatable and consistent environments: from development to production --> 

{% mermaid %}
        graph LR
        subgraph one
        A[Virtual Machine] --> B[EC2 Development]
        end
        subgraph one
        B --> C[EC2 Testing]
        C --> D[EC2 Staging]
        D --> E[EC2 Production]
        end
{% endmermaid %}

* Talk about AWS here

# Distributed databases

* Talk about Cassandra and MongoDb

<!-- * Automation and continuous delivery 
* Data infrastructure to support ETL and aggregation processes 
* Mobile event tracking for operational and product insights

## Specialized technologies

* Apache Spark
* Ansible
* Amazon Web Services (Kinesis, Redshift, S3, EC2, Route53, VPC)
* Scala  
* Cassandra
* MongoDB -->
