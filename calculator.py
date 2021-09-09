class Calculator:

    op_count = 0

    @classmethod
    def update_count(cls):
        cls.op_count += 1

    def __init__(self,number1,number2):
        self.num1 = number1
        self.num2 = number2

    def add(self):
        self.update_count()
        return self.num1 + self.num2

    def sub(self):
        self.update_count()
        return self.num1 - self.num2


    def multi(self):
        self.update_count()
        return self.num1 * self.num2

    def divide(self):
        self.update_count()
        return self.num1 / self.num2
