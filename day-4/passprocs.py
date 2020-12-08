def pass_match_info(lst):
    passport_requirements = ("byr","iyr", "eyr","hgt","hcl","ecl", "pid")
    indivial_can_board = 0
    for passenger in lst:
        boarding_requirements = 0
        for i in passport_requirements:
            if i in passenger:
                boarding_requirements+= 1
        
        if boarding_requirements == len(passport_requirements):
            indivial_can_board += 1
    return indivial_can_board


with open('input.txt') as input:
    passengers = input.read().rstrip()
    current_passengers = passengers.split('\n\n')

print(pass_match_info(current_passengers))