# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return f'Area: {math.pi * self.radius ** 2:.2f}'
    
    def perimeter(self):
        return f'Perimeter: {2 * math.pi * self.radius:.2f}'

r = float(input('Enter circle radius: '))
c = Circle(r)

print(c.area(), c.perimeter())


# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
from datetime import datetime
class Person:
    def __init__(self, name, country, birth_date, occupation):
        self.name = name
        self.country = country
        self.birth_date = birth_date
        self.occupation = occupation
    def age(self):
        return f"{self.name.capitalize()}, your age is {datetime.today().year - datetime.strptime(self.birth_date, '%Y-%m-%d').year}"

name = input('Enter your name: ')
country = input('Enter your living country: ')
birth_date = input('Enter your date of birth (e.g 2000-01-01): ')
occupation = input('Enter your occupation: ')

p1 = Person(name, country, birth_date, occupation)

print(p1.age())


# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return f'Addition: {self.a + self.b}'
    
    def subtraction(self):
        return f'Subtraction: {self.a - self.b}'
    
    def multiplication(self):
        return f'Multiplication: {self.a * self.b}'

    def division(self):
        try:
             return self.a / self.b
        except ZeroDivisionError:
            return 'It seems like there is 0 value'


a = float(input('Enter the  first number: '))
b = float(input('Enter the second number: '))
c1 = Calculator(a, b)

print(c1.addition(), c1.subtraction(), c1.multiplication(), c1.division())

        
# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
import math
class Shape:
    def area(self):
        raise NotImplementedError('you need to implement this method')

    def perimeter(self):
        raise NotImplementedError('you need to implement this method')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return f'Circle area: {math.pi * self.radius**2:.2f}'
    
    def perimeter(self):
        return f'Circle perimeter: {2 * math.pi * self.radius:.2f}'

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c)/2
        A = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return f'Trianle area: {A}'

    def perimeter(self):
        return f'Triangle perimeter: {self.a + self.b + self.c}'

class Square(Shape):
    def __init__(self, a):
        self.a = a
    
    def area(self):
        return f'Square area: {self.a**2}'
    
    def perimeter(self):
        return f'Square perimeter: {4 * self.a}'

c1 = Circle(5)
print(c1.area(), c1.perimeter())

t1 = Triangle(3, 4, 5)
print(t1.area(), t1.perimeter())

s1 = Square(4)
print(s1.area(), s1.perimeter())



# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def add(node, data):
            if not node: return Node(data)
            if data < node.data:
                node.left = add(node.left, data)
            else:
                node.right = add(node.right, data)
            return node
        self.root = add(self.root, data)

    def search(self, key):
        def find(node, key):
            if not node: return False
            if key == node.data: return True
            return find(node.left, key) if key < node.data else find(node.right, key)
        return find(self.root, key)
    
bst = BST()
bst.insert(30)
bst.insert(20)
bst.insert(95)

print(bst.search(30)) 
print(bst.search(90))  


# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        return f'{self.items.pop()} is popped'
    
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
s = Stack()

s.push(5)
s.push(40)
s.push('Hello')

print(s.pop())

print('Peek:', s.peek())
print('Size:', s.size())

    
# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()    

ll.delete(20)
ll.display()      



# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Added {item_name} for ${price:.2f} to the cart.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Removed {item_name} from the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    def total_price(self):
        total = sum(self.items.values())
        print(f"Total price: ${total:.2f}")
        return total

    def show_cart(self):
        print("Shopping Cart:")
        for item, price in self.items.items():
            print(f"- {item}: ${price:.2f}")
        if not self.items:
            print("- (Cart is empty)")

cart = ShoppingCart()
cart.add_item("Apple", 1.20)
cart.add_item("Milk", 2.50)
cart.add_item("Bread", 1.80)
cart.show_cart()
cart.remove_item("Milk")
cart.show_cart()
cart.total_price()



# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.stack:
            print("Stack is empty!")
            return None
        return self.stack.pop()

    def display(self):
        print("Stack (top to bottom):")
        for item in reversed(self.stack):
            print(item)
        if not self.stack:
            print("(Stack is empty)")

stack = Stack()
stack.push("Book")
stack.push("Laptop")
stack.push("Notebook")
stack.display()
print("Popped item:", stack.pop())
stack.display()


# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}.")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
            return None
        return self.queue.pop(0)

    def display(self):
        print("Queue (front to rear):")
        for item in self.queue:
            print(item)
        if not self.queue:
            print("(Queue is empty)")

queue = Queue()
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")
queue.display()
print("Dequeued item:", queue.dequeue())
queue.display()


# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"{self.account_holder}'s balance: ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[name] = BankAccount(name)
            print(f"Account created for {name}.")

    def get_account(self, name):
        return self.accounts.get(name, None)

bank = Bank()
bank.create_account("John")
bank.create_account("Alice")

john = bank.get_account("John")
alice = bank.get_account("Alice")

john.deposit(1000)
john.withdraw(250)
john.display_balance()

alice.deposit(500)
alice.withdraw(700)  
alice.display_balance()
