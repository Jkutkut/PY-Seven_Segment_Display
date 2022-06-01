class SevenDigitsDisplay:
	def __init__(self):
		self.digits = {
			"A": False,
			"B": False,
			"C": False,
			"D": False,
			"E": False,
			"F": False,
			"G": False
		}

		self.digits["A"] = True
		self.digits["F"] = True
		self.digits["G"] = True
		self.digits["C"] = True
		self.digits["D"] = True

	def __str__(self):
		return f" {self.get('A')} \n{self.get('F')}  {self.get('B')}\n {self.get('G')} \n{self.get('E')}  {self.get('C')}\n {self.get('D')} "

	def get(self, key):
		if key in ["A", "G", "D"]:
			return SevenDigitsDisplay.hori(self.digits[key])
		else:
			return SevenDigitsDisplay.verti(self.digits[key])

	@staticmethod
	def hori(val):
		return "──" if val else "  "
	
	@staticmethod
	def verti(val):
		return "│" if val else " "



if __name__ == "__main__":
	d = SevenDigitsDisplay()
	print(d)