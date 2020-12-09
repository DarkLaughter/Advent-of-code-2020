import math

def find_midpoint(num):
    return math.ceil(num/2)

def row_finder(char, num):
    if char == 'F':
        row_nums = find_midpoint(num)
    elif char == 'B':
        num = find_midpoint(num)

def seat_finder(char, num):
    if char == 'L':
        row_nums = find_midpoint(num)
    elif char == 'B' or char == 'R':
        num = find_midpoint(num)

def highest_seat_num(list):
    for item in list:
        row_info = item[0:-3]
        row_nums = 127
        seat_info = item[-3:]
        seat_nums = 7
        for char in row_info:
            row_finder(char,row_nums)
        for char in seat_info:
            row_finder(char, seat_nums)
        print(row_nums, seat_nums)


with open('input.txt') as input:
    seat_assignments = input.read().rstrip()
    seat_lst = seat_assignments.split("\n")

print(highest_seat_num(seat_lst))