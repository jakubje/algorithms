alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = "IAOQ UQ G FQOQB FWKI QKWVIM GKJ G LVFPBVU WK CMAPM EW RFGPQ AE GKJ A NMGFF UWOQ EMQ CWBFJ"
ciphertext = ciphertext.replace(' ', '')
counter = [0]*26

for char in ciphertext:

    print(f'Before: Char: {char}')
    num = alphabet.find(char)
    counter[num] += 1

    print(f'After: Num: {num}, CounterNum: {counter[num]}, Counter: {counter}')

print(counter) 
 