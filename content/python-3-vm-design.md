Title: Could a Python interpreter run both Python 2 and 3?
Date: 2016-12-01 18:00
Tags: python, python3
Status: draft
Summary: 

Zed Shaw, the author of Learn Python the Hard Way, one of the most successful resources to teach Python to beginners,
[went on a rant on Python 3](https://learnpythonthehardway.org/book/nopython3.html) and why it supposedly is a
terrible language and beginners should steer away from it. Some of his arguments are dubious and borderline paranoid,
and [other people have done a decent job at debunking them](https://eev.ee/blog/2016/11/23/a-rebuttal-for-python-3/).
One of his points piqued my curiosity, though: he argues that, had the Python 3 VM been designed "properly", it would
have been able to run both Python 2 and Python 3 code. He says[^1]:

> * Python 3 uses a Virtual Machine (VM) just like Python 2 did.
> * The original design of Python 3 could have also run Python 2 in this same VM. They controlled both languages, and could make it work. They chose not to do this, and instead tell you to manually translate.
> * F#/C# and JRuby/Java are good examples of doing this. The former, when you have control over both languages. The latter, when you don't.
> * Successive versions of Java are another example of doing this, and may be closer to Python 2/3 integration.
> * Choosing not to support both Python 2 and Python 3 in the same VM makes the transition cost off Python 2 much higher than it needs to be. Rather than support a smooth transition, the Python project instead asks you to manually convert code instead of simply supporting both languages.
> * When asked why they don't run both, members of the Python project have actually told me this is impossible. This is a lie. It is not impossible, and in fact would have been the better design to help with migration.

So, why didn't the Python developers write a VM that supports both Python 2 and 3?

## How does the Python interpreter work?

Zed says:

> Python 3 uses a Virtual Machine (VM) just like Python 2 did.

This is true! When executing Python programs, the interpreter first compiles them down to intermediate bytecode that
the Python virtual machine then executes.

<insert simple diagram showing intermediate bytecode representation>

For example, suppose I want to execute the following Python file:

```python
#!/usr/bin/python3
print("o hai!")
```

When I run `$ python3 ohai.py`, this code first gets translated into bytecode instructions (this is the `.pyc` files
that get created alongside the Python source code). The bytecode is a series of operation code that tell the Python
virtual machine what to do in a form that is much more simpler and efficient than raw Python code is. Using the  `dis`
module, we can see that the above gets translated into something that looks like:

```python
  1           0 LOAD_NAME                0 (print)
              3 LOAD_CONST               0 ('o hai!')
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
              9 RETURN_VALUE
```

The Python virtual machine then executes those instructions one after the other. This is very similar to how Java and
the Java Virtual Machine work! We'll come back to this later.


## Why is Python 3 backwards-incompatible?

Read http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html!

The first of those were aimed at making the language easier to learn, and easier to maintain. Keeping deprecated
features around isn’t free: in order to maintain code that uses those features, everyone needs to remember them and new
developers need to be taught them. Python 2 had acquired a lot of quirks over the years, and the 3.x series allowed
such design mistakes to be corrected.

--> So moving this to the VM means keeping that cost of maintaining.

## Could the Python 3 VM address this?

Zed Shaw compared to different versions of Java, JRuby/Java. Could the same have happened?

My intuition: static vs dynamic. JVM has public spec -> impact? 


[^1]: This section of his post was amended, and originally went over a tangent about
Turing-completeness. You can find the original version (as long as a counter-argument)
[here](https://eev.ee/blog/2016/11/23/a-rebuttal-for-python-3/#you-should-be-able-to-run-2-and-3).
