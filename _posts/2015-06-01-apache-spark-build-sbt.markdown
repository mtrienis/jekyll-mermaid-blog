---
layout: post
title:  "Building Apache Spark using sbt"
date:   2015-05-31 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

## How to avoid dependency hell

Assembling your fat jar through [sbt-assembly](https://github.com/sbt/sbt-assembly) will result in a huge number of library conflicts. In order to circumvent this issue, you can simply include all spark libraries as `provided`. 

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