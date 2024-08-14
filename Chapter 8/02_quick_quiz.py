
def goodday():
    name = input("Enter a name : ")
    print(f"Good Day {name}")

goodday()

def goodday(name):
    print("Good Day" + name)

goodday("Abhishek")


def goodday(name, ending):
    print("Good Day, " + name + ending)
    print("Good Day, " + name)
    print(ending)
goodday("Abhishek", "How are you")


