---
layout: post
title:  "Spark streaming and aws kinesis pitfalls"
date:   2015-05-31 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

What you need to know when setting up [Spark Streaming](http://spark.apache.org/streaming/) with [AWS Kinesis](https://aws.amazon.com/kinesis/). 

## Each receiver occupies an entire core

A receiver is associated with a _dstream_ which receives data from streaming sources. It typically sits on the worker and pulls in data from one or more Kinesis shards. 

> Input DStreams are DStreams representing the stream of input data received from streaming sources. In the quick example, lines was an input DStream as it represented the stream of data received from the netcat server. Every input DStream (except file stream, discussed later in this section) is associated with a Receiver (Scala doc, Java doc) object which receives the data from a source and stores it in Spark’s memory for processing.

Receivers are generated when you create a stream to Kinesis:

{% highlight scala %}
KinesisUtils.createStream(ssc, appName, streamName, endpointUrl, regionName,
        InitialPositionInStream.LATEST, kinesisCheckpointInterval, StorageLevel.MEMORY_AND_DISK_2)
{% endhighlight %}

For each shard in your Kinesis stream, you should typically create one receiver. Additional streams (or receivers) will allow you to scale out the amount of incoming data that will be processed. 

{% highlight scala %}
val numStreams = numShards

// Create the Kinesis DStreams
val kinesisStreams = (0 until numStreams).map { i =>
	KinesisUtils.createStream(ssc, appName, streamName, endpointUrl, regionName,
        InitialPositionInStream.LATEST, kinesisCheckpointInterval, StorageLevel.MEMORY_AND_DISK_2)
}
{% endhighlight %}

However, it's important to note that each receiver created will use an entire core in your cluster. If you are using the snippet above, then you will automatically create additional receivers by simply adding shards to your Kinesis stream. If you create too many receivers then you will not have any cores available for processing. 

## Never cross your Kinesis stream names mid flow 

During development you may need to change the stream name as you debug your application. If you noticed that you are unable to process any additional records from Kinesis then you need purge the Kinesis related DynamoDB table located in the _us-east-1_ region. In some cases you may also need to delete and recreate Kinesis streams. 

## Job duration should never exceed batch time

The time it takes to run your jobs should always be less than the batch interval. If you find your spark jobs taking longer than the batch interval then your streaming application will take longer and longer to finish processing. That's why it's important to setup monitoring to measure _throughput_.

### AWS cloud watch

Cloud watch provides dashboards for monitoring the put and get requests for AWS Kinesis. It's important to understand these metrics as it will allow you to determine whether you need to increase the number of shards in Kinesis or workers in apache spark. If the _get rate_ (bytes / records) is less than the maximum available then the bottleneck is your spark streaming application. 

### Spark Web UI

Spark web UI provides a scheduler delay metric that is determined by the time required to assign a task to an available resource. If your scheduling delay is increasing, it's a good indication that your system can not handle the amount of incoming data. 
	

