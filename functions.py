def equeal_elements(arr):
    for a in range(len(arr)):
        for el in range(a+1, len(arr)):
            if arr[a] == arr[el]:
                print(arr[a])


# def crypter(word):
#     dec_word = []
#     numbers = ""
#
#     for a in word:
#         if a.isdigit():
#             numbers+=a
#         else:
#             z = ord(a)+1
#             dec_word.append(chr(z))
#
#     print(''.join(dec_word),end='')
#
#     if numbers.isdigit():
#         print(int(numbers) + 1)
#
# def decrypter(word):
#     dec_word = []
#     numbers = ""
#
#     for a in word:
#         if a.isdigit():
#             numbers+=a
#         else:
#             z = ord(a)-1
#             dec_word.append(chr(z))
#
#     print(''.join(dec_word),end='')
#
#     if numbers.isdigit():
#         print(int(numbers) + 1)
