---
layout: post
title:  "Integrating spark streaming and aws redshift"
date:   2015-05-31 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---
{% stylesheet mermaid %}
The most efficient way to load data into [AWS Redshift](https://aws.amazon.com/redshift/) is first upload your data to [S3](https://aws.amazon.com/s3/) and then execute the copy command on Redshift. From the [documentation](http://docs.aws.amazon.com/redshift/latest/dg/t_Loading_data.html)

>A COPY command is the most efficient way to load a table. When you load data from Amazon S3, the COPY command is able to read from multiple data files simultaneously. Whether you load from data files on Amazon S3 or from an Amazon DynamoDB table, Amazon Redshift distributes the workload to the cluster nodes and performs the load process in parallel.

Therefore for each batch of data in your Spark Streaming application,  

1. Write batch to _S3_ folder identified by the batch interval   
2. Copy the batch to Redshift by executing a `copy` command

{% mermaid %}
        graph LR
        A[AWS Kinesis] --> B[Spark Streaming Application]
        B --> C[AWS S3]
        B --> D[AWS Redshift]
        C -.-> D
{% endmermaid %}

Pushing data from Spark Streaming to [S3](https://aws.amazon.com/s3/) is fairly straight forward as Spark exposes the `saveAsTextFile` output operation that supports [s3n](https://aws.amazon.com/s3/) hadoop connection point. The endpoint will likely have a structure that resembles:

{% highlight bash %}
s3n://[accessKey]:[secretKey]@[bucket]/[batchFolder]/[batchInterval]
{% endhighlight %}

The output operation can be applied to both [RDDs](http://spark.apache.org/docs/latest/programming-guide.html#resilient-distributed-datasets-rdds) and [DStreams](http://spark.apache.org/docs/latest/streaming-programming-guide.html#discretized-streams-dstreams). However, in order to uniquely identify the batch interval we will need to expose the spark streaming _time_ parameter. Simply override the `foreachRDD` function:

{% highlight scala %}
def dispatch(RDD[T], Time): Unit {
    // 1. Write the batch to an _S3_ folder that is identified by the batch interval 
    // 2. Copy the batch to Redshift by executing a `copy` command
}

// perform etl process
dstream.foreachRDD(dispatch _)

{% endhighlight %}






