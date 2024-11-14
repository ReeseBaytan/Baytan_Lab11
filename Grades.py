Grades = []
passed = []
Valid = True

while True:
    Grade = input("Enter Grade (TYPE 'done' TO STOP):)")
     
     
     
    if Grade.lower() == 'done':
         break
    if not Grade.isdigit():
         print("ERROR")
    else:
        Grade = int(Grade)
    if Grade <= 40 or Grade > 100:
        print ("INVALID")
        Valid = False
        break
    else:
        Grades.append(Grade)
    if Grade >= 75:
        passed.append(Grade)
        
    if Valid:
        if Grades:
            
            average = sum(Grades) / len(Grades)
            passing_percentage = (len(passed) / len(Grades)) * 100
            print(f"The average grade is: {average:.2f}")
            print(f"The passing percentage is: {passing_percentage:.2f}%")
            print(f"The number of student who passed is: {len(passed)}")
            print(f"Grades: {Grades}")
    else:
        print("No inputted grades")
        