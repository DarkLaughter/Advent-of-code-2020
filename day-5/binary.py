import math

def find_midpoint(num):
    return math.ceil(num/2)

def row_seat_decoder(list):
    seat_dict = {}
    for item in list:
        rows = [*range(1,128)]
        seats = [*range(1,8)]
        for char in item[0:-3]:
            if char == 'F':
                rows = rows[:find_midpoint(len(rows))]
            elif char == 'B':
                rows = rows[find_midpoint(len(rows)):]
        for char in item[-3:]:
            if char == 'L':
                seats = seats[:find_midpoint(len(seats))]
            elif char == 'R':
                if len(seats) == 1:
                    break
                seats = seats[find_midpoint(len(seats)):]
        seat_dict[rows[0]] = seats[0]
    return seat_dict 

def highest_id(lst):
    current_tickets = row_seat_decoder(lst)
    highest_id = 0
    for i in current_tickets:
        id = i * 8 + current_tickets[i]
        if highest_id < id:
            highest_id = id
    return highest_id

with open('input.txt') as input:
    seat_assignments = input.read().rstrip()
    seat_lst = seat_assignments.split("\n")

print(highest_id(seat_lst))