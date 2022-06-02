# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sevenSegmentDisplayTest.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/01 23:11:03 by jre-gonz          #+#    #+#              #
#    Updated: 2022/06/02 14:52:14 by jre-gonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('.')

from model.sevenSegmentDisplay import SevenSegmentDisplay

def printAll():
	print("Print all")
	for i in range(0, 16 + 1):
		d = SevenSegmentDisplay(i)
		print("--------------")
		print(d)
		print("--------------")

def changeDigit():
	print("Change digit")
	d = SevenSegmentDisplay(0)
	print("0--------------0")
	print(d)
	print("0--------------0")

	d.update(1)
	print("1--------------1")
	print(d)
	print("1--------------1")

	d.clear()
	print("--------------")
	print(d)
	print("--------------")

	d.update("A")
	print("A--------------A")
	print(d)
	print("A--------------A")

def getValues():
	print("Get values")
	d = SevenSegmentDisplay(9)

	print("Get values/segments")
	print("9--------------9")
	print(d.getSegments(), sep=", ")
	print("9--------------9")

def getSegment():
	print("Get segment")
	d = SevenSegmentDisplay(9)

	print("Get segment A")
	print("9--------------9")
	print(d.get("A"))
	print("9--------------9")

# Extra functionalities
def initAsString():
	displays = [
		SevenSegmentDisplay('2'),
		SevenSegmentDisplay("3"),
		SevenSegmentDisplay('A')
	]

	print("Displays made with string")
	for d in displays:
		print("----------")
		print(d)
		print("----------")

def getSegmentAsInt():
	print("Get segment as int")
	d = SevenSegmentDisplay(9)

	print("Get segment C")
	print("9--------------9")
	print(d.get(2))
	print("9--------------9")

	print("Get first segment")
	print("9--------------9")
	print(d.get(0))
	print("9--------------9")

	print("Get last segment")
	print("9--------------9")
	print(d.get(SevenSegmentDisplay.SEGMENTS - 1))
	print("9--------------9")


# Fail tests


if __name__ == "__main__":
	printAll()

	changeDigit()

	getValues()

	getSegment()

	# String

	initAsString()

	getSegmentAsInt()

	print("End of test")