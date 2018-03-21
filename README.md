# Python-Programing
Some simple codes using Python 3 

# intellegent parking system
Gui For intelligent parking system Using Tkinter module
this Gui would show no. of empty spots and filled spots along with current Time and date.
Data would be feeded by a program by taking visual data through cctv camera fitted at parking.

# Encrypt your message
 encryption is the process of encoding a message or information in such a way that only authorized parties can access it and those who are not authorized cannot.
Here an encryption technique is used to encrypt the message, named "Polybius cipher".
Following are some Features of this technique -:

i) this consist of a 5X5 grid which contains 25 english alphabets out of 26 (here Z is excluded because its chance of occurence is very less in any message)
ii) 25 letters are filled in grid in a specific manner which depends on a key given by encoder.(who is sending message)
iii) after filling grid, every letter in message can be specified by its index value inside grid.
iv) And here is your encrypted message. specifying each letter with its co-ordinate value gives an encrypted message.

Lets take an example :
   lets after giving key grid has been generated (Here encoder have not to be worried about grid formation, it would be automatically        done after giving key)
    
 assume grid is :
     
                                                                                                1  2  3  4  5
                                                                                             1  a  b  c  d  e
                                                                                             2  f  g  h  i  j
                                                                                             3  k  l  m  n  o
                                                                                             4  p  q  r  s  t
                                                                                             5  u  v  w  x  y
    
  Consider your message is : Hello sam
   index for 'H' is 2,3
   index for 'e' is 1,5
   index for 'l' is 3,2
   index for 'o' is 3,5
   index for 's' is 4,4
   index for 'a' is 1,1
   index for 'm' is 3,3
   
 so encrypted message is: 23 15 32 35 44 11 33
 
similarly for decryption you have to provide key and index values, and code would be decrypt automatically.
if you are more curious about how its happening, then you can visit this link- https://www.dcode.fr/polybius-cipher
