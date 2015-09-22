---
layout: post
title:  "Java singleton pattern"
date:   2015-06-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

The singleton pattern ensures that only one instance of an object can be instantiated. The code snippet below is an example of a singleton pattern.

{% highlight java %}
public class Singleton {

	private static Singleton singleton = new Singleton();
	
	/* A private Constructor prevents any other 
	* class from instantiating.
	*/
	private Singleton() { }
	
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

First we notice that the `Singleton` class is instanitated and stored in a static variable. As static variables share the same copy of the variable across all objects of the same type, so we ensure that the same object is persisted across all objects.  

{% highlight java %}
private static Singleton singleton = new Singleton();
{% endhighlight %}

Since the constructor is private, the only way to instantiate te `Singleton` object is to call the static `getInstance` method.
 
{% highlight java %}
Singleton tmp = Singleton.getInstance( ); 
{% endhighlight %}




