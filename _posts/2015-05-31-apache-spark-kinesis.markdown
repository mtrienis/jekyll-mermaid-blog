---
layout: post
title:  "Spark Streaming and AWS Kinesis Pitfalls"
date:   2015-05-31 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

## Common pitfalls

### Each receiver occupies an entire core

I realize this sounds like an obvious statement. However it can be subtle problem if you end up creating too many receivers for a spark streaming application. For example, the code snippet, 

{% highlight scala %}
val numStreams = numShards

// Create the Kinesis DStreams
val kinesisStreams = (0 until numStreams).map { i =>
	KinesisUtils.createStream(ssc, appName, streamName, endpointUrl, regionName,
        InitialPositionInStream.LATEST, kinesisCheckpointInterval, StorageLevel.MEMORY_AND_DISK_2)
}
{% endhighlight %}

creates as many streams as you have shards. Each stream creates a receiver, and will occupy an entire core for the duration of your streaming application. This means that if you scale out the number of shards, you will also need to scale out the number of cores available for your executors. Otheriwse, you may find yourself running out of cores. 

### Never cross your Kinesis stream names mid flow 

During development you may need to change the stream name as you debug your application. Soon after you may noticed that you are unable to process any additional records from Kinesis. The solution here is to purge the Kinesis related DynamoDB table located in the us-east-1 region. In some cases you may also need to delete and recreate Kinesis streams. 

### Total job duration should never exceed batch interval time 

There are a couple ways to monitor throughput:

* Cloud watch provides dashboards for monitoring the put and get requests. It's important to understand these metrics as it will allow you to determine whether you need to increase the number of shards in Kinesis or workers in apache spark. If the get rate (bytes / records) is less than the maximum available then the bottleneck is the consumer application (i.e. spark streaming). 
* Spark web UI provides a scheduler delay metric that is determined by the time required to assign a task to an available resource. If your scheduling delay is increasing, it's a good indication that your system can not handle the amount of incoming data. 
	
### How to avoid dependency hell when using assembly-sbt

Assembling your fat jar through `sbt-assembly` will result in a huge number of library conflicts. In order to circumvent this issue, you can simply include all spark libraries as `provided`. 

{% highlight scala %}
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.3.0" % "provided",
  "org.apache.spark" %% "spark-streaming" % "1.3.0" % "provided",
  "org.apache.spark" %% "spark-streaming-kinesis-asl_2.10" % "provided"
)
{% endhighlight %}

Provided is defined as:

> This is much like `compile`, but indicates you expect the JDK or a container to provide the dependency at runtime. For example, when building a web application for the Java Enterprise Edition, you would set the dependency on the Servlet API and related Java EE APIs to scope `provided` because the web container provides those classes. This scope is only available on the compilation and test classpath, and is not transitive.

Submitting a spark application through `spark-submit` will automatically include those libraries at run-time. Additional libraries can be provided at run time by specifying `--jars` arguments.

{% highlight bash %}
./bin/spark-submit \
  --verbose 
  --jars <external-jars>
  --class <main-class>
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  ... # other options
  <application-jar> \
  [application-arguments]
{% endhighlight %}
