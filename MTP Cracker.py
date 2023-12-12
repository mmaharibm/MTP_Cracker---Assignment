import binascii

def isSpace(lines, chrCurrent, col):     #This function  xors characters of two ciphertexts at the same column if the result is an alphabet or zero it returns true for space
    for line in lines:                   #becasue you get zero when 2 spaces are xored and an alphabet changes cases when xored with a space, in other cases you get a control character
        result = line[col] ^ chrCurrent  
        if not (chr(result).isalpha() or result == 0): return False 
    return True


space=ord(' ')

try:
    file = open("ciphertexts.txt") # file contains the ciphertexts
    ciphertexts = [binascii.unhexlify(line.rstrip()) for line in file] # stores binary string for each ciphertext in an array 
except Exception:
    print("Cannot Open File")

file.close()
texts = [bytearray(b'?' * len(line)) for line in ciphertexts]  #This array will store plaintext. It is filled with ? for each character of each ciphertext 

lengthMax = max(len(line) for line in ciphertexts)
for col in range(lengthMax):        #This goes through each charcter
    cipherNext = [line for line in ciphertexts if len(line) > col] # contains ciphertext to be deciphered
    for cipher in cipherNext:   # for one ciphertext from the array
        if isSpace(cipherNext, cipher[col], col):
            i = 0
            for textRow in range(len(texts)): # each array item is considered one row containing one message
                if len(texts[textRow]) !=0 and col < len(texts[textRow]):  
                    result = cipher[col] ^ cipherNext[i][col]  #character of chosen ciphertext is xored with character of ciphertext at i in the same column
                    if result == 0:
                        texts[textRow][col] = space  # if result is zero then a space is xored with space so the plain text array stores space at the column 
                    elif chr(result).isupper():
                        texts[textRow][col] = ord(chr(result).lower()) # if result is an upper case letter, it is changed to lower case and stored at the column
                    elif chr(result).islower():
                        texts[textRow][col] = ord(chr(result).upper()) # if result is a lower case letter, it is changed to upper case and stored at the column
                    i+=1  #i is incremented by 1 to move to the next ciphertext
            break

print("\n".join(line.decode('ascii') for line in texts))  #prints all the messages in plain text
