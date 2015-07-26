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
