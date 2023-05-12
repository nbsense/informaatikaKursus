import math

class Check:
    def isComma(item):
        return item == ','

    def isDigit(item):
        try:
            float(item)

            return True
        except:
            return False
    
    def isEqualPrecedence(initial, item):
        return initial == item
    
    def isFunction(item):
        return item == ' '
    
    def isGreaterPrecedence(initial, item):
        return initial > item

    def isInList(item, list):
        return item in list

    def isLeftAssociative(item):
        return Data.associative[item] == 'Left'

    def isLeftParenthesis(item):
        return item == '('
    
    def isPunctuation(item):
        return item == '.'

    def isRightParenthesis(item):
        return item == ')'

class Data:
    associative = {'+': 'Left', '-': 'Left', '*': 'Left', '/': 'Left', '^': 'Right', ' ': 'Left'} # ' ' represents a mathematical function: ghetto.
    functions = {}
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, ' ': 4} # ' ' represents a mathematical function: ghetto.

    operatorStack = []
    outputAnswer = []
    outputQueue = []

class Helper:
    def calculate(x, y, operator):
        x = float(x)
        y = float(y)

        match operator:
            case '+':
                return x + y
            case '-':
                return x - y
            case '*':
                return x * y
            case '/':
                if y == 0:
                    return math.inf / 1
                else:
                    return x / y
            case '^':
                if x < 0:
                    return -abs(x)**y
                else:
                    return x ** y

class Parser:
    def __init__(self, expression):
        self.expression = expression.replace(' ', '')

    def shuntingYard(self):
        for index in range(len(self.expression)):
            token = self.expression[index]

            if Check.isComma(token):
                while Data.operatorStack and not Check.isLeftParenthesis(Data.operatorStack[-1]):
                    Data.outputQueue.append(Data.operatorStack.pop())

            if Check.isDigit(token):
                if Data.outputQueue and (Check.isDigit(self.expression[index - 1]) or Check.isPunctuation(self.expression[index - 1])):
                    Data.outputQueue[-1] += token
                else:
                    Data.outputQueue.append(token)

            if Check.isFunction(token):
                Data.operatorStack.append(token)

            if Check.isInList(token, Data.operators):
                while Data.operatorStack and not Check.isLeftParenthesis(Data.operatorStack[-1]) and (Check.isGreaterPrecedence(Data.operators[Data.operatorStack[-1]], Data.operators[token]) or (Check.isEqualPrecedence(Data.operators[Data.operatorStack[-1]], Data.operators[token]) and Check.isLeftAssociative(token))):
                    Data.outputQueue.append(Data.operatorStack.pop())

                Data.operatorStack.append(token)
            
            if Check.isLeftParenthesis(token):
                Data.operatorStack.append(token)

            if Check.isPunctuation(token):
                Data.outputQueue[-1] += token

            if Check.isRightParenthesis(token):
                while Data.operatorStack and not Check.isLeftParenthesis(Data.operatorStack[-1]):
                    Data.outputQueue.append(Data.operatorStack.pop())

                if Data.operatorStack and Check.isLeftParenthesis(Data.operatorStack[-1]): # otherwise there are mismatched parentheses: error.
                    Data.operatorStack.pop()

                if Data.operatorStack and Check.isFunction(Data.operatorStack[-1]):
                    Data.outputQueue.append(Data.operatorStack.pop())

        while Data.operatorStack:
            if not Check.isLeftParenthesis(Data.operatorStack[-1]): # otherwise there are mismatched parentheses: error.
                Data.outputQueue.append(Data.operatorStack.pop())

        print(Data.outputQueue)

    def reversePolishNotation(self):
        for index in range(len(Data.outputQueue)):
            token = Data.outputQueue[index]

            if Check.isDigit(token):
                Data.outputAnswer.append(token)

            if Check.isInList(token, Data.operators):
                result = Helper.calculate(Data.outputAnswer[-2], Data.outputAnswer[-1], token)

                Data.outputAnswer.pop()
                Data.outputAnswer.pop()

                Data.outputAnswer.append(result)

    def finalSolution(self): # Holocaust reference: abandon the minorities.
        self.shuntingYard()
        self.reversePolishNotation()

        print(Data.outputAnswer[0])

Parser('536176.597410741 + 98164.2818300 * 1302.1097739 / (1.98398 - 5.148041) ^ 2.9830 ^ 3.585').finalSolution()

# We hate blacks & minorities
# God, Honor, Homeland
# Heil white Evropa
# Heil victory