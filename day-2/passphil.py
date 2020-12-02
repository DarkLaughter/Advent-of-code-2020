# Valid Passwords will have a min and max of occurences of a speficic character, accompanied by the password string
# 3-5 f: fgfff
# min-max 'character': "password string"

parsed_current_pass = []

with open('day2.txt') as input:
    individual_data = input.readlines()
    for line in individual_data:
        individual_pass_list = line.split(' ')
        first_element = individual_pass_list[0].split('-')
        first_num = first_element[0]
        second_num = first_element[1]
        character = individual_pass_list[1][0]
        pass_string = individual_pass_list[2].rstrip()
        parsed_current_pass.append({'first': first_num, 'second': second_num, 'character': character, 'string': str(pass_string)})

#part 1

def meets_philosphy(lst):
    count = 0
    for i in lst:
        char_count = 0
        for char in i['string']:
            if char == i['character']:
                char_count += 1
        if char_count >= int(i['first']) and char_count <= int(i['second']):
            count += 1
    return count
#print(meets_philosphy(parsed_current_pass))

#part2

def updated_philosophy(lst):
    count = 0
    for i in lst:
        pass_string = i['string']
        first_index = int(i['first']) -1
        second_index =  int(i['second']) - 1
        if pass_string[first_index] == i['character'] and pass_string[second_index] != i['character']:
            count += 1
        elif pass_string[first_index] != i['character'] and pass_string[second_index] == i['character']:
            count += 1
    print(count)



# updated_philosophy(parsed_current_pass)