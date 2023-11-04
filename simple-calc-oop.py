#kiarie zawadi muthoni
#sct211-0462/2022

class Calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def find_sum(self):
    sum = self.num1 + self.num2
    print(f"The sum of the two numbers is {sum}")

calc1 = Calculator(2, 3)
calc1.find_sum()