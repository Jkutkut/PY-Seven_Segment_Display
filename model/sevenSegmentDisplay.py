# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sevenSegmentDisplay.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/01 23:11:13 by jre-gonz          #+#    #+#              #
#    Updated: 2022/06/01 23:11:14 by jre-gonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SevenSegmentDisplay:
	'''Class with the logic need to parse a number to a seven segments display'''

	OFF = 16

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

	def __init__(self, v:int=None) -> None:
		self.segments = {}
		self.update(v)

	def update(self, v:int) -> None:
		'''Update the display with the given value. If invalid, the display is cleared'''
		if not (type(v) is int) or v < 0 or v > SevenSegmentDisplay.OFF:
			v = self.OFF
		self.v = v
		for i in range(7):
			self.segments[chr(i + ord("A"))] = self.itoDisplay[v][i]

	def clear(self) -> None:
		'''Clears the display'''
		self.update(SevenSegmentDisplay.OFF)

	def getSegments(self) -> list:
		'''Returns a list with the states of the seven segments display'''
		return self.itoDisplay[self.v]

	def __str__(self):
		return f" {self.getS('A')} \n{self.getS('F')}  {self.getS('B')}\n {self.getS('G')} \n{self.getS('E')}  {self.getS('C')}\n {self.getS('D')} "

	def get(self, key:str) -> bool:
		'''Returns the state of the segment with the given key.'''
		return self.segments[key]

	def getS(self, key:str) -> str:
		'''Returns the state of the segment with the given key as a string.'''
		if key in ["A", "G", "D"]:
			return "──" if self.get(key) else "  "
		else:
			return "│" if self.get(key) else " "