import math

number = float(input("Enter a number: "))
epsilon = 0.0000001 
actual_value = number ** 0.5
its = 1

lower = math.floor(actual_value)
upper = math.ceil(actual_value)

while True: 
    guess = (lower + upper) / 2
    if abs(guess - actual_value) < epsilon:
        break
    if guess > actual_value:
        upper = guess
    else:
        lower = guess
    its += 1

print(f"The square root of {number} is approximately {guess}.")
print(f"This took {its} iterations.")
