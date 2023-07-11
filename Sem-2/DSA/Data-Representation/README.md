# Data structure and Algorithm
## BCU university
__Creator Himansu Mahato__

* Data Structure - How data is represented
* Algorithm - How data is operated

Data structure is a way of `organizing` and `storing` data in computer so that it can be accessed and modified efficiently.
* It depends upon Time and Space complexity

Data are represented as binary in computers

Binary are used to store data for following reason
* Computer works on transistor so the data can be managed as weather it on or off
* On can be represented as __1__ and Off can be represented as __2__ 
* With laser technology light can reflect in two different directions.

Compiling all the statements binary is used since it can be represented as (1 or 0)


**Question**
* How do we use binary to represent the value we want to store?
* How many switches (bits) do we need to represent this data type?


### Representing integers in bits

* Tally scheme - The number represented by a sequence 10011011 is simple 5 since it has __5 (1 bits)__
* Base 2 representation - The number is sum of the value of bits i.e. the right most bit is 1 the left one is 2 and 3, 8 ....  so (01001100) mean 64 + 8 + 4 =76 


#### Number systems
* Base 10 
    - 0:9 -- 10^1
    - 10:99 -- 10^2
    - 100:999 -- 10^3
    - 1000:9999 -- 10^4

* Base 2 (0,1)
    - 0:1 -- 2^1
    - 2:3 -- 2^2
    - 4:7 -- 2^3
    

### Data Representations
* Byte is a smallest memory to store a data (8 bits = byte)
* 1 byte allows to store upto 256 combinations of data representation (2^8 = 256)
* 2 bytes can hold upto 65536(216) .


|S.N.| Type  | Size              | Description                   |
|----|-------|-------------------|-------------------------------|
|    | Integers                                                   |
|1.  |Byte   |8 bits             | Byte Length Integer           |
|2.  |Short  |16 bits            |Short Integer                  |
|3.  |Int    |32 bits            |Integer                        |
|4.  |Long   |64 bits            |Long Integer                   |
|    |Real Numbers                                                |
|5.  |Float  |32 bits            |Single precision floating point|
|6.  |Double |64 bits            |Double precision floating point|
|    |Other Types                                                 |
|7.  |char   |16 bits unicode character            | A single character            |                         
|8.  |Boolean|Ture or false      | A boolean value               | 

            
__QUIZ__
* Storing a day of week requires how much bits?
- 4 bits
* Number of people in the world?
- 64 bits
* Number of stars in the universe ?
- 128 bits

### Two's complement - Negative#'s
* A byte (i.e 8 bits) can represents integers in the range of -128 to 127
* -1 is 
