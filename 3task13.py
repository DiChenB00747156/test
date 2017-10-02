
fin = open('words.txt')

def is_abecedarian(word):
    i = 0
    while i < len(word) -1:
        if word[i] > word[i+1]:
            return False
        else:
            i = i + 1
    return True

def number():
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            count = count + 1
    return count

print(number())   
