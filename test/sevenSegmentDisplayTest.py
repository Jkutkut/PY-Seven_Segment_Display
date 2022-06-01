# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sevenSegmentDisplayTest.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/01 23:11:03 by jre-gonz          #+#    #+#              #
#    Updated: 2022/06/01 23:35:38 by jre-gonz         ###   ########.fr        #
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


if __name__ == "__main__":
	printAll()

	changeDigit()

	getValues()

	getSegment()

	print("End of test")