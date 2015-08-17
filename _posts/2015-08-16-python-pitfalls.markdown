---
layout: post
title:  "Python pitfalls"
date:   2015-08-16 12:00:00
categories: Python
image:
  feature: sample-image-7.jpg
---

## Object persistence and bad side-effects

The output of the snippet of code below is not obvious as most people tend to think that the `list` will be created each time the `extendList` function is called. However, the `list` is only created once when the function is first defined and then use for subsequent calls where the `list` argument is __not__ provided.    

{% highlight python %}
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')


print "list1 = %s" % list1 # list1 = [10, 'a']
print "list2 = %s" % list2 # list2 = [123]
print "list3 = %s" % list3 # list3 = [10, 'a']
{% endhighlight %}

The desired implementation would default the `list` argument with the value `None` in order to prevent the `list` variable from being initiated as a list. 

{% highlight python %}
def extendListUpdated(val, list=None):
    # if no list is provided initialize an empty list
    if list is None:
        list = []
    list.append(val)
    return list

list1 = extendListUpdated(10)
list2 = extendListUpdated(123,[])
list3 = extendListUpdated('a')

print "list1 = %s" % list1 # [10]
print "list2 = %s" % list2 # [123]
print "list3 = %s" % list3 # ['a']
{% endhighlight %}

Note that the `None` value is a way to signify __empty__ or __no value here__. It's commonly defined as  

> Assigning a value of None to a variable is one way to reset it to its original, empty state.


## Closures and late binding

The expected output of the print statement is `[0, 2, 4, 6]` based on the element-wise operation `[0*2, 1*2, 2*2, 3*2]` where each element in list represents `i*x`. However, `[3*2, 3*2, 3*2, 3*2] = [6, 6, 6, 6]` is what is actually calculated.  

{% highlight python %}
def multipliers():
    return [lambda x : i*x for i in range(4)]

print [m(2) for m in multipliers()] # [6, 6, 6, 6]
{% endhighlight %}

The function returns `[6, 6, 6, 6]` because the variable `i` is not passed to the the _lambda function_ until the loop `for i in range(4)` has been evaluated. That's why `i` is the last element of the list `[0, 1, 2, 3]` list.

