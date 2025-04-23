#### Kevin Rodriguez
#### Network Security Project-Option 2 Symmetric Encryption/Decryption
#### Part 1: Encryption/Decryption using Polyalphabetic Ciphers
#### Part 2: Encryption/Decryption using Rail Fence Cipher
#### CSCI 4400-D01 Network Security
#### Dr. Yi Gu

# Description

My project completes both part 1 and 2, displays all plaintext, ciphertext, and decrypted ciphertext, and writes to a file. In main opening the file is hardcoded into read mode, prints the original plaintext and passed it into both part 1 and 2 functions. 

## How to run
Depending on operating system, use command line `python3 termProj.py` or `python termProj.py` 

## Part 1:
I created two functions called shiftCipher and fixedCipher for the polyalphabetic cipher. I then created a cycle pattern of ciphers from the given pattern. 

### Encryption:
The shiftCipher function accepts an integer value as a parameter and creates a shiftedAlphabet string using that value. The plain and shift alphabets are zipped into a tuple to create and return the shifted dictionary.The fixedCipher is a hardcoded shifted alphabet zipped into a tuple. The plaintext and cyclePattern are passed to the encryptPoly function for encryption. An empty ciphertext list and a variable for the cycleLength is created. A for loop is used to evaluate it the plaintext is a letter or whitespace. If it is a whitespace is it simply appended to the ciphertext list. If it is a letter we use the index of the plaintext mod cyclelength to decide which cipher is used. The original message is printed again along with the new ciphertext. The ciphertext is written to a new file.

### Decryption:
The dictionaries from the encryption process is used as a parameter to the unshift functions. It swaps the letters to be used for the key.The same process is used for decryption algorithm using the new decrypted order and dictionaries. The decrypted plaintext is written to a file.

## Part 2:
The user is prompted for a railfence depth 'n'. It is converted into an integer and passed along with the plaintext to the encrypt function. I tried to display the rails with appropriate spacing but could not achieve this. It simple prints the row number and the string associated with it. Starting at the second row a white space is added to the front and incremented per row. 

### Encryption:
Minor bound check is performed if the depth is LT 2 it is return as is. A list of 'n' empty strings for the rails, row, and directions are initilaized. A zigzag approach is used to "climb up and down" the rails and bounce back when the top or bottom is reached. It adds the letters to each rail and the ciphertext is joined and returned. The plaintext and ciphertext are printed. The ciphertext is written to a new file. **Note: Spaces were not removed from the plaintext which results in spaces in the ciphertext**

### Decryption
The decrpt function first determines how long each rail is and slices the ciphertext into segments for each of those rails. Similarly to the encrypt function the rails are climbed up and down bouncing when the top and bottom are reached and the letters are appeneded into plaintext and returned. The decrypted plaintext is written to a new file. 

