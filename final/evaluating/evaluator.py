import math
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsing.parser import Parser
from parsing.utils import Utils

functions = {'ceil': math.ceil, 'fabs':math.fabs, 'factorial': math.factorial, 'floor': math.floor, 'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt, 'acos': math.acos, 'asin': math.asin, 'atan': math.atan, 'cos': math.cos, 'sin': math.sin, 'tan': math.tan, 'acosh': math.acosh, 'asinh': math.asinh, 'atanh': math.asinh, 'cosh': math.cosh, 'sinh': math.sinh, 'tanh': math.tanh, 'gamma': math.gamma}

class Compute():
    def function(name, token):
        return functions[name](float(token))

    def operator(name, item, token):
        match name:
            case '+':
                return float(token) + float(item)
            
            case '-':
                return float(token) - float(item)
            
            case '*':
                return float(token) * float(item)
            
            case '/':
                return float(token) / float(item)
            
            case '^':
                return float(token) ** float(item)

class Evaluator:
    def __init__(self, expression):
        self.outputQueue = []
        self.postfixNotation = Parser(expression).parse()

    def evaluate(self):
        amountOfTokens = len(self.postfixNotation)

        currentToken = None

        for index in range(amountOfTokens):
            currentToken = self.postfixNotation[index]

            if Utils.isFunction(currentToken):
                final = Compute.function(currentToken, self.outputQueue.pop())

                self.outputQueue.append(final)

            if Utils.isNumber(currentToken):
                self.outputQueue.append(currentToken)

            if Utils.isOperator(currentToken):
                final = Compute.operator(currentToken, self.outputQueue.pop(), self.outputQueue.pop())

                self.outputQueue.append(final)

        return self.outputQueue