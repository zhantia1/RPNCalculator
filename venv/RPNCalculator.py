import numpy as np
from MyStack import *

class RpnCalculator:
   # Class constants
   ADDITION = "+"
   SUBTRACTION = "-"
   MULTIPLICATION = "*"
   FLOOR_DIVISION = "//"

   def __init__(self):
      pass

   @staticmethod
   def eval(rpn_expression):
      parsed_expression = RpnCalculator.parse(rpn_expression)
      return RpnCalculator.eval_tokens(parsed_expression)

   @staticmethod
   def parse(rpn_expression):
      return rpn_expression.split()

   @staticmethod
   def multiply(a, b):
      if a == 0:
         return 0
      if a < 0:
         return -b - RpnCalculator.multiply(-a - 1, b)
      return b + RpnCalculator.multiply(a - 1, b)

   @staticmethod
   def eval_tokens(tokens):
      stack = MyStack(0, len(tokens))
      for token in tokens:
         try:
            int_token = int(token)
            stack.push(int_token)
         except ValueError:
            if token == RpnCalculator.ADDITION:
               operand2 = stack.pop()
               operand1 = stack.pop()
               stack.push(operand1 + operand2)
            elif token == RpnCalculator.SUBTRACTION:
               operand2 = stack.pop()
               operand1 = stack.pop()
               stack.push(operand1 - operand2)
            elif token == RpnCalculator.FLOOR_DIVISION:
               operand2 = stack.pop()
               operand1 = stack.pop()
               stack.push(operand1 // operand2)
            elif token == RpnCalculator.MULTIPLICATION:
               operand2 = stack.pop()
               operand1 = stack.pop()
               stack.push(RpnCalculator.multiply(operand1, operand2))
            else:
               raise Exception("Invalid operator")
      final_result = stack.pop()
      if stack.is_empty():
         return final_result
      raise Exception("Invalid number of operator/operands")

def test():
   valid_basic_test_bank = ["2 3 +", "2 3 -", "2 3 *", "6 3 //", "3",
                            "-5 0 *", "-5 -5 *"]
   valid_advanced_test_bank = ["2 3 -4 + *", "10 2 3 + - 5 *", "2 1 // 3 + 11 "
                                                              "10 - *"]
   invalid_test_bank = ["", "1 +", "1 1", "1 1 test", "1 1 + +", "junk"]

   print("testing valid basic expressions: ")
   for expression in valid_basic_test_bank:
      try:
         print("testing expression:", expression)
         result = RpnCalculator.eval(expression)
         print("result: ", result)
      except Exception as e:
         print("error: ", e)

   print("testing valid advanced expressions: ")
   for expression in valid_advanced_test_bank:
      try:
         print("testing expression:", expression)
         result = RpnCalculator.eval(expression)
         print("result: ", result)
      except Exception as e:
         print("error: ", e)

   print("testing invalid expressions: ")
   for expression in invalid_test_bank:
      try:
         print("testing expression:", expression)
         result = RpnCalculator.eval(expression)
         print("result: ", result)
      except Exception as e:
         print("error: ", e)

if __name__ == '__main__':
   test()
