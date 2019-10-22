word = input(" : ")
dec_word = []
numbers = ""

for a in word:
    if a.isdigit():
        numbers+=a
    else:
        z = ord(a)+1
        dec_word.append(chr(z))

print(''.join(dec_word),end='')

if numbers.isdigit():
    print(int(numbers) + 1)
