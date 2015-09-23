---
layout: post
title:  "Python closures and late binding"
date:   2015-08-16 12:00:00
categories: Python
image:
  feature: sample-image-7.jpg
---


An example of a closure is when a function depends on a variable outside it's scope. A more specific definition from [Stack Overflow Post](http://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures) states:

> A closure occurs when a function has access to a local variable from an enclosing scope that has finished its execution.

{% highlight python %}
def make_printer(msg):
    def printer():
        print msg
    return printer
{% endhighlight %}

We can see that the `printer()` function depends on the variable `msg` which is defined outside the scope of it's function. 

### Late binding and bad side-effects

However, things get a bit more complicated when we have late binding. It's indeed a gotchas and is stated in [Python Guide](http://docs.python-guide.org/en/latest/writing/gotchas/) as:

> Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called.
 
For example, if we are given the closure: 

{% highlight python %}
def multipliers():
    return [lambda x : i*x for i in range(4)]

print [m(2) for m in multipliers()] # [6, 6, 6, 6]
{% endhighlight %}

Then we expect the output of the print statement to be `[0, 2, 4, 6]` based on the element-wise operation `[0*2, 1*2, 2*2, 3*2]`. However, `[3*2, 3*2, 3*2, 3*2] = [6, 6, 6, 6]` is what is actually return. That is because `i` is not passed to the the _lambda function_ until the loop `for i in range(4)` has been evaluated. 

In order to avoid the late binding side-effect we default the `i` argument by:
 
{% highlight python %}
def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]

print [m(2) for m in multipliers()] # [0, 2, 4, 6]
{% endhighlight %}