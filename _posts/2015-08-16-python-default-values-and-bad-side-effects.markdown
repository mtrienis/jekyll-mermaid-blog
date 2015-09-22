---
layout: post
title:  "Python default values and bad side-effects"
date:   2015-08-16 12:00:00
categories: Python
image:
  feature: sample-image-7.jpg
---

 
The `extendList` function defaults `myList` to an empty list. However, `myList` is only created when the function is first _defined_. Therefore subsequent calls to `extendList` will mutate and return the original list.
 
{% highlight python %}
def extendList(val, myList=[]):
    myList.append(val)
    return myList

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')


print "list1 = %s" % list1 # list1 = [10, 'a']
print "list2 = %s" % list2 # list2 = [123]
print "list3 = %s" % list3 # list3 = [10, 'a']
{% endhighlight %}

The desired implementation would default the `myList` argument with the value `None` in order to prevent the `myList` variable from being initiated as a list. 

{% highlight python %}
def extendListUpdated(val, myList=None):
    # if no list is provided initialize an empty list
    if myList is None:
        myList = []
    myList.append(val)
    return myList

list1 = extendListUpdated(10)
list2 = extendListUpdated(123,[])
list3 = extendListUpdated('a')

print "list1 = %s" % list1 # [10]
print "list2 = %s" % list2 # [123]
print "list3 = %s" % list3 # ['a']
{% endhighlight %}

Note that the `None` value is a way to signify __empty__ or __no value here__. It's commonly defined as  

> Assigning a value of None to a variable is one way to reset it to its original, empty state.




