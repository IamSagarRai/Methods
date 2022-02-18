class Programmer:
    company = "Microsoft"

    def __init__(self, name, area, country):
        self.name = name
        self.area = area
        self.country = country

    def info(self):
        print(f"The name of the programmer is {self.name}")
        print(f"The area of the programmer is {self.area}")
        print(f"The country of the programmer is {self.country}")


Benjamin = Programmer("Benjamin", "Software Engineer", "Paper towns")
Arthur = Programmer("Arthur", "Guy", "U.S")
Benjamin.info()
Arthur.info()



