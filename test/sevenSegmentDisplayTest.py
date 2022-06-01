# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sevenSegmentDisplayTest.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/01 23:11:03 by jre-gonz          #+#    #+#              #
#    Updated: 2022/06/01 23:11:07 by jre-gonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('.')

from model.sevenSegmentDisplay import SevenSegmentDisplay

if __name__ == "__main__":
	for i in range(0, 16 + 1):
		d = SevenSegmentDisplay(i)
		print("--------------")
		print(d)
		print("--------------")
	

	digito = SevenSegmentDisplay("fsaf")
	print("9")
	print(digito)
	print("9")
	digito.clear()
	print("9")
	print(digito)
	print("9")
	digito.update(2)
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

	digito2 = SevenSegmentDisplay(SevenSegmentDisplay.OFF)
	print("off")
	print(digito2)
	print("off")
	print(digito2.getStates())