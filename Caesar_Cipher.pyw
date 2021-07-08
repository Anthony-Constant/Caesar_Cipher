# Caesar_Cipher.py
# Created a Caesar Cipher Encryption in Python
# Author: Anthony Constant (AC)

################################# SOME NOTES #########################################

## In cryptography, a Caesar cipher is one of the most simplest and mostly wide known techniques.  

## Encryption formula 
## En(x) = (x + n) mod 26 

## Decryption formula 
## Dn(x) = (x - n) mod 26

## we use mod 26 because there are 26 letters in the alphabet.
## in this instance x is our plaintext message respectively.
## in this instance n is our key.

######################## HOW DOES IT WORK ##############################################

## It is a type of substituion cipher in which each letter in the alphabet is replaced by a letter some fixed number of positions (indexes) down the alphabet. 

## For example, with a right shift of 2, C would replace A, D would become B and so on... The method is named after Julius Caesar, who used it in his private corresponence. 

## for instance, here is a Caesar cipher using right rotation of 2 spaces below. 

## Plain:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

## Cipher: C D E F G H I J K L M N O P Q R S T U V W X Y Z A B

## USE CASE: 

## Plaintext: Hello

##Ciphertext: jgnnq

## Now the message is encrypted!

############################# REFERENCES ###############################################

## https://en.wikipedia.org/wiki/Caesar_cipher

########################################################################################
############################ START PROJECT HERE #######################################
############################################################################################

## create a function for encryption so we can implement a Ceasar Cipher 
## passing string as the parameter and the key (shift)
def encryption(string,shift):


    cipher = '' ## create an empty string to place the ciphertext in this variable 

    for char in string: ## here we must extract each character from the string 
        if char == ' ':## if the string character is uppercase
            ## first check the order of character for example: A = 1 B = 2 and so on... Each letter has its corresponding index number
            ## Get the shift variable from the user which is provided to us. 
            ## we substract -65 because the UpperCase alphabet starts from 65. Has 65 characters/Indexes
            ## then add mod 26 and add it back to 65 due to the ASCII value table starting from 65
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher+char((ord(char)+shift-65)%26+65)
        else:
            cipher = cipher+chr((ord(char)+shift-97)%26+97)
    return cipher

## GET USER INPUT
user_input = input("Enter message: ")
s = int(input("Enter amount of shifts: "))

print("The plaintext is: ", user_input)
print("The encrypted message is: ",encryption(user_input,s))



