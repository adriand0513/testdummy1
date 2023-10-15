s = input("Expression: ")

x, y, z = s.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
	result = new_x + new_z
elif y == "-":
	result = new_x - new_z
elif y == "/":
	result = new_x / new_z
elif y == "*":
	result = new_x * new_z
else:
	print("Expression unknown")
	
print(round(result, 1))
