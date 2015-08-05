---
layout: page
title: Professional for Hire
tags: [about, Jekyll, theme, responsive]
modified: 2014-08-08T20:53:07.573882-04:00
comments: true
image:
  feature: sample-image-7.jpg
---
 
I love building data products that scale. That means implementing simple solutions with minimal maintenance through automation and eloquent designs.

## Technical expertise

My software experience spans the full stack; from system level deployment to application implementation. In particular, I spent quite a bit of time working with the technologies

* [Apache Spark](http://spark.apache.org/) ([Spark Streaming](http://spark.apache.org/streaming/), [Spark SQL](http://spark.apache.org/sql/))
* [Ansible](http://www.ansible.com/home)
* [Amazon Web Services](http://aws.amazon.com/) ([Kinesis](http://aws.amazon.com/kinesis/), [Redshift](http://aws.amazon.com/redshift/), [S3](http://aws.amazon.com/s3/), [EC2](http://aws.amazon.com/ec2/), [Route53](http://aws.amazon.com/route53/), [VPC](http://aws.amazon.com/vpc/))  
* [Cassandra](http://cassandra.apache.org/)
* [MongoDB](https://www.mongodb.org/)
* [Python](https://www.python.org/) ([Flask](http://flask.pocoo.org/), [Gunicorn](http://gunicorn.org/))
* [Scala](http://www.scala-lang.org/) ([Play](https://www.playframework.com/), [sbt](http://www.scala-sbt.org/))

## Professional projects

A few projects that I designed, implemented and delivered to a production environment. 

### Data pipeline and analytics framework

Implemented a high-throughput data pipeline that enabled massive amounts of data to be published to _AWS Kinesis_ and consumed with _Apache Spark_. The infrastructure enabled in-flight computation as well as data integration with a variety of datastores.  

* Data pushed to _S3_, _AWS Redshift_ and _MongoDB_ within 1 minute. 
* Supports real-time machine learning and aggregation.

### Real-time dashboards

Built a highly scalable analytics reporting system as part of the core product of our software as a service (SaaS) platform. The system was designed using a services oriented architecture (SOA) model to minimize coupling. It also supported horizontal scaling by distributing writes and reads across nodes. Over a million data points can be processed within minutes and rendered within seconds to the end user. 

* Dashboard metrics are updated within a minute.
* Supports up to ~500 million events per day.

### Cloud infrastructure and automation 

Automated the deployment and buildup of an AWS cloud infrastructure that auto-scales with traffic demand. The infrastructure was automated using Ansible and enabled the deployment of multi-instance clusters with varying configuration and topology. 

* Multi-instance cluster collapsed into a single-instance.
* Tear-down or build-up an environment within 5 minutes. 
* Decouple subsystems with independent deployment trains.

### Decoupled platform architecture

Architected as well as implemented a new configuration management system for the core QP platform at [QuickMobile](http://quickmobile.com). The design decoupled the system services from the application to enable greater flexibility and reduced down-down during deployments. The configuration mechanism was implemented using Ansible in idempotent style.
