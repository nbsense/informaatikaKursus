from evaluating.evaluator import Evaluator

userExpression = input('Please enter your preffered expression: ')

print(Evaluator(userExpression).evaluate()[0])