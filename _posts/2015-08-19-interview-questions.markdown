---
layout: post
title:  "General phone screen interview questions"
date:   2015-08-16 12:00:00
categories: Python
image:
  feature: sample-image-7.jpg
---

## How do you scale a write/read-heavy application?

* Read-heavy applications can be scaled by adding slaves to the database as well as web nodes for serving the requests. Caching is also a useful strategy for high concurrency. 
* Write-heavy applications  can be scaled by sharding the database. It serves to balance the write load as well as distribute the data across multiple machines. 

## What are parts of the infrastructure you need to consider when scaling out an application?

* Horizontal and vertical scaling
* Read/write heavy applications
* Application and storage servers 
* Application CPU
* Memory
* Storage
* Database replication / sharding 
* Caching
* Network

## What is the difference between a thread and a process?

* Threads are used for small tasks, whereas processes are used for more 'heavyweight' tasks – basically the execution of applications. Another difference between a thread and a process is that threadswithin the same process share the same address space, whereas different processes do not.

## What is the difference between asynchronous and synchronous request?

* Async (Non-blocking)
* Sync (blocking)

## What is the difference between UDP (User Datagram Protocol) and TCP (Transmission Control Protocol)?

### TCP

* HTTP, HTTPs, FTP, SMTP, TELNET
* Connection-oriented protocol
* A message makes its way across the internet from one computer to another. 
Suited for applications that required high reliability and transmission time is less critical

### UDP

* DNS, DHCP, TFTP, SNMP, RIP, VOIP
* Connectionless protocol
* One program can send a load of packets to another and that would be the end of the relationship.
* Suited for application that need fast, efficient transmissions, such as games

## What is a load balancer and how is it useful for a web application?

* A load balancer is a device that acts as a reverse proxy and distributes network or application traffic across a number of servers. Load balancers are used to increase capacity (concurrent users) and reliability of applications.

## Describe the difference between LEFT, RIGHT, NATURAL joins used in MySQL?

* LEFT JOIN is same as LEFT OUTER JOIN and means to show all records from left table (i.e. the one that precedes in SQL statement) regardless of the existence of matching records in the right table.
* RIGHT JOIN is same as RIGHT OUTER JOIN and means opposite of LEFT JOIN, i.e. shows all records from the second (right) table and only matching records from first (left) table.
* JOIN records that match in both tables

## What kind of tables are required for a many-to-many relationship?

* Links table that contains the primary key from both tables

## What is an index? What are the advantages / disadvantages?

* Most MySQL indexes (PRIMARY KEY, UNIQUE, INDEX, and FULLTEXT) are stored in B-trees.

## Define the terms models, views, controllers, helpers, libraries and hooks, routing

* Model–View–Controller (MVC) is a type of computer user interface that separates the representation of information from the user's interaction with it.[1][2] The model consists of application data and business rules, and the controller mediates input, converting it to commands for the model or view.[3] A view can be any output representation of data, such as a chart or a diagram.

## What is function overloading?

* Allows creating several methods with the same name which differ from each other in the type of the input and the output of the function. It is simply defined as the ability of one function to perform different tasks.

## What is an interface in the JAVA world?

* An interface is a contract specifying a set of methods, fields and properties which will be available on any implementing object

## What is dependency injection?

* Dependency injection is a software design pattern in which one or more dependencies (or services) are injected, or passed byreference, into a dependent object (or client) and are made part of the client's state. The pattern separates the creation of a client's dependencies from its own behavior, which allows program designs to be loosely coupled and to follow the dependency inversion and single responsibility principles.

## Describe the the factory pattern and explain how it is useful?

* The factory method pattern is an object-oriented creational design pattern to implement the concept of factories and deals with the problem of creating objects (products) without specifying the exact class of object that will be created.

## Describe the singleton pattern and explain how it is useful

* In software engineering, the singleton pattern is a design pattern that restricts the instantiation of a class to one object.


## What is SQL injection?

* SQL injection is a security vulnerability which allows intruder to steal data from system. Any system which take input from user and create SQL query without validating or sanitizing that input is vulnerable to SQL injection. In such system, intruder can inject SQL code instead of data to retrieve more than expected data. There are many instances on which sensitive information e.g. user id, password and personal details are stolen by exploiting this vulnerability. In Java, you can avoid SQL injection by using Prepared statement.

## What is a strongly typed programming language? (answer)

* In a strongly typed language compiler ensure type correctness, for example you can not store number in String or vice-versa. Java is a strongly typed language, that's why you have different data types e.g. int, float, String, char, boolean etc. You can only store compatible values in respective types. 

## How do you find a  running Java process on UNIX? (command)

* You can use combination of 'ps' and 'grep' command to find any process running on UNIX machine. Suppose your Java process has a name or any text which you can use to match against just use following command.

## What are some important differences between a linked list and an array? 

* linked list and array are two of the most important data structure in programming world. Most significant difference between them is that array stores its element at contiguous location while linked list stores its data anywhere in memory. 

## What is loose-coupling?

* Loose coupling is a desirable quality of software, which allows one part of software to modify without affecting other part of software. For example in a loosely coupled software a change in UI layout should not affect the back-end class structure.

## Can you describe three different kinds of testing that might be performed on an application before it goes live?

* unit testing, integration testing and smoke testing. Unit testing is used to test individual units to verify whether they are working as expected, integration testing is done to verify whether individually tested module can work together or not and smoke testing is a way to test whether most common functionality of software is working properly or not e.g. in a flight booking website, you should be able to book, cancel or change flights.

## How do you get the last digit of an integer?

* By using modulus operator, number % 10 returns the last digit of the number, for example 2345%10 will return 5 and 567%10 will return 7.  Similarly division operator can be used to get rid of last digit of  a number e.g. 2345/10 will give 234 and 567/10 will return 56. This is an important technique to know and useful to solve problems like number palindrome or reversing numbers.

## What is the difference between asynchronous and synchronous request?

* Async (Non-blocking)
* Sync (blocking)

## What is an index? What are the advantages / disadvantages?

* Most MySQL indexes (PRIMARY KEY, UNIQUE, INDEX, and FULLTEXT) are stored in B-trees.

## What are bad attributes for a unit test?

* Tests with external dependencies (DB, file, server, time…)
* Tests that depend on each other
* Tests that verify the implementation rather than the behaviour
* Test that are so slow that no one executes them
* Tests test too many things

## What is the advantage of test driven development?

* The application is written for testability
* Tests for every feature get written
* Refactor code without fear of breaking functionality
* Write minimal code

## What is mocking in the contexts of software testing and why would do you need to use it?

* Verify interaction and test code in isolation 

## What is code coverage and how is it measured?

* How many lines/blocks/arcs of your code are executed while the automated tests are running

## What is the difference between a thread and a process?

* Threads are used for small tasks, whereas processes are used for more 'heavyweight' tasks – basically the execution of applications. Another difference between a thread and a process is that threads within the same process share the same address space, whereas different processes do not.

## What is a load balancer and how is it useful for a web application?

* A load balancer is a device that acts as a reverse proxy and distributes network or application traffic across a number of servers. Load balancers are used to increase capacity (concurrent users) and reliability of applications.

## What kind of tables are required for a many-to-many relationship?

* Many to many — Example student and course
* Links table that contains the primary key from both tables

## Define the terms models, views, controllers, helpers, libraries and hooks, routing

* Model–View–Controller (MVC) is a type of computer user interface that separates the representation of information from the user's interaction with it.[1][2] The model consists of application data and business rules, and the controller mediates input, converting it to commands for the model or view.[3] A view can be any output representation of data, such as a chart or a diagram.

## What is the difference between passing by reference and passing by value?

* Passing by reference means the called functions' parameter will be the same as the callers' passed argument (not the value, but the identity - the variable itself). Pass by value means the called functions' parameter will be a copy of the callers' passed argument.

## What is function overloading?

* that allows creating several methods with the same name which differ from each other in the type of the input and the output of the function. It is simply defined as the ability of one function to perform different tasks.

## What is an interface in the context of JAVA?

* An interface is a contract specifying a set of methods, fields and properties which will be available on any implementing object

## What’s the difference between http and https? What are the default ports?

* Data transferred of https is encrypted and port 80 / 443

## What is the difference between UDP (User Datagram Protocol) and TCP (Transmission Control Protocol)?

* TCP
* HTTP, HTTPs, FTP, SMTP, TELNET
* Connection-oriented protocol
* A message makes its way across the internet from one computer to another. 
* Suited for applications that required high reliability and transmission time is less critical
* UDP
* DNS, DHCP, TFTP, SNMP, RIP, VOIP
* Connectionless protocol
* One program can send a load of packets to another and that would be the end of the relationship.
* Suited for application that need fast, efficient transmissions, such as games, video / sound streaming 

## What is dependency injection?

* Dependency injection is a software design pattern in which one or more dependencies (or services) are injected, or passed by reference, into a dependent object (or client) and are made part of the client's state. The pattern separates the creation of a client's dependencies from its own behavior, which allows program designs to be loosely coupled and to follow the dependency inversion and single responsibility principles.

## Describe the the factory pattern and explain how it is useful?

* The factory method pattern is an object-oriented creational design pattern to implement the concept of factories and deals with the problem of creating objects (products) without specifying the exact class of object that will be created.

## Describe the singleton pattern and explain how it is useful

* In software engineering, the singleton pattern is a design pattern that restricts the instantiation of a class to one object.

## How do you scale a write/read-heavy application?

* Read-heavy applications can be scaled by adding slaves to the database as well as web nodes for serving the requests. Caching is also a useful strategy for high concurrency. 
* Write-heavy applications  can be scaled by sharding the database. It serves to balance the write load as well as distribute the data across multiple machines. 

## What are important metrics to monitor for web application performance?

* CPU
* Memory usage 
* Storage capacity
* Network bandwidth

## How do you debug an http request between a client and server?

* tcpdump
* wireshark

## What’s the difference between chmod and chown in unix?

* chmod changes file permissions, such as read/write access, while chown changes ownership. chmod lets someone borrow your file, while chown gives(or takes) it away.

## What are some unix package managers?

* yum
* pip
* pecl
* brew

## How do file and directory permissions work on unix?

* What does 755 do?

## What does the tail command do in unix?

* By default, tail will output the last 10 lines of its input to the standard output. With command line options, the amount of output and the units (lines, blocks or bytes) may be changed.

## How do you copy a file from one server to another through unix command line?

* scp

## Explain how ssh keys work?

* pub and private keys