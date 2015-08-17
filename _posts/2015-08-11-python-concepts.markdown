---
layout: post
title:  "Python concepts for interviews"
date:   2015-06-05 12:00:00
categories: Python
image:
  feature: sample-image-7.jpg
---

Important Python concepts for interviews.

## Generators

We can break down the snippet of code further by inspecting the output of various components of the snippet. The `range` operator is a [generator](https://wiki.python.org/moin/Generators) function, and is used to generate lists. In this example, it generates a list of integers from 0 to 3.
{% highlight python %}
>>> print range(4) # [0, 1, 2, 3]
[0, 1, 2, 3]
{% endhighlight %}

## Anonymous (lambda) functions 

The next snippet of code defines a [lambda function](http://www.secnetix.de/olli/Python/lambda_functions.hawk) which is essentially a function that is not bounded to a name (i.e. an anonymous function). 
{% highlight python %}
>>> print lambda x : i * x
<function <lambda> at 0x109ae6938>

{% endhighlight %}

## List comprehensions

Putting it all together, we end up with a [list comprehension](http://www.secnetix.de/olli/Python/list_comprehensions.hawk) that generates a list of lambda functions. This is what is returned from the original `multipliers` function. 

{% highlight python %}
>>> print [lambda x : i * x for i in range(4)]
[<function <lambda> at 0x109ae6938>, <function <lambda> at 0x109ae6758>, <function <lambda> at 0x109ae69b0>, <function <lambda> at 0x109ae6a28>]
{% endhighlight %}

As a solution to this problem we can define a generator 

> A generator is a function that produces a sequence of results instead of a single value.

{% highlight python %}
>>> def multipliers():
...      for i in range(4): yield lambda x : i * x 

{% endhighlight %}

## Iterating over iterators 

 __lists__, __dictionaries__, __generators__ and __strings__ are all example of iterators. Each one of these constructs support the `for` statement for looping over.
  
{% highlight python %}

# looping through a list
>>> for i in [1,2,3]:
...   print i
... 
1
2
3

# looping through a dictionary
>>> for i in {"key":"value"}:
...   print i
... 
key

# loop through a generator 
>>> for i in range(3):
...   print i
... 
0
1
2
{% endhighlight %}

# looping through a string
>>> for i in "hello":
...     print i
... 
h
e
l
l
o
{% endhighlight %}


## Dynamic arguments

It's possible to pass a dynamic number of arguments. Either a sequence of values or a sequence of key-values. 

{% highlight python %}
>>> def dynamicArguments(*arg, **kwargs):
...     print arg
...     print kwargs
... 
>>> dynamicArguments(1,2,3, first=4, second=5, third=6)
(1, 2, 3)
{'second': 5, 'third': 6, 'first': 4}
{% endhighlight %}

## Linked-list implementation in python

A node in a linked list can represented as a class with a storage variable and another variable that points to the next node in the list. If the next pointer is `None` then it's the last element of the list.

{% highlight python %}
class Node:
  def __init__(self, item=None, next=None):
    self.item = cargo
    self.next  = next
  def __str__(self):
    return str(self.item)

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

nodeA.next = nodeB
nodeB.next = nodeC
{% endhighlight %}

## Private members in class

A member variable in a class can be set to private by prefixing with `__`. 

{% highlight python %}
>>> class Foo:
...     myPublicVar = "a" 
...     __myPrivateVar = "b" 
... 
>>> foo = Foo()
>>> print foo.myPublicVar
a
>>> print foo.__myPrivateVar
{% endhighlight %}


## Class variable and instance variables

Class variables:

{% highlight python %}
MyController(Controller):

  path = "something/"
  children = [AController, BController]

  def action(request):
    pass

{% endhighlight %}

Instance variables:

{% highlight python %}
MyController(Controller):

  def __init__(self):
    self.path = "something/"
    self.children = [AController, BController]

  def action(self, request):
    pass
{% endhighlight %}

## Command-line arguments (sys.argv)

Passing command line arguments to a python script is as simple as importing `sys` module and using the `sys.argv` for retrieving the arguments.

{% highlight python %}
import sys
print sys.argv
{% endhighlight %}

The arguments are constructed as a list when executing the python script.

{% highlight python %}
Mikes-MacBook-Pro-3:code miketrienis$ python example1_4.py a b
['example1_4.py', 'a', 'b']
{% endhighlight %}

## Pass statement

>The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

{% highlight python %}
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
{% endhighlight %}



