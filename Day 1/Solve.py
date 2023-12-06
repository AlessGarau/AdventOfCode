def isNumber(input):
    input_to_int = int(input)
    if  0 <= input_to_int <= 9:
        return True
    else:
        return False
    
def isInt(input):
    
    return
with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    print("================")
    for caracter in line:
        test = isNumber(caracter)
        print(test)
