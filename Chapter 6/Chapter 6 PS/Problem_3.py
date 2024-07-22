
p1 = "Make lots of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter you comment : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("******")

else:
    print(message)