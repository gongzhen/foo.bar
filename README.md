##Purpose
This repository contains all of my completed Google [foobar](https://foobar.withgoogle.com/) problem sets.
I made the problem sets available  for anyone who wants to learn what types of
problems Google is using in the challenge, and how to potentially solve them.
For some context, the foobar challenge is a recruiting tactic that Google uses.
If you use Google search, and you search something of "interest" to Google,
(e.g. list comprehension python) they will present this challenge, in browser
to you. If you accept, you are taken to the challenge.

## Usage
<p align="center">
  <img src="https://github.com/RagingTiger/gifs/raw/master/foo.bar.gif"/>
</p>

## Description
Each program in the repository, named after the problem set from the
**foobar** challenge, has the problem statement, problem solution, and how to
execute and use the solution:

```
$ cat minion_hierarchy.py
#!/usr/bin/env python

'''
Author: John D. Anderson (TigerJ)
Usage: minion_hierarchy (int)
Origin: Google "foo.bar" project - Problem 1.1
Program Description:

    Minion hierarchy
    ================

    Rumor has it there's a mad scientist out there who had abducted hundres of
    rabbits to test out a new zombie serum.

    Agent Beta Rabbit, spy and brilliant mathematician, storms in the room:
    "I know who's behind that plan. It's a man who calls himself Professor
    Boolean. My preliminary recon data shows that he's operating a lab
    somewhere on the islands near Silicon Valley. I also recently got a tip
    that Professor Boolean's lab minions have a certain hierarchical structure:
    Each manager has no more than 7 direct reports."

    Interesting... This information can help us estimate how many minions are
    working in this lab, and thus, the size of this operation. We need to know
    what we're facing here.

    Write a function called answer(x) that returns the maximum number of minion
    employees a company following the "no more than 7 direct reports" theory
    can have, with no more than x levels of supervision.

    You can assumet that:
    1. Professor Boolean is the highest level of supervision and has no
       manager.
    2. Each minion employee (other than Professor Boolean) has exactly one
       manager.

    For example, with no more than 1 level of supervision, we could have a
    maximum of 8 employees: Professor Boolean and his 7 reports.

    x will be a positive integer, not exceeding 10.

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
        (int) x = 1
    Output:
        (int) 8

    Inputs:
        (int) x = 2
    Output:
        (int) 57

    Use verify [file] to test your solution and see how it does. When you are a
    finished editing your code, use submit [file] to submit your answer. If
    your solution passes the test cases, it will be removed from your home
    folder.
'''

# libs
import sys


# functions
def answer(x):
    y = 0
    for i in range(x+1):
        y += 7**i
    return y

# executable
if __name__ == '__main__':

    if len(sys.argv) == 2:
        print answer(int(sys.argv[1]))

    else:
        sys.exit('\nusage: minion_hierarchy (int)\n')
```