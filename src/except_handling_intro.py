#try:
#    file = open("nonexistent_file.txt", "r")
#except ValueError:
#    print("The file you are looking for does not exist")

#number = -5
#if number < 0:
#    raise ValueError("The number cannot be negative")

#def check_number(num):
#    if num > 100:
#        raise ValueError("number cannot be greater than 100")
#    if num < 0:
#        raise ValueError("Number must be positive")
#    return f"Your number {num} is valid"


#print(check_number(120))

# Catching self made errors

#try:
#    number = -10
#    if number < 0:
#        raise ValueError("Negative errors are not allowed")
#except ValueError as e:
#    print(f"Custom Error Caught: {e}")

#Custom Exceptions

#class MyCustomError(Exception):
#    pass

# Raise like a built-in error
#raise MyCustomError("This is my custom error!")

#class AgeToolowError(Exception):
#    def __init__(self, age):
#        self.age = age
#        super().__init__(f"Age {age} is too low! Minimum is 18.")

#try:
#    age = 16
#    if age < 18:
#        raise AgeToolowError(age)
#except AgeToolowError as e:
#    print(e)


#class NotEnoughFundsError(Exception):
#    def __init__(self, balance, amount):
#        self.balance = balance
#        self.amount = amount
#        super().__init__(f"Insufficient funds! Balance: ${balance}, Tried to withdraw: ${amount}.")

# def withdraw_money(balance, amount):
#     if amount > balance:
#         raise NotEnoughFundsError(balance, amount)
#     return balance - amount


# # Test
# try:
#     balance = 100
#     print(withdraw_money(balance, 150)) # Too much withdrawal
# except NotEnoughFundsError as e:
#     print(f"Error: {e}")   

# try:
#     temp = -298
#     if temp < -273:
#         raise ValueError("temperature is below absolute zero")
# except ValueError as e:
#     print(f"Error: {e}")

# Custom Exception

# class PasswordTooShort(Exception):
#     def __init__(self, password):
#         self.password = password
#         super().__init__(f"password is too short: {password}")

# try:
#     password = (input("Enter password: \n"))
#     if len(password) < 8:
#         raise PasswordTooShort(password)
# except PasswordTooShort as e:
#     print(f"Error: {e}")

# program checks if a person is at least age 18; which implies they have at least $500

