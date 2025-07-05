# Homework 1. ToDo List Application

# Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.
# Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} - {self.description} (Due: {self.due_date}) [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if not task.completed:
                print(task)
                found = True
        if not found:
            print("All tasks are complete.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return f"Marked '{title}' as complete."
        return "Task not found."

def todo_cli():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List ---")
        print("1. Add Task\n2. List All Tasks\n3. Mark Task as Complete\n4. Show Incomplete Tasks\n5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date: ")
            todo.add_task(Task(title, desc, due))
        elif choice == '2':
            todo.list_all_tasks()
        elif choice == '3':
            title = input("Enter task title to mark complete: ")
            print(todo.mark_task_complete(title))
        elif choice == '4':
            todo.list_incomplete_tasks()
        elif choice == '5':
            break



# Homework 2. Simple Blog System

# Define Post Class:
# Create a Post class with attributes like title, content, and author.
# Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
# Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.
# Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.
# Test the Application:
# Create instances of posts and test the functionality of your Blog system.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\n{self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("No posts available.")
        for post in self.posts:
            print(post)

    def posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                found = True
        if not found:
            print("No posts found for that author.")

    def delete_post(self, title):
        before = len(self.posts)
        self.posts = [post for post in self.posts if post.title != title]
        if len(self.posts) < before:
            print("Post deleted.")
        else:
            print("Post not found.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print("Post updated.")
                return
        print("Post not found.")

    def latest_posts(self, n=5):
        print("\n--- Latest Posts ---")
        for post in self.posts[-n:]:
            print(post)

def blog_cli():
    blog = Blog()
    while True:
        print("\n--- Blog System ---")
        print("1. Add Post\n2. List All Posts\n3. Show Posts by Author")
        print("4. Delete Post\n5. Edit Post\n6. Latest Posts\n7. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == '2':
            blog.list_posts()
        elif choice == '3':
            author = input("Author name: ")
            blog.posts_by_author(author)
        elif choice == '4':
            title = input("Title of post to delete: ")
            blog.delete_post(title)
        elif choice == '5':
            title = input("Title of post to edit: ")
            content = input("New Content: ")
            blog.edit_post(title, content)
        elif choice == '6':
            blog.latest_posts()
        elif choice == '7':
            break


  
# Homework 3. Simple Banking System

# Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.
# Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.
# Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.
# Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
# Test the Application:
# Create instances of accounts and test the functionality of your Banking system.
class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        print(f"${amount} withdrawn successfully.")
        return True

    def __str__(self):
        return f"Account {self.number} - {self.holder}: Balance = ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account.number] = account
            print("Account created successfully.")

    def get_account(self, number):
        return self.accounts.get(number)

    def transfer(self, from_num, to_num, amount):
        from_acc = self.get_account(from_num)
        to_acc = self.get_account(to_num)
        
        if not from_acc or not to_acc:
            print("Invalid account number.")
            return
        if from_acc.withdraw(amount):
            to_acc.deposit(amount)
            print("Transfer completed.")

def bank_cli():
    bank = Bank()
    while True:
        print("\n--- Banking System ---")
        print("1. Add Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transfer\n6. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            number = input("Account Number: ")
            holder = input("Account Holder Name: ")
            bank.add_account(Account(number, holder))
        elif choice == '2':
            number = input("Account Number: ")
            amount = float(input("Amount to deposit: "))
            acc = bank.get_account(number)
            if acc:
                acc.deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            number = input("Account Number: ")
            amount = float(input("Amount to withdraw: "))
            acc = bank.get_account(number)
            if acc:
                acc.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            number = input("Account Number: ")
            acc = bank.get_account(number)
            if acc:
                print(acc)
            else:
                print("Account not found.")
        elif choice == '5':
            from_num = input("From Account Number: ")
            to_num = input("To Account Number: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer(from_num, to_num, amount)
        elif choice == '6':
            break


def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. ToDo List")
        print("2. Blog System")
        print("3. Banking System")
        print("4. Exit")
        choice = input("Select an application: ")

        if choice == '1':
            todo_cli()
        elif choice == '2':
            blog_cli()
        elif choice == '3':
            bank_cli()
        elif choice == '4':
            print("Goodbye!")
            break
        
