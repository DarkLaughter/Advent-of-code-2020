#part 1

rr = []
with open('day1.txt') as input:
    numbers = input.readlines()
    for num in numbers:
        rr.append(int(num))

def reportRepair(l, sum):
    for i in range(len(rr) - 1):
        first = rr[i]
        for j in range(i+1, len(rr)):
            second = rr[j]
            if first + second == sum:
                product = first * second
    return product

print(reportRepair(rr, 2020))


#Part 2

def reportRepair(l, sum):
    for i in range(len(rr) - 2):
        first = rr[i]
        for j in range(i+1, len(rr) - 1):
            second = rr[j]
            for k in range(j +1, len(rr)):
                third = rr[k]
                if first + second + third == sum:
                    product = first * second * third
    return product

print(reportRepair(rr, 2020))