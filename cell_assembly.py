from course import Course
import random

CURRICULUM = ["algebra1", "geometry", "algebra2", "precalculus", "calculus"]

def main():
    iterations = input("How many days of learning do you have?: ")
    environment = input("Is your learning environment supportive or unsupportive?: ")
    while not (environment == "supportive" or environment == "unsupportive"):
        environment = input("Please answer again (supportive/unsupportive): ")
    print("On a scale from 1-10 (1: confusion, 10: clarity), enter your level of comfort for the following courses...")
    courses = []
    for course in CURRICULUM:
        rating = input(course.capitalize() + ": ")
        course = Course(course, rating)
        courses.append(course)
    
    learn(courses, iterations, environment)

def learn(courses, iterations, environment):
    #Initalize learning rate - higher learning rate for supportive environments
    if environment == "supportive":
        learning_rate = random.uniform(0.4, 0.6)
    else:
        learning_rate = random.uniform(0.1, 0.3)
    
    for course in courses:
        if course.familiarity <= .80: #does not meet threshold to learn next topic
            #TODO:
            return
            
    
if __name__ == "__main__":
    main()
