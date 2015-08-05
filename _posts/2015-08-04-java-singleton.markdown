---
layout: post
title:  "Java singleton pattern"
date:   2015-06-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

The singleton pattern ensures that only one instance of an object can be instantiated.

{% highlight java %}
public class Singleton {

	private static Singleton singleton = new Singleton( );
	
	/* A private Constructor prevents any other 
	* class from instantiating.
	*/
	private Singleton(){ }
	
	/* Static 'instance' method */
	public static Singleton getInstance( ) {
		return singleton;
	}

	/* Other methods protected by singleton-ness */
	protected static void demoMethod( ) {
		System.out.println("demoMethod for singleton"); 
	}
}
{% endhighlight %}