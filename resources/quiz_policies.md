Computational Bootcamp Quiz Policies
-----

- Quizzes are closed book, notes, and Internet. 

-  The quiz could be on any material up to now, including prework sent before classes begin. Since programming is cumulative, assume all quizzes are cumulative. Other prework (e.g., optional or challenge) or prework for the current day of the quiz will *not* be on the quiz.

-  You will have one chance to answer each question and they will appear in random order.

-  Quizzes require Respondus LockDown Browser to be installed on your personal computer.
    +  Please work through the quick start guide [here](http://www.respondus.com/downloads/RLDB-QuickStartGuide-Instructure-Student.pdf).
    - Please install it before hand. Familiarize yourself with it. A link to sample quiz is here [TODO]. All quizzes will start promptly at 9am on Monday. Failure to install the required software will result in a zero for the quiz.
    - It only works with [Windows and Mac](https://www.respondus.com/products/lockdown-browser/requirements.shtml). Let the instructor by 07-12-19 that you'll need accommodation for all four quizzes and why (e.g., I have Linux).

- Your computer must in good working order. You must notify the instructor electronically before the start of the quiz (i.e., send Slack message before 9am on Mondays) the precise reason for an accommodations for the quiz that day. If fail to do that or if your computer stops working during the quiz, it is up the instructor's discretion to accommodate you.

- The quiz will take 40 minutes, and there will be approximately 15 questions.

- You can __not__ leave the room and re-enter the room once the quiz has started. Please use the restroom before 9am.

- You can __not__ ask questions during the quiz. Do your best to interpret the question on your own.

- Looking at any computer (including your phone or another student's computer) or any notes is considering cheating. You'll receive an automatic zero on the quiz. Other penalties for academic integrity violations are also possible.

- Once you finish the quiz, you have to leave the room. At a minimum, remaining in the room is a distraction to the other students still working on the quiz. Opening notes, browsing the Internet, or using your phone could be considered facilitating cheating. Just leave the room after submitting quiz.

Please reach out to the instructor about any questions or clarifications.

-----

You'll ask for it, here it is. Sample quiz questions:

1.  What is output of this code?
    
    ```python
    def func(my_list):
       my_list = [1, 2, 3, 4]; 
       print ("Values inside the function: ", my_list)

    my_list = [10, 20, 30]
    func(my_list)
    print("Values outside the function: ", my_list)
    ```
    A. Values inside the function:  [1, 2, 3, 4]   
    Values outside the function:  [10, 20, 30]
     
    B. Values inside the function:  [10, 20, 30]   
    Values outside the function:  [10, 20, 30]

    C. Values inside the function:  [1, 2, 3, 4]   
    Values outside the function: [1, 2, 3, 4]

    D. None of the above   

    Correct answer is: 

    <!--- A --->  (It is hidden in the website code. Look at the raw HTML.)

1. What is output of this code?

    ```python
    x = 50
     
    def func():
        global x
        print('The value of x is', x)
        return
        x = 2

    func()
    print('The value of x', x)
    ```
    A. The value of x is 2  
    The value of x 50
    
    
    B. The value of x is 50  
    The value of x 2

    C. The value of x is 50  
    The value of x 50
    
    D. None of the above 

    Correct answer is: 

    <!--- C ---> (It is hidden in the website code. Look at the raw HTML.)
