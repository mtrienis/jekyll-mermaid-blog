---
layout: post
title:  "Data pipeline and streaming processing"
date:   2015-08-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---
A data pipeline is method for shipping data efficiently to various services throughout your organization. 

On one hand you will have your set of producers that will generate the data for your pipeline. They are essentially your sources of data. 

{% stylesheet mermaid %}

{% mermaid %}
        graph LR
        subgraph Data Producers
        A[Mobile] ==> E[Data Pipeline] 
        B[Platform] ==> E[Data Pipeline] 
        C[Sales] ==> E[Data Pipeline] 
        D[Markeing] ==> E[Data Pipeline] 
        end
        E[Data Pipeline]  ==Data Stream==> L[Stream Processing]
        subgraph Data Consumers
        L[Stream Processing] ==> G[Data Warehouse]
        L[Stream Processing]  ==> I[Real-time Dashboards]
        L[Stream Processing]  ==> J[Recommender Systems]
        L[Stream Processing]  ==> K[Third-party Integration]
        end
{% endmermaid %}

After the data has been published to the pipeline you can create consumer applications that will subscribe to various data feeds. This kind of architecture enables agile integration with different subsystems.

The event bus could be AWS Kinesis or Kafka while the processing engine could be Apache Spark.

Th

What are the appropriate use cases for a data pipeline?
* Activity stream data 


