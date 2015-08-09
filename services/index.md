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
We offer services focused on the Apache Spark engine. There are several options regarding the cluster manager, data store, build tools, automation and instance types. 

| Cluster Manager     | Data Store | Build Tool  | Automation | Virtual Environment |
|---------------------|-----------|-------------|------------| ----------------------|
| Spark Standalone    | Cassandra | Sbt         | Ansible    | Virtualbox |
| Apache Mesos        | HDFS   | Ant         | Salt       | Docker |
| Hadoop Yarn         | AWS S3 | Maven       | Puppet     | EC2 |

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

The deployment of Spark must run on either __Standalone__, __Apache Mesos__ or __Hadoop Yarn__. These will define the rules that dictate how your cluster resources will be utilized.

### Data stores

As part of the deployment you should choose a data store that best fits your storage requirements. __Cassandra__ is a great data store for time series data as well as real-time dashboards. __HDFS__ is excellent option for flexible storage and reporting. __AWS S3__ is another option that will integrate into your cloud infrastructure.

### Build tools

Building your application should be simple and provide enough flexibility to integrate into your delivery process. We will build out your initial Spark application using either __sbt__, __ant__, or __Maven__.

### Automation

It is important that each step in the process of building out the infrastructure is automated in order to create repeatable and consistent environments. We provide automation services using __Ansible__, __Salt__ as well as __Puppet__.  

### Virtual environment

Scale out your nodes based on demand by deploying Apache Spark in the cloud. We support __EC2__ deployments, or __Docker__ containers for shipping. We also provide virtual machine support using __Virtualbox__ for development purposes. 





