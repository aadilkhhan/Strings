letter = ''' Dear <|Name|>
You are selected !
<|Date|>'''

a = input("Enter name : ")
b = input("Enter Date : ")

letter = letter.replace("<|Name|>", a)
letter = letter.replace("<|Date|>" , b)

print(letter)