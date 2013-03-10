# Project Euler Problem 1

**Problem Statement**

>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

>Find the sum of all the multiples of 3 or 5 below 1000.

*Logic*

Generating the list of 3 multiples and 5 multiples. This list would contain certain duplicates that are multiples of 15. So converting the list to a set ensures no duplicates. The final list is summed.  

[problem link](http://projecteuler.net/problem=1)