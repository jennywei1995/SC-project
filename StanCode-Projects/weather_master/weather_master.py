"""
File: weather_master.py
Name: Jenny Wei
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = -100

def main():
	"""
	This program will implement a console program
	computing the average, highest, lowest, cold days among user's inputs.
	"""
	print("StanCode \"Weather Master 4.0\"!")

	new_data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?: '))

	if new_data == EXIT:
		print('No temperatures were entered.')
	else:
		# to find highest temperature
		highest = new_data
		# to find lowest temperature
		lowest = new_data
		#  to count how many times the user input
		times = 1
		# sum of all the input data
		sum_data = new_data
		# to count how many cold days
		cold_day = 0
		if new_data < 16 and new_data != EXIT:
			cold_day += 1

		while True:
			new_data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?: '))
			if new_data != EXIT:
				sum_data += new_data
				sum_data = sum_data
				times += 1
				times = times
				if new_data < 16:
					cold_day += 1
					cold_day = cold_day
				if highest >= new_data > lowest:
					pass
				elif new_data > highest:
					highest = new_data
				else:
					if new_data <= lowest:
						lowest = new_data
			else:
				# when new_data == EXIT
				break

		print('Highest temperature＝ '+str(highest))
		print('Lowest temperature＝ '+str(lowest))
		print('Average= '+str(sum_data/times))
		print(str(cold_day)+' cold day(s).')





###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
