# Tutorial 1 : Attempt all questions 

1. State the difference between presistent & ephemeral data structure.
-> The difference between presistent  & ephemeral data structure are mentioned below.

### Presistent
    * Data structure which always preserves its previous versions when its modified.
    * Persistent data structure are effectively immutable, as their operations don't update the data structure, instead always yeild a new data structure 

### Ephemeral 
    * Data Structure which never preserves its pervious versions when its modified.
    * Since it does not store the previous version of itself, it makes a simpler data structure 

2. Solve **Tower of Hanoi** for 3 no. discs recursively, write pseudocode and derive its asymptotic time complexity in term of Big-O.

```
def towerOfHanoi(n=3,from_rod, to_rod, act_rod)
    if n == 0:
        return
    towerOfHanoi(n-1,from_rod,act_rod,to_rod)
    print("Move",n,"disk","from_rod","to_rod",to_rod)
    towerOfHanoi(n-1,aux_rod,to_rod,from_rod)
n = 3

towerofHanoi(3,'A','B','C')
```

* Asymptotic time complexity in term of Big-O for is O(2^n)

**Derivation**
Let time required for n disk be T(n)
There are two recursive call for the function towerOfHanoi to move a disk form rod 'A'to rod 'C', let it be K

T(n) = 2T(n-1)  + k
T(0) = k1 #Constant
T(1) = 2k1 + k
T(2) = 4k1 + 2k + k

Coffecient of k = 2n 
Coffecient of k1= 2n -1 

3. Write pseudocode of **push, pop, peek & isEmpty** implementation of an ADT called Stack. Discuss complexities of each operation in terms of Big-O




  
