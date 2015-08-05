---
layout: post
title:  "Launching apache spark using supervisord"
date:   2015-06-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

Apache Spark comes bundled with several [launch scripts](https://spark.apache.org/docs/latest/spark-standalone.html) to start the master and worker processes. We can launch a master and two workers processes by executing

{% highlight bash %}
./sbin/start-master.sh
./sbin/start-slaves.sh 1 spark://master.mydomain.com:7077
./sbin/start-slaves.sh 2 spark://master.mydomain.com:7077
{% endhighlight %}

The issue with launching the cluster this way is that each time the cluster reboots you will need to re-execute the shell scripts above. This process is cumbersome and prone to error.

# Controlling master and worker process with Supervisord

A better approach requires the use of [supervisord](http://supervisord.org/introduction.html) (a process control system) to manage spark processes. It has the following benefits:

* A homogeneous method for _starting_/_stopping_/_restarting_ processes
* Provides a centralized monitoring mechanism for sensitive services   
* Accurate up/down statuses, even when a process crashes

The only requirements is that processes must be run in the _foreground_. Therefore master and worker(s) processes should be initiated through `spark-class` instead of the sbin shell scripts as they run the processes as a daemon. You should end up with supervisord configurations resembling:

* /supervisor/conf.d/spark_master.conf
{% highlight bash %}
[program:spark_master]
command=/bin/spark-class org.apache.spark.deploy.master.Master --ip master.mydomain.com --port 7077 --webui-port 18080
stderr_logfile = /var/log/spark_master-stderr.log
stdout_logfile = /var/log/spark_master-stdout.log
priority=1
autostart=true
{% endhighlight %}

* /supervisor/conf.d/spark_worker.conf
{% highlight bash %}
[program:spark_worker]
command=/bin/spark-class org.apache.spark.deploy.worker.Worker spark://master.mydomain.com:7077
stderr_logfile = /var/log/spark_worker-stderr.log
stdout_logfile = /var/log/spark_worker-stdout.log
priority=2
autostart=true
{% endhighlight %}

It's convenient to drop your configuration files into `/supvisor/conf.d/` as they will be picked up automatically when you start the Supervisord service. It allows you to easily distribute your configuration files across your cluster.  

The priority flag means that the master will start prior to the worker. You can also set the number of retries (default is 3) for the worker in case the master has not completed its startup sequence.
