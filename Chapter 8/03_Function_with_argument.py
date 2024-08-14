

def goodday(name):
    print("Good Day" + name)

goodday("Abhishek")


def goodday(name, ending):
    print("Good Day, " + name + ending)
    print("Good Day, " + name)
    print(ending)
goodday("Abhishek", "How are you")

#return function


def goodday(name, ending):
    print("Good Day, " + name + ending)
    print("Good Day, " + name)
    print(ending)
    return "done"
a = goodday("Abhishek", "How are you")
print(a)


