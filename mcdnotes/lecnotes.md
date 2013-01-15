# PS 632: Computational Political Economy #
### Duke University, Spring 2013 ###
### Taught by Josh Cutler ###

## Lecture 1: Administrivia ##

**Names**:
Won
Max
Lucy
Amy
Kevin (undergrad ps)
Andy
Chris (undergrad senior econ/ps)

Main idea: simplify data collection

## Lecture 2: The World of Software ## ##

There are a number of cultures in the software world. We will introduce them in the order we'll study their ideas in this course. 

### Software Engineering ###

From this world, we will draw on the ideas of *source control* and *testing*. Software engineers work at IBM and wear tucked-in, button-up shirts. 

#### Source control ####

- file versioning
- multiple users
- git and https://github.com

Here are the git commands you should know. Try them out and write down what they do:

- `git init`
- `git add`
- `git commit -m`
- `git log`
- `git push`
- `git pull`
- `git status`

There are several rules of thumb for working with git. One of them is "one idea, one commit." In practice this means that you should be able to explain any commit in a one-sentence commit message (or shorter). At a minimum the code in a commit should work--don't break your teammates' code! 

#### Testing ####

There are a number of types of software tests. Manual testing is when you have human testers type or click their way through your program. That's labor intensive and not much fun. Integration tests are automated and make sure all the parts of your program place nicely with each other.

We are going to start on the ground floor with unit tests, which are the most basic type of automated tests. A test specifies what the correct behavior/result should be, and compares it to the actual process or output of the program. Under the Test-Driven Development (TDD) paradigm, you write your tests before you write your code. However, for the experimental nature of our code this is not always the best practice.

**If you write code that you can't test, you have written it incorrectly.**




Another important concept that may take some time to wrap your head around is *branching*. Making a branch allows you to work on something in parallel, without overwriting a version that works for some purpose. One example is branching your CV into academic and corporate versions. 

### Computer Science  ###

We will draw on computer science to understand *algorithms*. They have ponytails and beards. If you need encryption software, they cannnot be beat.

### Hackers ###

You will find hackers working at startups. They are the ones who put all the cool stuff together and make it useful in the real world. 





