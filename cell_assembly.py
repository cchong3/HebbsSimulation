from course import Course
import random

CURRICULUM = ["algebra1", "geometry", "algebra2", "precalculus", "calculus"]
EXPERT_THRESHOLD = 0.85

def main():
    #Gather user input
    days = int(input("How many days of learning do you have?: "))
    environment = input("Is your learning environment supportive/unsupportive?: ")
    while not (environment == "supportive" or environment == "unsupportive"):
        environment = input("Please answer again (supportive/unsupportive): ")
    print("On a scale from 1-10 (1: confusion, 10: clarity), enter your level of comfort for the following courses...")
    courses = []
    for course in CURRICULUM:
        clarity_rating = int(input(course.capitalize() + ": "))
        while not (clarity_rating >= 1 and clarity_rating <= 10):
            clarity_rating = int(input("Please enter a valid rating (1-10): "))
        #Initalize learning rate - higher learning rate for supportive environments
        if environment == "supportive":
            learning_rate = random.uniform(0.2, 0.3)
        else:
            learning_rate = random.uniform(0.05, 0.15)
        course_obj = Course(course, clarity_rating, learning_rate)
        courses.append(course_obj)
    
    #Evaluate current understanding
    need_to_learn = get_courses_to_learn(courses)
    
    #Begin Learning
    learn(need_to_learn, days)
    
    #Output
    #TODO: generate graph
    for course in courses:
        if course.score > EXPERT_THRESHOLD:
            print("MASTERED:", course.name, course.score)

def get_courses_to_learn(courses):
    need_to_learn = []
    for course in courses:
        #score = Course.check_understanding(course.name)
        score = course.check_understanding()
        #does not meet threshold to learn next topic
        if score < EXPERT_THRESHOLD:
            need_to_learn.append(course)
    return need_to_learn

def learn(courses_to_learn, iterations):
    pointer = 0
    day = 0
    while day < iterations and pointer < len(courses_to_learn):
        print("Day ", day)
        current_course = courses_to_learn[pointer]
        print("Learning", current_course.name)
        print("learning rate:", current_course.learning_rate)
        current_course.score += (1-current_course.score) * current_course.learning_rate
        print("Score:", current_course.score)
        if current_course.score > EXPERT_THRESHOLD:
            pointer += 1
        day += 1
    
if __name__ == "__main__":
    main()
