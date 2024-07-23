a = {} #Empty dictionary
marks = {

     "Abhi" : 100,
     "Akhilesh" : 35,
     "Aji" : 23,
     0: "Aniket"
}

print(marks.items())  #Give key:value pairs in tuple form
# print(marks.keys())
# print(marks.values())
marks.update({"Abhi": 99,"Amit":90}) #It will update current dict because it is mutable.
print(marks)