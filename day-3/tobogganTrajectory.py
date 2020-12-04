with open('day3.txt') as input:
	inp = [line.rstrip() for line in input]

# i = 0
# c = 0
# for x in inp:
# 	l = len(x)
# 	if i >= l:
# 		i -= l
# 	if (x[i] == '#'):
# 		c += 1
# 	i += 3


# print(c)

def count(lst, y, m=0):
    if m != 0:
        m -= 1
    i = m
    c = 0
    for x in inp:
	    l = len(x)
	    if i >= l:
		    i -= l
	    if (x[i] == '#'):
		    c += 1
	    i += 3
    return c

print(count(inp,3))
print(count(inp,1))
print(count(inp,5))
print(count(inp,7))
print(count(inp,1, 2))
print(count(inp,3) ** 4 * count(inp,1, 2))