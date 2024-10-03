

with open("log.html") as f:
    lines = f.read()

lineno = 1
for line in lines:
  if("python" in line):
    print(f"The word python is present in content, line no :{line}")
    break
  lineno += 1
else:
    print("Word not found")