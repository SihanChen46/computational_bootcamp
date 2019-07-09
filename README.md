<center><h2>Computation for Analytics <br> University of San Francisco's MSDS 501 Summer 2019</h2></center>

<center><img src="https://imgs.xkcd.com/comics/python.png" style="width: 40%"/></center>

----
Course Description
----

This short bootcamp-style course is part of the [MS in Data Science (formerly MS Analytics) program at the University of San Francisco](https://www.usfca.edu/arts-sciences/graduate-programs/data-science) and is specifically designed as a catalyst to improve computer programming skills for those who are not yet skilled programmers. The course will focus on the applied computer programming concepts and skills directly related to data science.

Writing software is about problem-solving, data structures, algorithms, computer languages, libraries, software tools, and computing devices. In this course, I'm going to teach you how to approach programming, review the key elements of Python, teach you how to leverage Python to solve data science programs, introduce you to the command line, and finally introduce you to cloud computing. You'll go deeper into fundamental data structures and algorithms later in the MSDS program in a course that specifics cover those topics.

----
Logistics
----

__Instructor:__ Brian Spiering   
__Contact__: [Slack @Brian Spiering](https://msan-usf.slack.com/messages/DAMAXHTL5) (more preferred) | [bspiering@usfca.edu](mailto:bspiering@usfca.edu) (less preferred)  
__Office hours__: Mondays and Thursdays<sup>*</sup> from 12:30-1:00p   
\* Except: 1st week Tuesday (07/09) from 12:30-1 and Thursday (07/011) from 3-3:30; 2nd week Thursday  (07/18) from 3-3:30.

__Grader__: Robert Sandor  
__Contact__: [Slack @rsandor](https://msan-usf.slack.com/messages/DCKPG71FD) | [risandor@usfca.edu](mailto:risandor@usfca.edu) 

__Website__: [github.com/brianspiering/
computational_bootcamp](https://github.com/brianspiering/computational_bootcamp)    
__Communication__: Slack [`#comp_bootcamp`](https://msan-usf.slack.com/messages/CJZ738Q0J)  
__Location__: Classroom 155-156, 101 Howard St, San Francisco, CA   
__Sections__:

1. Mondays<sup>*</sup> and Thursdays from 10:00a-11:50a   
2. Mondays<sup>*</sup> and Thursdays from 1:00p-2:50p 

\* Except first week. Due to orientation, the first class will be on Tuesday (07/09)

You have been assigned a section, either the first section or the second section, for this course. You __must__ attend the section you have been assigned!

Anyone enrolled in the MSDS program can audit the course. You do __not__ need my permission or notify me if you want to audit. Just show up! I plan to record my lectures and make all materials available to all students. All the course materials are autograded so you can try the exercises and see where you stand.

Prerequisites
----

- Acceptance into the MSDS program.

Learning Outcomes
----

By the end of the course, you should be able to:  

1. Write Python programs to solve data-related problems.
1. Define common programming terms in your own words.
1. Use NumPy to efficiency perform complex numerical analysis.
1. Fluently use the Jupyter Notebook environment for writing, testing, and debugging Python code.
1. Read and use programming language documentation.
1. Use fundamental Unix command line tools, git, and GitHub.

----
Course Schedule and Topics (Tentative)
----
 
1. 07/09 
    - Welcome 
    - Overview of Python
    - Functions (built-in and user-defined)
    - Setting up your computer
1. 07/11
    - Booleans and truthiness
    - Conditionals
    - Looping with `for` and `while`   
    - NumPy (Numeric Python) library
1. 07/15 
    - Strings and string formatting 
    - List and list comprehensions  
    - Sets, dicts, and Counters
1. 07/18 Quiz #1 
1. 07/18
    - Bash
    - File handling  
    - git and GitHub  
1. 07/22 
    - Recursion   
    - Scripting   
1. 07/25 Quiz #2 
1. 07/25 
    - Object-oriented programming (OOP) and using classes   
    - Solving the same problem in multiple programming paradigms
1. 07/29 
    - Unicode  
    - Debugging
1. 08/01 Quiz #3  
1. 08/01
    - Review / Buffer day
    - Possible Topics:
        - Advanced functions: generators, decorators
        - Intermediate Python: `any`, `all`, `in`
        - Standard Library modules: `sys`, `os`, `collections`
1. 08/05
    - How to organize code (e.g., pep8)  
    - Refactoring 
    - Create your own modules  
1. 08/08 Quiz #4  
1. 08/08
    - Amazon Web Services (AWS), s3, and ec2   
    - Optional topics

Topics Not Covered
-----

- Introduction to programming (the course assumes you already know the very basics of programming)
- Implementation of fundamental programming data structures (e.g., linked lists)
- Implementation of fundamental programming algorithms (e.g., sorting)
- Python 2
- Other libraries in Python's data science stack: SciPy, scikit-learn, Pandas
- Tabular data storage and processing: JSON, CSV, parquet
- Advanced OOP: Multiple inheritance, static methods, property methods
- Dynamic programming  
- Data visualization 
- Concurrency, threading, `async` module
- Distributed computing
- Integrated development environment (IDE): PyCharm, Visual Studio Code
- Data acquisition: web architecture, web scraping, APIs, `requests` library 
- Automating AWS with `boto` library

----
Textbooks
----

The required textbook is _Fundamentals of Python Programming_ by Richard L. Halterman. Generously made available for free [here]( http://python.cs.southern.edu/pythonbook/pythonbook.pdf).

Here are other suggested books to help you become a better Python programmer:

- [Fluent Python: Clear, Concise, and Effective Programming](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008) by Luciano Ramalho 
- [Python Cookbook, Third edition](https://www.amazon.com/Python-Cookbook-Third-David-Beazley/dp/1449340377/) by David Beazley and Brian K. Jones

----
Grading
----

| Item           | Weight   |
|:---------------|:--------:|
| Professionalism| 10%      |  
| Labs           | 20%      |
| Projects       | 20%      |
| Quizzes        | 50%      |
| __Total__      | __100%__ |

Each item's contribution is capped its respective percentage. The total course percentage is capped at 100%.

Currently, there is no extra credit. If there is any extra credit, it is entirely at the discretion of the instructor.

We'll be using Canvas as the learning management system (LMS), aka the gradebook. The instructional team will do their best to have Canvas accurately reflect your current scores in the course. However, Canvas may not be completely accurate all the time. In other words, your actual grade maybe significant different than it appears on Canvas. 

### Professionalism

I expect you act professionally in-person (both inside and outside the classroom) and electronically. Since people come up from a variety of backgrounds, I want to be explicit about the elements of professionalism: 

- Show up on time and prepared.
- Remain fully present.
- Contribute appropriately and meaningfully.
- Follow staff and faculty instructions appropriately.
- Show respect to all people.

Professionalism points are entirely at the instructor's discretion. 

Violations of Academic Integrity are unprofessional, thus you'll automatically lose all Professionalism points for any violations of Academic Integrity.

Part of professionalism may include completing small ad hoc assignments, such as MSDS Student Info Survey and setting up online profiles for the tools MSDS program uses.

I try to create an active learning environment in my classroom. Attendance is mandatory, you can't participate if you don't attend. It is the responsibility of the student to attend all classes. If you have to miss class, due to sickness, job interviewing, or other circumstances, please notify your instructor by Slack in advance. Supporting documents (e.g., doctor’s notes) may be asked for.

Tardiness negatively impacts an active learning environment, thus will impact your professionalism grade.

You must show-up to each session prepared. Each person is important to the dynamic of the class, and therefore students are required to participate in class activities. Expect to be "cold called". I call on students at random not to put you on the spot but to keep you engaged in the material at all times.

This is a closed-computer classroom. Your phone and laptop must stay put away during the entire class, unless explicitly instructed by me that it is okay to use your laptop for a specific activity. I have directly observed that just the presence of phones and laptops negatively impacts the learning experience for everyone in the classroom. I expect you to be fully present and engaged in the classroom at all times. I _strongly_ suggest taking notes on paper. A tablet is acceptable for note-taking. A tablet should __not__ be used for any other purpose.

This is your warning around off-topic computer use. Violations include (but not limited to): looking at the screen, typing, and using any type of computer for activities not directly to the current in-class activities. Every violation will negatively impact your total grade by losing professional points. The penalties scale exponentially - The first offense is will result in a .5% loss of total points, the second offense is 1% of total points, the third offense is 3%, the fourth offense is 6%, and the fifth offense is 10% of total points (i.e., the cap is 100% of your professional points). 

### Quizzes

There be will be a quiz every Thursday, starting the second week, at 9 am for a total of 4 quizzes. Quizzes will be a combination of multiple choice, short answer, and programming questions.

Missing quizzes will only be accommodated for medical emergencies.

More detailed information is in the quiz policies document in the resources folder on the course website.

### Labs

Each lab will be a collection of short coding problems in Python. There will be 1 lab per week (for a total of 4, each lab is worth 5% of total grade). Each lab will due on Sunday by 9:00p submitted on Canvas.

Late assignments will only be accepted for medical emergencies.

Asking for acceptance of any late assignments without a medical emergency or submitting assignment not through Canvas will result in a loss of professionalism points (and your assignment will still not be accepted).

### Projects

Each project will be a series of interdependent coding problems in Python to accomplish a large goal. There will be 2 projects, each worth 10% of the total grade. 
 
1. Text Processing Project due 07-27-19 (Saturday) at 9p submitted on Canvas.
1. Image Processing Project due 08-10-19 (Saturday) at 9p submitted on Canvas.

Late projects will only be accepted for medical emergencies.

Asking for acceptance of any late assignments without a medical emergency or submitting assignment not through Canvas will result in a loss of professionalism points (and your assignment will still not be accepted).

Grading standards
----

The MSDS program considers a grade of "A" to represent exceptional work with respect to both the instructor's expectations and peer student achievements. I consider an "A" grade to be above and beyond what most students achieve. A grade of "B" represents the expected outcome, what is called "competence" in a business setting. A "C" grade represents achievements lower than the instructor's expectations for competence in the subject. A grade of "F" represents little or no work in the course.

I will "curve" the final numerical grades at the end of the course. The mapping from percentages to letter grades (e.g., [95, 100] is an A, [90,95) is an A-, etc.) will not be established until the end of the course. Roughly, the top 15% of students will receive grades of A or A-. Roughly, 60% of students will receive grades of B+, B, or B-. Roughly, 20% of students will receive grades of C+, C, or C-. Students can receive failing grades. I am not required by program to fail a particular percentage of students, but I will fail students if it is appropriate. Students who fail this course __cannot__ continue in the MSDS program. 

Students with disabilities
-----

If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact [USF Student Disability Services](https://myusf.usfca.edu/sds) (SDS) for information about accommodations.

Behavioral Expectations
----

All students are expected to behave in accordance with the [Student Conduct Code](https://myusf.usfca.edu/fogcutter) and other University policies.

Academic Integrity
-----

USF upholds the standards of honesty and integrity from all members of the academic community. All students are expected to know and adhere to the University's [Honor Code](https://myusf.usfca.edu/academic-integrity/).

You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action. Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation. You must also abide by the copyright laws of the United States.

The golden rule: **You must never represent another person’s work as your own.** Credit to [Terence Parr](https://github.com/parrt/msds689).

I generously post all my materials to a public GitHub repo. However, you should not post any solutions to GitHub (or anywhere else on the Internet). __Publicly posting any solutions to any problems for this course will result in a failing grade for this course.__

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

Counseling and Psychological Services (CAPS)
-----

CAPS provides confidential, free [counseling](https://myusf.usfca.edu/student-health-safety/caps) to student members of our community.

Confidentiality, Mandatory Reporting, and Sexual Assault
-------

For information and resources regarding sexual misconduct or assault visit the [Title IX](https://myusf.usfca.edu/TITLE-IX) coordinator or USF's [Callisto website](http://usfca.callistocampus.org/).
