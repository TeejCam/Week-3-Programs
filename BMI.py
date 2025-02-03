print("Hello! I will ask you to enter your weight in pounds and height in feet and inches.")

def userWeightAndHeight():
    #using a try-except block
    try:
        #this try-except block fulfills the data-type check requirement
        weight = float(input("Please enter your weight in pounds: "))
        #using nested if statements
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")

        heightFt = float(input("Please enter your height in feet: "))
        if heightFt <= 0:
            raise ValueError("Height must be greater than zero.")

        heightIn = float(input("Please enter your height in inches: "))
        #this satisfies the range validation requirement
        if heightIn <= 0 or heightIn >= 12:
            raise ValueError("Invalid input for inches.")

        heightTotal = (heightFt * 12) + heightIn
        return weight, heightTotal

    except ValueError as e:
        print(f"Error: {e}")
        exit()

def calculateBMI(pounds, inches):
    #modified function to satisfy parameter validation requirement
    try:
        pounds = float(pounds)
        if pounds <= 0:
            raise ValueError("Input was either negative, zero, or invalid data type")

        inches = float(inches)
        if inches <= 0:
            raise ValueError("Input was either negative, zero, or invalid data type")
        BMI = (pounds / (inches*inches)) * 703
        return BMI

    except ValueError as e:
        print(e)
        exit()

def display():
    weight, heightTotal = userWeightAndHeight()

    #fulfills activity requirement of using assertions
    assert isinstance(weight, float), "Invalid input."
    assert isinstance(heightTotal, float), "Invalid input."

    BMI = calculateBMI(weight, heightTotal)
    print("BMI: ", f"{BMI:.1f}")
    print("Underweight: < 18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25.0-29.9")

display()









