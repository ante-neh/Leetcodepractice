Design a stack to support an additional operation that returns the minimum element from the stack in constant time.
The stack should continue supporting all other operations like push, pop, top, size, empty, etc., with no degradation in these operations’ performance.



Example:
if __name__ == '__main__':
 
    s = MinStack()
 
    s.push(6)
    print(s.getMin())        # prints 6
 
    s.push(7)
    print(s.getMin())        # prints 6
 
    s.push(8)
    print(s.getMin())        # prints 6
 
    s.push(5)
    print(s.getMin())        # prints 5
 
    s.push(3)
    print(s.getMin())        # prints 3
 
    print(s.pop())          # prints 3
    print(s.getMin())        # prints 5
 
    s.push(10)
    print(s.getMin())        # prints 5
 
    print(s.pop())          # prints 10
    print(s.getMin())        # prints 5
 
    print(s.pop())          # prints 5
    print(s.getMin())        # prints 6
