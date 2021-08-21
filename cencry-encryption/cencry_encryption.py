from sys import stdin



#Initial part for getting the standard input
def get_input(line=stdin):
	array = []
	if line != stdin:
		line = line.split("\n")
	for l in line:
		array.append(l)
	return array



if __name__ == '__main__':
	pass
