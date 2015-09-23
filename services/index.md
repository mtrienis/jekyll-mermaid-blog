---
layout: page
title: Apache Spark Cluster
tags: [about, Jekyll, theme, responsive]
modified: 2014-08-08T20:53:07.573882-04:00
comments: true
image:
  feature: sample-image-7.jpg
---
{% stylesheet mermaid %}

We offer services focused on the Apache Spark engine. There are several options regarding the cluster manager, data store, build tools, automation and deployments.

### Spark workflow

All of these tools enable you to quickly develop, configure and deploy applications to a Spark cluster. That way you can spend more time gleaning insights and less time debugging.

{% mermaid %}
graph LR
  C{Application} -.Build.-> C{Application}
    C -.Deploy.-> G(Spark Master)
    subgraph Virtual Environment
    G -.-> D(Spark Worker)
    D -.-> H(Data Store)
    G -.-> E(Spark Worker)
    E -.-> I(Data Store)
    G -.-> F(Spark Worker)
    F -.-> J(Data Store)
  end
{% endmermaid %}

### Cluster managers

The deployment of Spark must run on either [Standalone](http://spark.apache.org/docs/latest/cluster-overview.html), [Apache Mesos](http://mesos.apache.org/) or [Hadoop Yarn](http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html). These will define the rules that dictate how your cluster resources will be utilized and monitored.

### Data stores

As part of the deployment you should choose a data store that best fits your storage requirements. [Cassandra](http://cassandra.apache.org/) is a great data store for time series data as well as real-time dashboards. [HDFS](http://hadoop.apache.org/docs/r1.2.1/hdfs_design.html) is excellent option for flexible storage and reporting. [AWS S3](https://aws.amazon.com/s3/) is another option that will integrate into your cloud infrastructure.

### Build tools

Building your application should be simple and provide enough flexibility to integrate into your delivery process. We will build out your initial Spark application using either [Sbt](http://www.scala-sbt.org/), [Ant](http://ant.apache.org/) , or [Maven](https://maven.apache.org/).

### Virtual environment

Scale out your nodes based on demand by deploying Apache Spark in the cloud. We support [EC2](https://aws.amazon.com/ec2/) deployments, or [Docker](https://www.docker.com/) containers for shipping. We also provide virtual machine support using [Virtualbox](https://www.virtualbox.org/) for development purposes.

### Automation

It is important that each step in the process of building out the infrastructure is automated in order to create repeatable and consistent environments. We provide automation services using [Ansible](http://www.ansible.com/), [Salt](http://saltstack.com/) as well as [Puppet](https://puppetlabs.com/).






