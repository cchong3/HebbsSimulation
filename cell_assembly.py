"""
Authors: Crystal Chong & Emilie Grand'Pierre
Course: CSCI/DCS3400
Assignment: Final Project 
Date: December 19, 2022 

Description:
The cell_assembly file is the main method in a system that models a humans
cognitive architecture. Using one’s environment, prior knowledge, and alloted time,
this system builds and outputs a grpah that models the learning process.

Bugs: There are no known bugs within our code
"""

from course import Course
from course import TOPICS
import networkx as nx
from matplotlib import pyplot as plt
import random

CURRICULUM = ["Algebra1", "Geometry", "Algebra2", "Precalculus", "Calculus"]
SATISFICER_THRESHOLD = 0.85
MAXIMIZER_THRESHOLD = 0.95

def main():
    #Gather user input
    days = int(input("How many days of learning do you have?: "))
    environment = input("Is your learning environment supportive/unsupportive?: ")
    while not (environment == "supportive" or environment == "unsupportive"):
        environment = input("Please answer again (supportive/unsupportive): ")
    expert = input("Are you a satisficer or maximizer?: ")
    while not (expert == "satisficer" or expert == "maximizer"):
        expert = input("Please answer again (satisficer/maximizer): ")
    print("On a scale from 1-10 (1: confusion, 10: clarity), enter your level of comfort for the following courses...")
    courses = []
    for course in CURRICULUM:
        clarity_rating = int(input(course + ": "))
        while not (clarity_rating >= 1 and clarity_rating <= 10):
            clarity_rating = int(input("Please enter a valid rating (1-10): "))
        #Initialize learning rate - higher learning rate for supportive environments
        if environment == "supportive":
            learning_rate = random.uniform(0.2, 0.3)
        else:
            learning_rate = random.uniform(0.05, 0.15)
        course_obj = Course(course, clarity_rating, round(learning_rate, 2))
        courses.append(course_obj)
    
    #Evaluate current understanding
    need_to_learn = get_courses_to_learn(courses, expert)
    
    #Begin Learning
    duration = learn(need_to_learn, days, expert)
    
    #Output
    build_cell_assembly(courses)
    
    print("\n"+ "SUMMARY...")
    evaluation(duration, courses, expert, environment)

def get_courses_to_learn(courses, expert):
    need_to_learn = []
    for course in courses:
        score = course.check_understanding()
        if (expert == "satisficer"):
            #does not meet threshold to learn next topic
            if score < SATISFICER_THRESHOLD:
                need_to_learn.append(course)
        else:
            #must learn everything to learn next topic
            if score < MAXIMIZER_THRESHOLD:
                need_to_learn.append(course)
    return need_to_learn

def learn(courses_to_learn, iterations, expert):
    pointer = 0
    day = 0
    if expert == "satisficer":
        threshold = SATISFICER_THRESHOLD
    else:
        threshold = MAXIMIZER_THRESHOLD
    while day < iterations and pointer < len(courses_to_learn):
        current_course = courses_to_learn[pointer]
        print("Day", str(day) + ":", current_course.name)
        print("Learning rate:", current_course.learning_rate)
        current_course.score += (1-current_course.score) * current_course.learning_rate
        print("Progress:", str(round(current_course.score * 100, 2)) + "%")
        if current_course.score > threshold:
            pointer += 1
            #Increase learning rate by 0.05 for next course if maximizer
            if expert == "maximizer" and pointer < len(courses_to_learn):
                courses_to_learn[pointer].learning_rate += 0.05
        day += 1
    return day

def build_cell_assembly(courses):
    edges = []
    for i in range(len(courses) - 2):
        course = courses[i]
        mastered_topics = int(course.score * 10)
        for topic in TOPICS[course.name]:
            counter = 1
            if counter <= mastered_topics:
                edges.append([topic, course])
            counter += 1
        following_course = courses[i + 1]
        if course.score > SATISFICER_THRESHOLD and following_course.score > SATISFICER_THRESHOLD:
            edges.append([course, following_course])
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()
    
def evaluation(duration, courses, expert, environment):
    if expert == "satisficer":
        threshold = SATISFICER_THRESHOLD
    else:
        threshold = MAXIMIZER_THRESHOLD
    
    mastered = []
    incomplete = []
    for course in courses:
        if course.score > threshold:
            mastered.append(course.name)
        else:
            incomplete.append(course)
    
    print("MASTERED:", mastered)
    
    if (len(mastered) == len(courses)):
        print("Calculus knowledge achieved in", duration, "days of learning as a " + expert + ".")
    else:
        print("Calculus still in progress under " + environment + " and " + expert + " environment conditions.")
        #Predict number of days left to learn
        learning_days_left = 0
        pointer = 0
        while pointer < len(incomplete):
            course = incomplete[pointer]
            course.score += (1-course.score) * course.learning_rate
            if course.score >= threshold:
                pointer += 1
                #Increase learning rate by 0.05 for next course if maximizer
                if expert == "maximizer" and pointer < len(incomplete):
                    incomplete[pointer].learning_rate += 0.05
            learning_days_left += 1
        print("Completion of calculus is predicted to require ~" + str(learning_days_left) + " more days of learning.")
    
if __name__ == "__main__":
    main()
