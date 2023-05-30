from evaluating.evaluator import Evaluator

userExpression = input('Please enter your preferred expression: ')

print(Evaluator(userExpression).evaluate()[0])
