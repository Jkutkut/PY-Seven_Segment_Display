class SevenDigitsDisplay:

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

	def __init__(self, v=None):
		self.digits = {
			"A": False,
			"B": False,
			"C": False,
			"D": False,
			"E": False,
			"F": False,
			"G": False
		}

		if v == None or v >= len(self.itoDisplay):
			v = self.OFF
		
		self.v = v
		for i in range(7):
			self.digits[chr(i + ord("A"))] = self.itoDisplay[v][i]

	def getStates(self):
		return self.itoDisplay[self.v]

	def __str__(self):
		return f" {self.getS('A')} \n{self.getS('F')}  {self.getS('B')}\n {self.getS('G')} \n{self.getS('E')}  {self.getS('C')}\n {self.getS('D')} "

	def get(self, key):
		return self.digits[key]

	def getS(self, key):
		if key in ["A", "G", "D"]:
			return "──" if self.get(key) else "  "
		else:
			return "│" if self.get(key) else " "



if __name__ == "__main__":
	for i in range(0, 16 + 1):
		d = SevenDigitsDisplay(i)
		print("--------------")
		print(d)
		print("--------------")
	

	digito = SevenDigitsDisplay(9)
	print("9")
	print(digito)
	print("9")
	print(digito.getStates())

	if digito.get("A") == True:
		## Set LED ON
		pass
	else:
		## Set LED OFF
		pass

	digito2 = SevenDigitsDisplay(SevenDigitsDisplay.OFF)
	print("off")
	print(digito2)
	print("off")
	print(digito2.getStates())