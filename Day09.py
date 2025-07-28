import csv
from importlib import import_module  ###Day 09###
from importlib.resources import contents
from os import write


##Practice Question #1##
# Small Coding Task (Day 9)
# Build a file reader function that:
# Takes a filename as input.
# Handles FileNotFoundError, UnicodeDecodeError, and PermissionError.
# Logs errors to a separate file (error_log.txt).
# Always closes the file (with finally block or with statement).

def fileReader(fileName):
    try:
        with open(fileName, 'r',encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        log_error(f"FileNotFoundError: The file '{fileName}' was not found.")

    except UnicodeError:
        log_error(f"UnicodeError: Cannot decode contents of The file {fileName}")

    except PermissionError:
        log_error(f"PermissionError: No permission to read the file '{fileName}'.")

    finally:
        file.close()



from datetime import datetime
def log_error(message):
    current_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    with open("error-log.txt", 'a') as log:
        log.write(f"Error logged at {current_time} , with message: {message}")

    print(message)


##Practice Question #3 ##
# Write a function to divide two numbers and handle division by zero.
def divisionByZero(a,b):
    try:
        c= a/b
    except divisionByZero(a,b):
        print("Cannot divide by 0")



##Prctice Questions #4 ##
#Catch invalid input from a user (e.g., letters when expecting numbers).
def detectingIncorrectInput():
        number= input("Please enter your phone number: ")
        try:
            int_number = int(number)
            print(f"Thank you for the right number: {number} ")
        except ValueError:
            print("Please do not enter letters only numbers")

## Practice Question #5 ##
# Read from a CSV and handle FileNotFoundError if the file is missing.
def readingCSV(filename):
    try:
        with open(filename,'r', newline='', encoding='utf-8') as file:
            contents = csv.reader(file)
            for row in contents:
                print(row)

    except FileNotFoundError:
        print("File not found")




