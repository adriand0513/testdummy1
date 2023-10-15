def main():
	s = input("What time is it? ")
	time = convert(s)
	if time >= 7 and time <= 8:
		print("breakfast time")
	if time >= 12 and time <= 13:
		print("lunch time")
	if time >= 18 and time <= 19:
		print("dinner time")



def convert(time):
	hours, minutes = time.split(":")
	time = time.replace(":", ".")
	new_minutes = float(minutes) / 60
	return float(hours) + new_minutes

if __name__ == "__main__":
	main()
