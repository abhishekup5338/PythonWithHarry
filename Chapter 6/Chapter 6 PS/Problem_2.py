
marks1 = int(input("Enter student marks1 :"))
marks2 = int(input("Enter student marks2 :"))
marks3 = int(input("Enter student marks3 :"))

total_percentage = (100*(marks1 + marks2 + marks3))/300
if(total_percentage>40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed", total_percentage)
else:
    print("You are failed, Try after one year", total_percentage)