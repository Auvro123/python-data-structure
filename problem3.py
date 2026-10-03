dictionary={"auvro": 100, "laltu": 90, "montu": 92}
result= input("Enter the name of student: ")
if result in dictionary:
    print("The marks of", result, "is", dictionary[result])
