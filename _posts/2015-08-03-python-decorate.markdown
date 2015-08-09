---
layout: post
title:  "Python decorate pattern"
date:   2015-06-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

A decorate pattern is simply a wrapper that is used to extend the behavior of a function without actually modifying the function.

For example (sourced from [here](http://thecodeship.com/patterns/guide-to-python-function-decorators/)), the function prints out a string given a name as an argument.

{% highlight python %}
def get_text(name):
  return "lorem ipsum, {0} dolor sit amet".format(name)
{% endhighlight %}

Now if we wanted to extend the `get_text` function to add html `<p>` tags, then we would create a wrapper that takes a function as an argument.

{% highlight python %}
def p_decorate(func):
  def func_wrapper(name):
    return "<p>{0}</p>".format(func(name))

  return func_wrapper

print get_text("John") # lorem ipsum, John dolor sit amet
{% endhighlight %}

Next, we simply assign the decorate function given the primary function `get_text` as an argument.

{% highlight python %}
my_get_text = p_decorate(get_text) # This is what takes place when you add @p_decorate

print p_decorate(get_text)("John") # <p>lorem ipsum, John dolor sit amet</p>
print my_get_text("John") # <p>lorem ipsum, John dolor sit amet</p>
{% endhighlight %}

Python provides syntatic sugar by prefixing your decorate function by `@` you can extend a functions behavior by essentially making a call to the wrapper.

{% highlight python %}
@p_decorate
def get_text(name):
  return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("John") # <p>lorem ipsum, John dolor sit amet</p>
{% endhighlight %}