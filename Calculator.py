class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        else:
            return self.num1 / self.num2
    
    def power(self):
        return self.num1 ** self.num2
    
    def is_even(self):
        if self.num1 % 2 == 0:
            return True
        else:
            return False
    
    def is_prime(self):
        if self.num1 < 2:
            return False
        for i in range(2, int(self.num1 ** 0.5) + 1):
            if self.num1 % i == 0:
                return False
        return True