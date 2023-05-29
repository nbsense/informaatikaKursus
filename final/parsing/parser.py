from parsing.lexer import Lexer
from parsing.utils import Utils

class Parser:
    def __init__(self, expression):
        self.tokens = Lexer(expression).tokenize()
        self.operatorStack = []
        self.outputQueue = []

    def parse(self):
        amountOfTokens = len(self.tokens)

        currentToken = None

        for index in range(amountOfTokens):
            currentToken = self.tokens[index]

            if Utils.isNumber(currentToken):
                self.outputQueue.append(currentToken)

            if Utils.isFunction(currentToken):
                self.operatorStack.append(currentToken)

            if Utils.isOperator(currentToken):
                while self.operatorStack and not Utils.isLeftParenthesis(self.operatorStack[-1]) and (Utils.isGreater(self.operatorStack[-1], currentToken) or (Utils.isEqual(self.operatorStack[-1], currentToken) and Utils.isLeftAssociative(currentToken))):
                    self.outputQueue.append(self.operatorStack.pop())

                self.operatorStack.append(currentToken)

            if Utils.isComma(currentToken):
                while self.operatorStack and not Utils.isLeftParenthesis(self.operatorStack[-1]):
                    self.outputQueue.append(self.operatorStack.pop())

            if Utils.isLeftParenthesis(currentToken):
                self.operatorStack.append(currentToken)

            if Utils.isRightParenthesis(currentToken):
                while self.operatorStack and not Utils.isLeftParenthesis(self.operatorStack[-1]):
                    self.outputQueue.append(self.operatorStack.pop())

                self.operatorStack.pop()

                while self.operatorStack and Utils.isFunction(self.operatorStack[-1]):
                    self.outputQueue.append(self.operatorStack.pop())

        while self.operatorStack:
            self.outputQueue.append(self.operatorStack.pop())

        return self.outputQueue