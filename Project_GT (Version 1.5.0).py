"""
Created: 9/10/2022

Contributers:
Garrison Knapp
Max Gwartney
"""

# Importing Packages & Libraries
import operator
import random
import time

# Public/Global Variables
program_version = "Project GT: Version 1.5.0 | Not So Basic Mathematician"
numberOfProblems = 20
replay = "y"

# Generates and displays a problem; return its solution
def genProblem():

    # Dictionary of operators
    ops_diction = {"+" : operator.add,
                   "-" : operator.sub}

    # Generates two variables
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)

    # Randomly selects an operator from the operator dictionary and then generates a problem as well as its solution
    op = random.choice(list(ops_diction.keys()))
    solution = ops_diction.get(op)(num1,num2)

    # If statement that decides how to display the problem
    if op == "-" and num2 < 0:

        # If the second number is negative, then put parathesis around it
        print("{} {} ({})".format(num1, op, num2))
    
    else:

        # If the second number is not negative, then don't print parathesis
        print("{} {} {}".format(num1, op, num2))

    # Return the solution to the generated problem
    return solution

# Ask user for an answer to a randomly generated problem
def askUser():

    # Calls genProbelm function; This displays the problem and stores the solution of the problem
    solution = genProblem()

    # Error Handling
    try:

        # Looks for user input as a float value and stores it to user_answer
        user_answer = float(input())

    except:

        # if there is an error with the user's answer; set the answer to nothing
        user_answer = None

    # Returns a true/fales value to determine whether or not the user's answer was correct or not
    return user_answer == solution

# Generates a set of problems for the user to solve
def problemSet():

    # Keeps track of how many problems were answered correctly as well as declares elapsed_problem_set_time to keep track of time spent on this problem set
    score = 0
    elapsed_problem_set_time = 0

    # Prints out information regarding number of problems in the set
    print("{} problem(s) in this set:".format(numberOfProblems))

    # Loops for x (numberOfProblems) amount of solvable problems
    for i in range(numberOfProblems):

        # Checks the time the problem was displayed
        problemStartTime = time.time()
        
        # Calls askUser Function; Returns a true/false value based on if the user's answer was correct
        correct = askUser()

        # Checks the time when the user answered the problem
        problemEndTime = time.time()

        # Finds the difference between the time the problem was first displayed and the time the user answered the problem and adds that time to the elapse time
        elapsed_problem_set_time += problemEndTime - problemStartTime

        # if correct is true (The user's answer was correctly)
        if correct:

            # Display the user got the answer correct and adds one to score
            score += 1
            print('Correct!\n')

        else:

            # Display the user got the answer incorrect
            print('Incorrect!\n')
    
    # Return a printable statement that displays the performance of the user                                                                           finds the average time spent per problem      finds the elapsed time for the problem set
    return 'Performance Results:\nScore: {}/{}\nAverage time per problem: {} second(s) \nElapsed time: {} seconds'.format(score, numberOfProblems, round(elapsed_problem_set_time / numberOfProblems, 2), round(elapsed_problem_set_time, 2))

# If replay is yes (y) then keep rerunning the program
while(replay == 'y'):

    # Prints out project version to the terminal
    print(program_version)
    print(" ")

    # Runs the main bulk of the program basically
    print(problemSet())

    # Asks the user if they would like to replay the program
    print(" ")
    replay = input("Would you like to try again? (y/n): ")
    print(" ")

# Program Exit message
print("Remember, practice till you can't get it wrong! :)")