"""

1. Write a program in Python to find the occurance of alphabet in the name.
2. Implement a custom dictionary in Python having capacity of 5 elements.
  add function of add and size method. When you add 6th element it should not allow.
3. Write a program in Python to find fibbonaci series in the decorator.
4. SQL: Write a window function to find 3rd highest salary over the department.
5. WE have input data   1,100
                        2,200
                        3,300 --> 1,100
                                  2,300
                                  2,500
"""


# from functools import Counter
def count_alphabes(name: str):
    output = {}
    for char in name:
        if char.isalpha():
            if char in output:
                output[char] += 1
            else:
                output[char] = 1

    print(output)


count_alphabes("Sarwar Hayat")


class CustomDict:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = {}

    def add(self, key, value):
        if len(self.data) >= self.capacity:
            raise Exception("Dictionary is full. Cannot add more elements.")

        self.data[key] = value

    def size(self):
        return len(self.data)



def fibbonachi(n):
    a,b  = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b

def decorative(func):
    def wrapper(*args, **kwargs):
        print("fib series")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorative
def print_fibbonachi(n):
    for num in fibbonachi(n):
        print(num)


