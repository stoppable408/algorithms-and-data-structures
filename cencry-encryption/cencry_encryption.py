from sys import stdin

vowel_string = "aeiouaeiouaeiouaeiouaeiou"
consonant_string = "bcdfghjklmnpqrstvwxyzbcdfghjklmnpqrstvwxyz"


def encrypt(input):
	return input


#Initial part for getting the standard input
def get_input(line=stdin):
	array = []
	if line != stdin:
		line = line.split("\n")
	for l in line:
		array.append(l)
	return array



if __name__ == '__main__':
	input = get_input("2\nbaax\naaa")
	print(input)
