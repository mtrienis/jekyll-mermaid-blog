---
layout: post
title:  "Integrating spark streaming and aws redshift"
date:   2015-05-31 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

# Spark streaming ETL with AWS

{% stylesheet mermaid %}

The most efficient way to load data into AWS Redshift is first upload your data to S3 and then execute the copy command on Redshift. From the [documentation](http://docs.aws.amazon.com/redshift/latest/dg/t_Loading_data.html)

>A COPY command is the most efficient way to load a table. When you load data from Amazon S3, the COPY command is able to read from multiple data files simultaneously. Whether you load from data files on Amazon S3 or from an Amazon DynamoDB table, Amazon Redshift distributes the workload to the cluster nodes and performs the load process in parallel.

Therefore for each batch of data in your Spark Streaming application,  

1. Write the batch to an S3 folder that is identified by the batch interval   
2. Copy the batch to Redshift by executing a `copy` command

{% mermaid %}
        graph LR
        
        %% Example diagram
        A[AWS Kinesis] --> B[Spark Streaming Application]
        B --> C[AWS S3]
        B --> D[AWS Redshift]
        C -.-> D
{% endmermaid %}

Pushing data from Spark Streaming to S3 is fairly straight forward as Spark exposes the `saveAsTextFile` output operation that supports `s3n` hadoop connection point. The S3 endpoint may have a structure resemblying

{% highlight bash %}
s3n://[accessKey]:[secretKey]@[bucket]/[batchFolder]/[batchInterval]
{% endhighlight %}

The output operation can be applied to both RDDs and DStreams. However, in order to uniquely identify the batch interval we will need to expose the spark streaming _time_ parameter. Simply override the DStream `foreachRDD` function by

{% highlight scala %}
def dispatch(RDD[T], Time): Unit {
    // 1. Write the batch to an _S3_ folder that is identified by the batch interval 
    // 2. Copy the batch to Redshift by executing a `copy` command
}

// perform etl process
dstream.foreachRDD(dispatch _)

{% endhighlight %}






