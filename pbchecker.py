# Program that reads the lotto powerball numbers and compares your numbers

# Handle errors, date entered with no drawing, numbers entered in wrong.
# Add comparison of numbers matched to a win.


import urllib2  #the lib that handles the url stuff
import re

# Get the date of the drawing and return the numbers
date = raw_input("Enter date in this format ##/##/#### - ")
data = urllib2.urlopen("http://www.powerball.com/powerball/winnums-text.txt")
for line in data: #files are iterable
	if line.startswith(date):
		today_lotto = line
		today_lotto = today_lotto[:-5]
		print " "
		print "Draw Date   WB1 WB2 WB3 WB4 WB5 PB"
    		print today_lotto

expr = re.compile('\d{2}/\d{2}/\d{4}')
newline = re.sub(expr, '', today_lotto)  # replace all dates with ''
mynums = " "

while (mynums != "exit"):
	mynums = raw_input("Enter your numbers(type exit if done): ")
	if mynums == "exit":
		break
	matches = 0
	for n in mynums.split():
		for i in newline.split():
			if int(i) == int(n):
				matches = matches + 1
	if matches == 6:
		print "YOU WON THE LOTTERY!!!"
	else:	
		print "Total Matches = ", matches	
	


