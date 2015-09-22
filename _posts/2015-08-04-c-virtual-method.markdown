---
layout: post
title:  "C++ virtual functions"
date:   2015-06-05 12:00:00
categories: Apache Spark
image:
  feature: sample-image-7.jpg
---

Virtual methods allow the subclass methods to be called even if the pointer is of type base class. The code snippet is taken from [Stack Overflow](http://stackoverflow.com/questions/2391679/why-do-we-need-virtual-methods-in-c):

{% highlight c++ %}
class Base
{
  public:
    void Method1() {
      std::cout << "Base::Method1" << std::endl;
    }
    virtual void Method2() {
      std::cout << "Base::Method2" << std::endl;
    }
};

class Derived : public Base
{
  public:
    void Method1() {
      std::cout << "Derived::Method1" << std::endl;
    }
    void Method2() {
      std::cout << "Derived::Method2" << std::endl;
    }
};

//  Note - constructed as Derived, but pointer stored as Base*
Base* obj = new Derived ();

obj->Method1 ();  //  Prints "Base::Method1"
obj->Method2 ();  //  Prints "Derived::Method2"
{% endhighlight %}

If the `virtual` qualifier is missing from `Method2` then we would have early binding and the only the method in the base class would be available.

{% highlight c++ %}
class Base
{
  public:
    void Method1() {
      std::cout << "Base::Method1" << std::endl;
    }
    void Method2() {
      std::cout << "Base::Method2" << std::endl;
    }
};

class Derived : public Base
{
  public:
    void Method1() {
      std::cout << "Derived::Method1" << std::endl;
    }
    void Method2() {
      std::cout << "Derived::Method2" << std::endl;
    }
}

//  Note - constructed as Derived, but pointer stored as Base*
Base* obj = new Derived();

obj->Method1();  //  Prints "Base::Method1"
obj->Method2();  //  Prints "Base::Method2"
{% endhighlight %}





