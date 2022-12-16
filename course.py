TOPICS = {
    "algebra1": [
        "linear equations", "graphs", "inequalities", "functions", 
        "sequences", "exponents", "quadratics", "irrational numbers"
    ],
    "geometry": [
        "lines", "angles", "shapes", "planes", "area/perimeter",
        "volume/surface area", "pythagorean theorum", "congruence",
        "circles"
    ],
    "algebra2": [
        "polynomials", "complex numbers", "rational exponenents", "exponential models",
        "logarithms", "system of equations", "trigonometry"
    ],
    "precalculus": [
        "inverse functions", "rational functions", "conics", "vectors", "matrices",
        "probability", "limits", "continuity"
    ],
    "calculus": [
        "derivatives", "chain rule", "Lhopital's rule", "analyzing functions", 
        "integrals", "differential equations"
    ]
}

class Course():
    
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.familiarity = self.check_understanding()
        
    def check_understanding(self):
        print("Enter yes or no if you understand the following " + self.name + " topics...")
        count = 0
        for topic in TOPICS[self.name]:
            familiar = input(topic + ": ")
            if familiar == "yes":
                count += 1
        
        return round(count / len(TOPICS[self.name]), 2)