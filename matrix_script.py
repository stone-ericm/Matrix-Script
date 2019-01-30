n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in xrange(n):
    matrix_t = str(raw_input())
    matrix.append(matrix_t)

regex_char = r"[A-Z, a-z, 0-9]"
regex_nonchar = r"([^A-Z, a-z, 0-9]+|\s+)*"
regex_nonchar_end = r"([^A-Z, a-z, 0-9]+|\s+)*$"

class MatrixMatch:
    def __init__(self):
        self.output = ""
        self.buff = ""

    def matrix_match(self, x):
        self.output += self.buff
        print(x)
        self.output += x
        return ""

answer = MatrixMatch()

import re

i = 0
matrix_unwrap = ""

while i < m:
    for each in matrix:
		matrix_unwrap += each[i]
	i += 1

i = 0	

while matrix_unwrap[i].isalnum():
	while i < len(matrix_unwrap):
		while not bool(re.match(regex_nonchar_end, matrix_unwrap[i:])):
			answer.output += matrix_unwrap[i]
			i += 1
		matrix_unwrap1 = matrix_unwrap.replace(re.match(regex_nonchar, matrix_unwrap[i:]).group(), " ", 1)
		matrix_unwrap = matrix_unwrap1
		answer.output += matrix_unwrap[i]
		i += 1
	answer.output += matrix_unwrap[i:]
	break

		
print (answer.output)


# while i < m:
    # for each in matrix:
        # e = each[i]
        # t = bool(re.match(regex_nonchar, e))
       # print(t)
        # answer.buff = {False: answer.matrix_match(e)}.get(t, " ")
    # i += 1

# print answer.output













### We're going to unravel the matrix and use ([^A-Z, a-z, 0-9]+|\s+)* and ([^A-Z, a-z, 0-9]+|\s+)*$ to do replacements



# \w*\S
