#Repalce 'name' and 'date' with varchar 
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Abhishek").replace("<|Date|>", "12th July 2024"))