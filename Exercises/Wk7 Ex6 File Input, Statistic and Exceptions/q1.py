# A00258304

while True:
    inputStr = input("Enter your GPA (0.0–4.0): ")
    
    try:
        gpa = float(inputStr)        
    except ValueError:
        print("Invalid input: please enter a number between 0 and 4. Try again.")
        continue    

    # if gpa < 0.0 or gpa > 4.0:
    #     print("Invalid GPA: must be between 0.0 and 4.0. Try again.")
    #     continue

    try:
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError
    except ValueError:
        print("Invalid GPA: must be between 0.0 and 4.0. Try again.")
        continue

    if 0.0 <= gpa < 1.0:
        print("Fail")
    elif 1.0 <= gpa <= 1.99:
        print("Third Class Honours / Pass")
    elif 2.0 <= gpa <= 2.99:
        print("Second Class Honours, Grade 2")
    elif 3.0 <= gpa <= 3.69:
        print("Second Class Honours, Grade 1")
    elif 3.7 <= gpa <= 4.0:
        print("First Class Honours")
    break
