# MTP_Cracker---Assignment

This was an assignment for a Network Security Class

The code goes through each character till maximum length of the ciphertexts in the array. For each cipher text in the array that is greater in length then the value of col, 
it checks if the chosen character at the position col is a space. If it is a space, it is XORed with the character of another ciphertext at the same position. If the result 
is zero then a space is put into the plaintext array at position col, if it is an upper-case letter, it’s lowercase in put into the plaintext array at position col, and vice versa 
for lower case letters. Then it moves down a row and XORs the character at the same column of the next ciphertext. It repeats this for the 13 messages then increments the column and repeats the whole loop.
