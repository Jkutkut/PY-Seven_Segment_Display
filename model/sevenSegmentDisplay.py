# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sevenSegmentDisplay.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/01 23:11:13 by jre-gonz          #+#    #+#              #
#    Updated: 2022/06/02 14:43:21 by jre-gonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Union

class SevenSegmentDisplay:
	'''Class with the logic need to parse a number to a seven segments display'''

	OFF = 16

	SEGMENTS = 7

	itoDisplay = [
		[True, True, True, True, True, True, False], # 0
		[False, True, True, False, False, False, False], # 1
		[True, True, False, True, True, False, True], # 2
		[True, True, True, True, False, False, True], # 3
		[False, True, True, False, False, True, True], # 4
		[True, False, True, True, False, True, True], # 5
		[True, False, True, True, True, True, True], # 6
		[True, True, True, False, False, False, False], # 7
		[True, True, True, True, True, True, True], # 8
		[True, True, True, True, False, True, True], # 9
		[True, True, True, False, True, True, True], # A
		[False, False, True, True, True, True, True], # B
		[True, False, False, True, True, True, False], # C
		[False, True, True, True, True, False, True], # D
		[True, False, False, True, True, True, True], # E
		[True, False, False, False, True, True, True], # F
		[False, False, False, False, False, False, False] # EMPTY
	]

	def __init__(self, v: Union[int,str]) -> None:
		self.update(v)

	def update(self, v: Union[int,str]) -> None:
		'''Update the display with the given value. If invalid, the display is cleared'''
		self.v = SevenSegmentDisplay.OFF
		if type(v) == int:
			if v >= 0 and v < SevenSegmentDisplay.OFF:
				self.v = v
		elif type(v) == str and len(v) == 1:
			v = v.upper()
			if v.isdigit():
				self.v = int(v)
			elif (ord(v) >= ord("A") and ord(v) <= ord("F")):
				self.v = ord(v) - ord("A") + 10

	def clear(self) -> None:
		'''Clears the display'''
		self.update(SevenSegmentDisplay.OFF)

	def getSegments(self) -> list:
		'''Returns a list with the states of the seven segments display'''
		return self.itoDisplay[self.v]

	def __str__(self):
		return f" {self.getS('A')} \n{self.getS('F')}  {self.getS('B')}\n {self.getS('G')} \n{self.getS('E')}  {self.getS('C')}\n {self.getS('D')} "

	def get(self, key: Union[int,str]) -> bool:
		'''Returns the state of the segment with the given key/index.'''
		if type(key) == int and (key >= 0 and key < self.SEGMENTS):
			return self.itoDisplay[self.v][key]
		elif type(key) == str and len(key) == 1:
			key = key.upper()
			if key.isdigit():
				return self.get(int(key))
			elif (ord(key) >= ord("A") and ord(key) <= ord("G")):
				return self.get(ord(key) - ord("A"))
		return False # Invalid key
		

	def getS(self, key:str) -> str:
		'''Returns the state of the segment with the given key as a string.'''
		if key in ["A", "G", "D"]:
			return "──" if self.get(key) else "  "
		else:
			return "│" if self.get(key) else " "