class SevenDigitsDisplay:

	itoSD2 = [
		[True, True, True, True, True, True, False] # 0
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

		if v == None:
			return
		for i in range(7):
			# print(chr(i + ord("A")) + str(self.itoSD2[v][i]))
			self.digits[chr(i + ord("A"))] = self.itoSD2[v][i]

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
	d = SevenDigitsDisplay(0)
	print(d)