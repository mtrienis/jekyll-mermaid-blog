---
layout: post
title:  "Python closures and late binding"
date:   2015-08-16 12:00:00
categories: Python
image:
  feature: sample-image-7.jpg
---

The expected output of the print statement is `[0, 2, 4, 6]` based on the element-wise operation `[0*2, 1*2, 2*2, 3*2]` where each element in list represents `i*x`. However, `[3*2, 3*2, 3*2, 3*2] = [6, 6, 6, 6]` is what is actually calculated.  

{% highlight python %}
def multipliers():
    return [lambda x : i*x for i in range(4)]

print [m(2) for m in multipliers()] # [6, 6, 6, 6]
{% endhighlight %}

The function returns `[6, 6, 6, 6]` because the variable `i` is not passed to the the _lambda function_ until the loop `for i in range(4)` has been evaluated. That's why `i` is the last element of the list `[0, 1, 2, 3]` list.