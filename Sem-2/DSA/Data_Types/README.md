# Data Types
## Abstract Data types
It is a mathematical model with a collection of oprations defined on that model. It defines the properties of the data and the operations that can be applied to that data.

A wall of ADT operations isolates a data structure from the program that uses it.

## ADTs - Stacks and Queues 
### Stacks - First in Last out
### Queues - Last in Last out

#### Stack operations 
* Create an empty stack.
* Push a new value x onto the  top of the stack (put one in).
* Pop a value from the top of the stack (take one out), removing whichever remaining value was most recently 'pushed', and returning it. 
* Peek at whichever value would be 'popped' next, without removing it.
* Get the size of the stack (number of values remaining).
* Clear the stack ( remove all the values ).

#### Queue operations 
* Create an empty stack.
* Enqueue a new value x at the back of the queue (put one in).
* Dequeue/poll a value from the front of the queue (take one out), removing whichever remaining value was last recently 'enqueued', and returning it.
* Peek at whichever value would be 'polled' next, without removing it.
* Get the size of the queue (number of values remaining)
* Clear the queue ( remove all the values)

#### Priority Queues
* Create an empty queue.
* Enqueue a new value x with priority p (put one in)
* Dequeue/poll a value from the priority queue (take one out), removing whichever remaining value has the highest priority, and returning it.
* Peek at whichever value would be 'polled' next, without removing it.
* Get the size of priority queue (number of all remaining values)
* Clear the priority queue (remove all the values)


## Quiz - stacks 
1. What is the top item on the stack when the sequence is complete:
    m = Stack()
    m.push('x')
    m.push('y')
    m.pop()
    m.push('z')
    m.peek()

-> z

2. What is the top item on the stack when the sequence is complete:

    m = Stack()
    m.push('x')
    m.push('y')
    m.push('z')
    While not m.isempty():
        m.pop()
        m.pop()

-> An error will occour 

3. What items are left in the queue after this sequence of operations 
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    q.dequeue()

-> 'dog',3


