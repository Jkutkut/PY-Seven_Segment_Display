# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/02 15:09:22 by jre-gonz          #+#    #+#              #
#    Updated: 2022/06/02 16:27:50 by jre-gonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# Module import logic
if 'model.sevenSegmentDisplay' not in sys.modules:
	from sevenSegmentDisplay import SevenSegmentDisplay as SegmentDisplay
else:
	from model.sevenSegmentDisplay import SevenSegmentDisplay as SegmentDisplay

class Display:
	
	SIZE = 7

	OFF = "".join([" " for i in range(7)])

	def __init__(self, value=None):
		self.value = Display.OFF
		self.segmentDisplays = [SegmentDisplay(SegmentDisplay.OFF) for i in range(self.SIZE)]
		
		if value != None:
			self.update(value)

	def update(self, value: str = None):
		self.value = Display.OFF

		if type(value) == str and len(value) == Display.SIZE:
			value = value.upper()
			if all([d.isdigit() or (ord(d) >= ord("A") and ord(d) <= ord("F")) for d in value]):
				self.value = value

		for i in range(self.SIZE):
			self.segmentDisplays[i].update(self.value[i])

	def __str__(self):
		segmentStr = [d.__str__().split("\n") for d in self.segmentDisplays]
		string = ""
		for i in range(5):
			for p in segmentStr:
				string += f"{p[i]} "
			string += "\n"
		return string
