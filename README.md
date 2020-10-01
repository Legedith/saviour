# SAVIOUR

## Inspiration

There were three main problems we faced when we started with programming: 

First: We didn't have an active internet connection and since all the coding challenge websites like Hackerank and CodeWars worked only with an internet connection, it was particularly difficult to practice our skills. 

Second: We had to search StackOverflow and other platforms to find solutions for programming problems. But, a lot of times the code would not be explained properly and we had a hard time figuring out what it did. Also sometimes we'd write code without properly documenting it or adding comments and then later wonder how it worked.

Third: We didn't knew how to style our code properly or what styling practices to follow. 

We created a python package that helps us with all these issues aka our Saviour.

## What it does
It has three main components, you can view a list of commands by running saviour-help. They are 
<ul>
<<<<<<< HEAD
<li>Saviour-style -> Use for code styling using pep8 standards</li>
<li>Savior-pseudocode -> Use for generating pseudocode from a program</li>
<li>Savior-practice -> Use for practicing programming questions offline</li>
</ul>
=======
<li>Saviour-style -> used for code styling using pep8 standards</li>
<li>Savior-pseudocode -> used for generating pseudocode from a program</li>
<li>Savior-practice -> Used for practicing programming questions offline</li>
</ul>

## How We built it
We have used UiPath automation tool to scrap the questions data from the Project Euler website.

For the code styling, we used autopep8 to conform the python code to pep8 styling standards. 

The pseudocode generator works primarily by replacing certain keywords and functions from a normal line of code to plain-english so it is understandable by anyone.

## Challenges We ran into
3 of our team members are new to programming with python, so we had some difficulty working with packages.
The autopep8 library had poor documentation so it took time to get it to work. We had to make the output code not only correct but also highly presentable.
The pseudocode generation part was particularly difficult as we had to consider a lot of conditions to get it to output in as simple English as possible.
Other than that, we all live in different time zones, so we had to literally keep track of each other's progress everytime.

## Accomplishments that we're proud of
We are proud of the fact that we were able to make a program closest to the actual idea we had. 

## What we learned
+ Data scraping using UiPath
+ Pep8 code styling standards
+ Making python packages and command line scripts

## What's next for Savior
We will work towards building an even smarter pseudocode generator that can work with multiple programming languages. We will try to add more questions to our offline Saviour-practice module.
>>>>>>> abf18594060545b40c0c9e1975c72ded241fd84e
