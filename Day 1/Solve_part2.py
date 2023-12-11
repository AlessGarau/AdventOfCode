with open('data.txt') as f:
    data = f.readlines()

sum = 0
list_string_number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                      'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']


def is_find(word_to_find, data):
    find = data.find(word_to_find)
    if find != -1:
        print(word_to_find)
        return True
    else:
        return False


for line in data:
    print("================")
    line_number = []
    line_sum = 0
    for caracter in line:
        if caracter.isdigit():
            line_number.append(caracter)

    for number in list_string_number:
        test = filter(is_find(number, line), list_string_number)

    if (len(line_number) == 0):
        print(line_number)
        line_sum = int(line_number[0]) * 10 + int(line_number[0])

    else:
        print(line_number)
        line_sum = int(line_number[0]) * 10 + int(line_number[-1])
        print("line sum", line_sum)
    sum += line_sum


print(sum)
