# Data Structure and Algorithms

Data structure - How data is represented 
Algorithm - How data is operated

## Data Structre 
    It is the way of storing data in a computer so that it can be accessed and modified efficiently.

### Binary 
    Computer is two-state (binary) machine.


### Quiz
1. Storing the day of the week ?
-> B. 4 bits
2. Number of people in the world ?
-> D. 16 bits
3. Number of stars in the universe ?
-> Around 80 bits 

### Two's comlement
Process 
1. Convert number to binary
2. Invert all the digits
3. Add 1 to the result 

example : Decimal = -110
1. Binary for +110 = 01101110
2. Inverted = 10010001
3. 10010001 + 1 = 10010010
4. Check 01101110 + 10010010 = 100000000 for 8 bits its 0

### Decimal number representation
For integers we use positive powers where as for decimals we can use negative powers.
2^-1 = 1/2 = 0.5
2^-2 = 1/2^2 = 1/4 = 0.25
3^-2 = 1/3^2 = 1/27 = 0.037

Base 2      Base 10
   0.1  = 0.5
  0.111 = 1*2^-1 + 1*2^-2 + 1*2^-3 = 0.5 + 0.25 + 0.125 = 0.875
 0.10001 = 1*2^-1 + 1*2^-5  = 0.5 + 0.03125 = 0.53125




### Primitive Data types in python
1. Integers 
2. Float 
3. Strings
4. Boolean


### Bits, Bytes and words - Nomenclature
* Nibble - 4 bits (half byte)
* Byte - 8 bits 
* Word - a collection of 4 bytes, or 32 bits 
* Kilobytes (KB) - 1024 bytes
* Megabytes (MB) - 1024 kilobytes
* Gigabytes (GB) - 1024 Megabytes
* Terabytes (TB) - 1024 Gigabytes
* Petabytes (PB) - 1024 Terabytes
* Exabytes  (EB) - 1024 Petabytes  

since kilo is 1000 another nomenclature came to existance 

* Nibble - 4 bits (half a byte)
* Byte - 8 bits 
* Word - 32 bits
* Kilobyte - 1000 bytes 
* Megabyte - 1000 Kilobyte
* Gigabyte - 1000 Megabyte

(Note: windows considers KB - kibibyte etc, so a hard drive claiming to be 1 TB actually displays as 921.32 GB )


## Memory system

Computer program use varaible or data structure to store data in memory

