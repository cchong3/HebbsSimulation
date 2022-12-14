"""
Authors: Crystal Chong & Emilie Grand'Pierre
Course: CSCI 3400 / DCS 3400
Assignment: FInal Project 
Date: December 19, 2022 

Description:
The courses class stores the key attributes of each facet of math 
used in building our cell assembly. 
"""

TOPICS = {
    "Algebra1": [
        "linear equations", "graphs", "inequalities", "functions", 
        "sequences", "exponents", "quadratics", "irrational numbers"
    ],
    "Geometry": [
        "lines", "angles", "shapes", "planes", "area/perimeter",
        "volume/surface area", "pythagorean theorum", "congruence",
        "circles"
    ],
    "Algebra2": [
        "polynomials", "complex numbers", "rational exponenents", "exponential models",
        "logarithms", "system of equations", "trigonometry"
    ],
    "Precalculus": [
        "inverse functions", "rational functions", "conics", "vectors", "matrices",
        "probability", "limits", "continuity"
    ],
    "Calculus": [
        "derivatives", "chain rule", "Lhopital's rule", "analyzing functions", 
        "integrals", "differential equations"
    ]
}

class Course():
    
    def __init__(self, name, rating, learning_rate):
        self.name = name
        self.rating = rating/10
        self.learning_rate = learning_rate
        self.adjust_learning_rate()
        self.score = 0
    
    def adjust_learning_rate(self):
        #Only existing confusion reduces learning rate
        if self.rating < 0.4:
            self.learning_rate = round(self.learning_rate * 0.95, 3)
            
    def check_understanding(self):
        print("Enter yes/no if you understand the following " + self.name + " topics...")
        count = 0
        for topic in TOPICS[self.name]:
            familiar = input(topic + ": ")
            while not (familiar == "yes" or familiar == "no"):
                familiar = input("Please answer again (yes/no): ")
            if familiar == "yes":
                count += 1
        self.score = round(count / len(TOPICS[self.name]), 2)
        print("Topic understanding score:", self.score)
        return self.score

    def __str__(self):
        return self.name
