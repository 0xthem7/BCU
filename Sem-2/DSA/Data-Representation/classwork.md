4 bits representation

2^n - 2^4 = 16

| Base 10 | Sign - Magnitude | 1's complement | 2's complement |
|---------|------------------|----------------|----------------|
| +0      | 0000             | 0000           | 0000           |
| +1      | 0001             | 0001           | 0001           |
| +2      | 0010             | 0010           | 0010           | 
| +3      | 0011             | 0011           | 0011           |
| +4      | 0100             | 0100           | 0100           | 
| +5      | 0101             | 0101           | 0101           |
| +6      | 0110             | 0110           | 0110           | 
| +7      | 0111             | 0111           | 0111           | 
| -0      | 1000             | 1111           | *              |
| -1      | 1001             | 1110           | 1111           | 
| -2      | 1010             | 1101           | 1110           | 
| -3      | 1011             | 1100           | 1101           | 
| -4      | 1100             | 1011           | 1100           | 
| -5      | 1101             | 1010           | 1011           |
| -6      | 1110             | 1001           | 1010           | 
| -7      | 1111             | 1000           | 1001           |
| -8      |  *               |  *             | 1000           |

### Question
**1. Convert decimal to binary:** 
* a. 23
* Represent in binary number 
* 2^4 + 2^3 + 2^2 + 2^1 + 2^0
*  16 +  8  +  4  +  2  +  1
*  1  +  0  +  1  +  1  +  1
i.e 16 + 4 + 2 + 1 = 23 = 10111

