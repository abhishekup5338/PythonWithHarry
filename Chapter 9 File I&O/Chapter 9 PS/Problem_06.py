
with open("log.html") as f:
    content = f.read()

if("python" in content):
    print("The word python is present in content")

else:
    print("Word not found")