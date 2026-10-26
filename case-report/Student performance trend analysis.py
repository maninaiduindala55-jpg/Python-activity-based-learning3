n = int(input("Enter number of subjects: "))

if n <= 0:
    print("Enter at least one subject")

else:
    total1 = 0
    total2 = 0
    subjects = []

    for i in range(n):
        name = input("Enter subject name: ")
        marks1 = int(input("Enter Assessment 1 marks: "))
        marks2 = int(input("Enter Assessment 2 marks: "))

        if marks1 < 0 or marks1 > 100 or marks2 < 0 or marks2 > 100:
            print("Invalid marks")
            break

        difference = marks2 - marks1

        total1 += marks1
        total2 += marks2

        subjects.append([name, marks2, difference])

        print("Change in", name, ":", difference)

    else:
        weakest = subjects[0]

        for subject in subjects:
            if subject[1] < weakest[1]:
                weakest = subject

        print("Assessment 1 total:", total1)
        print("Assessment 2 total:", total2)

        if total2 > total1:
            print("Overall performance improved")
        elif total2 < total1:
            print("Overall performance declined")
        else:
            print("Overall performance unchanged")

        print("Lowest-scoring subject:", weakest[0])