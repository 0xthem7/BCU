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


    class Stack:
        data = None
        top = 0

    push(element):
        top += 1
        data[top] -= element
    pop():
        if isEmpty():
            return "Stack is empty"
        else
            element -= data[top]
            top -= 1
            return element
    peek():
        if isEmpty():
            return "Stack is empty"
        else:
            return data[top]
    isEmpty():
        return top == -1



Time complexity of each of the operation is O(1)



4. Write pseudocodes of enqueue, dequeue & isEmpty implementation of an ADT called Queue. Discuss complexities of each operation in terms of Big-O.

class Queue:
  data = None
  front = None
  rear = None

enqueue(element):
  rear += 1
  data[rear] = element

dequeue():
  if isEmpty():
    return "Queue is empty"
  else:
    element = data[front]
    front += 1
    return element

isEmpty():
  return (front > rear)

Time complexity of each of the opration is O(1)


5. Convert the following infix to postfix
a. 3 + 4 * 5 / 6
Postfix: 345*6/+

b. (300 + 23) * (43 - 21) / (84 + 7)
Postfix: 30023+4321-*847+/

c.  (4 + 8) * (6 - 5) / ((3 - 2) * (2 + 2))
Postfix: 48+65-32-22+/

d. A + (B * C - (D / E ^ F) * G) * H
Postfix: ABCDEF^/G-H*+

e. 44 - 15 / (9 - 3 * 2) + 12
Postfix: 4415-932*-/12+

f. 14 - (6 - 10) - 10
Postfix: 610--10-

g.  A / B ^ C - D
Postfix: ABC^/D-

h.  A + (B * C - (D / E ^ F ^ G) * H) * I
Postfix: ABCDEF^G^^/-HI*+


6. Convert infix to prefix (QN 5).
a. 3 + 4 * 5 / 6
Prefix: + 3 / * 4 5 6

b. (300 + 23) * (43 - 21) / (84 + 7)
Prefix: / * + 300 23 - 43 21 + 84 7

c. (4 + 8) * (6 - 5) / ((3 - 2) * (2 + 2))
Prefix: / * + 4 8 - 6 5 * - 3 2 + 2 2

d. A + (B * C - (D / E ^ F) * G) * H
Prefix: + A * - * B C / D ^ E F G H

e. 44 - 15 / (9 - 3 * 2) + 12
Prefix: + - 44 / 15 - 9 * 3 2 12

f. 14 - (6 - 10) - 10
Prefix: - - 14 - 6 10 10

g.  A / B ^ C - D
Prefix: - / A ^ B C D

h. A + (B * C - (D / E ^ F ^ G) * H) * I
Prefix: + A * - * B C / D ^ ^ E F G H I  


8. Solve the following postfix expressions: 
a. 2 3+ = 3 + 2 = 5
b. 7 8* = 8 * 7 = 56
c. 6 2/5+ = 6/2 = 3; 3 +5 = 8
d. 5 6 2 / + = 6 / 2 = 3; 5 + 3 = 8
e. 6 5 * 7 3 – 4 8 + * + = 6 * 5 = 30;  7-3 = 4; 4+8 =12; 30 * 12 = 360 

9. Evaluate the following expression, showing the state of the stack at each step.

a. 6 5 * 7 3 - 4 8 + * +

    Push 6 onto the stack.
    Stack: 6
    Push 5 onto the stack.
    Stack: 6 5
    Pop two operands (5 and 6) and apply the "*" operator: 6 * 5 = 30. Push the result back onto the stack.
    Stack: 30
    Push 7 onto the stack.
    Stack: 30 7
    Push 3 onto the stack.
    Stack: 30 7 3
    Pop two operands (3 and 7) and apply the "-" operator: 7 - 3 = 4. Push the result back onto the stack.
    Stack: 30 4
    Push 4 onto the stack.
    Stack: 30 4 4
    Push 8 onto the stack.
    Stack: 30 4 4 8
    Pop two operands (8 and 4) and apply the "+" operator: 4 + 8 = 12. Push the result back onto the stack.
    Stack: 30 12
    Pop two operands (12 and 30) and apply the "*" operator: 30 * 12 = 360. Push the result back onto the stack.
    Stack: 360
    Pop the final result from the stack: 360.
    Answer: 360

b . 3 8 + 5 + 10 – 3 / 4 + 5 + 7 -

    Push 3 onto the stack.
    Stack: 3
    Push 8 onto the stack.
    Stack: 3 8
    Pop two operands (8 and 3) and apply the "+" operator: 3 + 8 = 11. Push the result back onto the stack.
    Stack: 11
    Push 5 onto the stack.
    Stack: 11 5
    Pop two operands (5 and 11) and apply the "+" operator: 11 + 5 = 16. Push the result back onto the stack.
    Stack: 16
    Push 10 onto the stack.
    Stack: 16 10
    Pop two operands (10 and 16) and apply the "-" operator: 16 - 10 = 6. Push the result back onto the stack.
    Stack: 6
    Push 3 onto the stack.
    Stack: 6 3
    Pop two operands (3 and 6) and apply the "/" operator: 6 / 3 = 2. Push the result back onto the stack.
    Stack: 2
    Push 4 onto the stack.
    Stack: 2 4
    Pop two operands (4 and 2) and apply the "+" operator: 2 + 4 = 6. Push the result back onto the stack.
    Stack: 6
    Push 5 onto the stack.
    Stack: 6 5
    Pop two operands (5 and 6) and apply the "+" operator: 6 + 5 = 11. Push the result back onto the stack.
    Stack: 11
    Push 7 onto the stack.
    Stack: 11 7
    Pop two operands (7 and 11) and apply the "-" operator: 11 - 7 = 4. Push the result back onto the stack.
    Stack: 4
    The final result on the stack is 4.
    Answer: 4


c . 14 6 10 - - 10 –
    Push 14 onto the stack.
    Stack: 14
    Push 6 onto the stack.
    Stack: 14 6
    Push 10 onto the stack.
    Stack: 14 6 10
    Pop two operands (10 and 6) and apply the "-" operator: 6 - 10 = -4. Push the result back onto the stack.
    Stack: 14 -4
    Pop two operands (negative 4 and 14) and apply the "-" operator: 14 - (-4) = 18. Push the result back onto the stack.
    Stack: 18
    Push 10 onto the stack.
    Stack: 18 10
    Pop two operands (10 and 18) and apply the "-" operator: 18 - 10 = 8. Push the result back onto the stack.
    Stack: 8
    The final result on the stack is 8.
    Answer: 8


10. Solve the following prefix expressions

a. Prefix: + X Y
Solution: X + Y

b. Prefix: +2 / 8 4
Solution: 2 + (8 / 4) = 2 + 2 = 4

c. Prefix: * + a – b c / - d e + - f g h 
Solution: (h + (7 + (b + c))) * 7

d. Prefix:+ / 6 2 5
Solution: 8


11. 

ReverseArrayUsingStack(array):
  Stack stack = None

  for each element in array:
     stack.push(element)

  reversedArray = list(empty )

  while stack is not empty:
    element = stack.pop()
    reversedArray.append(element)

  return reversedArray


12.

    push(d): Stack: d
    push(h): Stack: d, h
    pop( ): Popped: h, Stack: d
    push(f): Stack: d, f
    push(s): Stack: d, f, s
    pop( ): Popped: s, Stack: d, f
  

  pop( ): Popped: f, Stack: d
    push(m): Stack: d, m

Popped Values Sequence: h, s, f
Final State of Stack: Top: m, Elements: d, m

b. Now let's consider the operations using enqueue and dequeue:

Initial State: Empty Queue

    enqueue(d): Queue: d
    enqueue(h): Queue: d, h
    dequeue( ): Dequeued: d, Queue: h
    enqueue(f): Queue: h, f
    enqueue(s): Queue: h, f, s
    dequeue( ): Dequeued: h, Queue: f, s
    dequeue( ): Dequeued: f, Queue: s
    enqueue(m): Queue: s, m

Dequeued Values Sequence: d, h, f
Final State of Queue: Front: s, Elements: s, m

13.
Given postfix expression: a a + b c - *
Substituting values: a = 10, b = 3, c = -2

Steps:

    Push a (10) onto the stack: Stack: 10
    Push a (10) onto the stack: Stack: 10, 10
    Pop two operands (10 and 10) and apply the "+" operator: 10 + 10 = 20. Push the result back onto the stack: Stack: 20
    Push b (3) onto the stack: Stack: 20, 3
    Push c (-2) onto the stack: Stack: 20, 3, -2
    Pop two operands (-2 and 3) and apply the "-" operator: 3 - (-2) = 5. Push the result back onto the stack: Stack: 20, 5
    Pop two operands (5 and 20) and apply the "*" operator: 20 * 5 = 100. Push the result back onto the stack: Stack: 100

Final result on the stack: 100

The value of the postfix expression "a a + b c - *" with a = 10, b = 3, and c = -2 is 100.



14. 
a. To pop in the order 2, 4, 5, 3, 1:
Push: 1 2 3 4 5
Pop: 2 4 5 3 1

b. To pop in the order 1, 5, 4, 2, 3:
Push: 1 2 3 4 5
Pop: 1 5 4 2 3

c. To pop in the order 1, 3, 5, 4, 2:
Push: 1 2 3 4 5
Pop: 1 3 5 4 2


15. 
a. 
It is possible to create a queue that supports both insertions (enqueue) and extractions (dequeue) in constant time O(1). This is due to the fact that a linked list requires constant time to add or remove elements from the head or tail nodes as long as you have a reference to those nodes.

b. 

It is possible to implement a stack with both insertions (push) and extractions (pop) in constant time O(1).

The index of the top element would be tracked for an array-based approach. When an element is pushed, the top index is increased, and the new element is then stored at that index. You only decrease the top index when you pop an element. Both of these operations use the top index directly, therefore they are O(1) operations

19. 19. Assume you have a queue with operations: enqueue(), dequeue(), isEmpty(). How would you use the queue methods to simulate a stack, in particular, push() and pop() ?

To simulate a stack using a queue and implement the push() and pop() oprations accordinhly.

    Initialize two queues, let's call them queue1 and queue2.

    Push Operation (simulating push using enqueue()):
        When you want to push an element onto the simulated stack:
            Enqueue the element into queue1.
        The idea is to maintain all elements in queue1 in the order they were pushed.

    Pop Operation (simulating pop using enqueue() and dequeue()):
        When you want to pop an element from the simulated stack:
            While there is more than one element in queue1, dequeue elements from queue1 and enqueue them into queue2.
            Dequeue the last element from queue1. This element will be the top element of the simulated stack.
            Swap the names of queue1 and queue2 so that queue1 now contains the remaining elements in the order they were pushed.

By implementing the push and pop operations in this manner, the behaviour of a queues is being mimicking.
