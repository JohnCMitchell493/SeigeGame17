from pygame import *
from rock import *

def main():
	print("===Testing Rock===")
	boulder = rock.Rock()

	print("===Test Movement===")
	boulder.launch(46, 25)
	assert boulder.getcoordinates() == (25.2178890695, 0.49502212441)
main()
