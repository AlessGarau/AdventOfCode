with open('data.txt') as f:
    lines = f.readlines()

sum = 0

for line in lines:
    print("================")
    line_number = []
    line_sum = 0
    for caracter in line:
        if caracter.isdigit():
            line_number.append(caracter)
    if (len(line_number) == 0):
        print(line_number)
        line_sum = int(line_number[0]) * 10 + int(line_number[0])

    else:
        print(line_number)
        line_sum = int(line_number[0]) * 10 + int(line_number[-1])
        print("line sum", line_sum)
    sum += line_sum

print(sum)
