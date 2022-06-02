# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    displayTest.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/02 16:05:06 by jre-gonz          #+#    #+#              #
#    Updated: 2022/06/02 16:24:44 by jre-gonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('.')

from model.sevenSegmentDisplay import SevenSegmentDisplay as SegmentDisplay
from model.display import Display

if __name__ == "__main__":
	d = Display()
	d.update("0000000")
	print(d)


	d = Display("1234567")
	print(d)
	d.update("123R232")
	print(d)