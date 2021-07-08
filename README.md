# Caesar_Cipher.py
# Created a Caesar Cipher Encryption in Python
# Author: Anthony Constant (AC)


# Notes

 In cryptography, a Caesar cipher is one of the most simplest and mostly wide known techniques.  

Encryption formula 
En(x) = (x + n) mod 26 

Decryption formula 
Dn(x) = (x - n) mod 26

we use mod 26 because there are 26 letters in the alphabet.
in this instance x is our plaintext message respectively.
in this instance n is our key.

# How does it work? 

It is a type of substitution cipher in which each letter in the alphabet is replaced by a letter some fixed number of positions (indexes) down the alphabet. 

For example, with a right shift of 2, C would replace A, D would become B and so on... The method is named after Julius Caesar, who used it in his private correspondence. 

for instance, here is a Caesar cipher using right rotation of 2 spaces below. 

Plain:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Cipher: C D E F G H I J K L M N O P Q R S T U V W X Y Z A B

Test case: 
 
Plaintext: Hello

Ciphertext: jgnnq

Now the message is encrypted!🔐 

# REFERENCES 

## https://en.wikipedia.org/wiki/Caesar_cipher
