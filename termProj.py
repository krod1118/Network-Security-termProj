# Kevin Rodriguez
# CSCI 4400 D01 Dr. Yi Gu
# Network Security Project Option 2
# Symmetric Encryption/Decryption (2 parts)
# Part 1: Encryption/Decryption using Polyalphabetic Cipher
# Part 2: Encryption/Decryption using Rail Fence Cipher
#----------------------
def main():

    print("")
    print("Welcome to the Symmetric Encryption/Decryption Program!\n")

    #filename = input()
    filename = "plaintext.txt"

    #Read the plaintext from the file
    infile = open(filename, 'r')

    plaintext = infile.read()

    print("Main")
    print("----------\n")
    print("Original plaintext: ", plaintext,"\n")

    #call part 1
    print("Calling Part 1")
    print("----------\n")
    
    part1(plaintext)

    #call part 2
    print("Calling Part 2")
    print("----------\n")
    part2(plaintext)

    infile.close()
#-----------------------

#-----------------------
def part1(plaintext):
    '''Part 1: 
    Input: A given text file for plaintext (assume only 26 letters, no special character, numbers, nor punctuations)
    3 substitution ciphers, M1, M2, M3
    M1 - right shift 8 letters
    M2 - fixed mapping
    M3 - left shift 12 letters
    Cycling pattern: 
    n=4: M2, M3, M1, M3; M2, M3, M1, M3; M2, M3, M1, M3; ...
    Output: Encrypted ciphertext and decrypted plaintext
    '''

    #create dictionaries for ciphers
    M1Cipher = shiftCipher(8)
    M2Cipher = fixedCipher()
    M3Cipher = shiftCipher(-12)

    #cycle pattern
    cyclePattern = [M2Cipher, M3Cipher, M1Cipher, M3Cipher]

    print("Welcome to Part 1: Encryption/Decryption using Polyalphabetic Ciphers\n")

    # call encrypt func and assign to cipher text
    print("**Encrypting**\n")
    ciphertext = encryptPoly(plaintext, cyclePattern)

    print("Original plaintext: ", plaintext,"\n")
    print("Ciphertext: ", ciphertext,"\n")

    #write to file
    p1Cipher = open('p1Cipher.txt', 'w')
    p1Cipher.write(ciphertext)
    p1Cipher.close()


    print("**Decrypting**\n")
    #create dictionaries to decrypt
    M1Plain = unshiftCipher(M1Cipher)
    M2Plain = unshiftCipher(M2Cipher)
    M3Plain = unshiftCipher(M3Cipher)

    #cycle pattern
    decryptOrder = [M2Plain, M3Plain, M1Plain, M3Plain]

    #call decrypt func and assign
    decryptedPlainText = decryptPoly(ciphertext, decryptOrder)

    print("Decrypted ciphertext: ", decryptedPlainText, "\n")

    #write to file
    p1Decrypted = open('p1Decrypted.txt', 'w')
    p1Decrypted.write(decryptedPlainText)
    p1Decrypted.close()
 
#----------------------- 

#-----------------------
def shiftCipher(toShift):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # [toShift:] slices from toShift to end
    # [:toShift] slices from beginning to toShift
    # and concatenates to create new shifted alphabet
    shiftedAlphabet = alphabet[toShift:] + alphabet[:toShift]

    # zip plain and shifted alphabets into tuple
    alphaTuple = zip(alphabet, shiftedAlphabet)

    # create dictionary
    cipherDict = {
        plain : cipher
        for plain,cipher in alphaTuple
    }

    return cipherDict
#----------------------

#----------------------
def unshiftCipher(dict):

    ## swaps dictionary letters
    plainDict = {
        cipher : plain
        for plain, cipher in dict.items()
    }

    return plainDict

#----------------------

#----------------------
def fixedCipher():

    #create alphabets and make it lowercase
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    fixedAlphabet= "DKVQFGBXWPESCJHTMYAUOLRIZN".lower()

    #create tuple
    alphaTuple = zip(alphabet, fixedAlphabet)

    #creates cipher dictionary
    cipherDict = {
        plain : cipher
        for plain,cipher in alphaTuple
    }

    return cipherDict
#-----------------------

#-----------------------
def encryptPoly(plaintext, cyclePattern):

    #empty list and cycle length used for mod op
    ciphertext = []
    cycleLength = len(cyclePattern)


    for index, letter in enumerate(plaintext.lower()):
        if letter.isalpha():

            #decide what step of polyalphabetic cipher to use by the index mod cyclelength
            cipher = cyclePattern[index % cycleLength]
            ciphertext.append(cipher[letter])
            index +=1
        else:
            ciphertext.append(letter)
    return "".join(ciphertext)
#-----------------------

#----------------------
def decryptPoly(ciphertext, decryptOrder):

    decrypted = []
    cycleLength = len(decryptOrder)

    for index, letter in enumerate(ciphertext.lower()):
        if letter.isalpha():
            reverseCipher = decryptOrder[index % cycleLength]
            decrypted.append(reverseCipher[letter])
        else:
            decrypted.append(letter)
    
    return "".join(decrypted)
#----------------------

#----------------------
def part2(plaintext):
    
    '''Part 2: 
    Input: A given text file for plaintext
    User input depth of rail fence

    Output:Encrypted ciphertext and decrypted plaintext
    '''
    print("Welcome to Part 2:Encryption/Decryption using Rail Fence Cipher\n")

    #ask user for rail depth and convert to int
    depth = input("Please enter 'n' the depth of the Rail Fence Cipher: ")
    depth = int(depth)
    print("")

    print("**Encrypting**")

    #to display each rail 
    ciphertext, rails = railFenceEncrypt(plaintext, depth)

    print("Original plaintext: ", plaintext, "\n")

    print("Ciphertext: ", ciphertext, "\n")

    #write to file
    p2Cipher = open('p2Cipher.txt', 'w')
    p2Cipher.write(ciphertext)
    p2Cipher.close()

    #print rails and ciphertext
    for i, row in enumerate(rails):
        print(f"Row{i}: {' '* i}{row}")
    print()

    print("**Decrypting**")
    decryptedPlainText = railFenceDecrypt(ciphertext, depth)

    print("Decrypted ciphertext: ", decryptedPlainText, "\n")

    #write to file
    p2Decrypted = open('p2Decrypted.txt', 'w')
    p2Decrypted.write(decryptedPlainText)
    p2Decrypted.close()
#----------------------

#----------------------
def railFenceEncrypt(plaintext, depth):

    if depth < 2:
        return plaintext

    # list of empty strings using depth for each rail
    rails = [""] * depth
    row, direction = 0, 1

    #to climb up and down rails and return when reached
    for letter in plaintext:
        rails[row] += letter
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1
    
    ciphertext = "".join(rails)
    return ciphertext, rails
#----------------------

#----------------------
def railFenceDecrypt(ciphertext, depth):

    if depth < 2:
        return ciphertext
    

    #identify how long each rail is 
    count = [0] * depth
    row, direction = 0, 1
    for _ in ciphertext:
        count[row] += 1
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1

    #slice the ciphertext into segments for each rail
    rail, index = [], 0
    for n in count:
        rail.append(ciphertext[index:index + n ])
        index += n

    #climb up and down rail and append to plaintext, return when top or bottom is reached
    railPtr = [0] * depth
    row, direction = 0, 1
    plaintext = []
    for _ in ciphertext:
        plaintext.append(rail[row][railPtr[row]])
        railPtr[row] += 1
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1
    
    return "".join(plaintext)
#----------------------



if __name__ == "__main__":
    main()

