
target_list = [31, 41, 59, 85, 66]
char = 66

def checker(target_list, char):
    for element in target_list:
        if(element == char):
            return True
    return False

result = checker(target_list, char)
print(result)