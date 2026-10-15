number = float(input("Enter a number: "))
epsilon = 0.0000001
guess = number
found = False
its = 0

while not found:
    its += 1
    updated_guess = 0.5 * (guess + number / guess)
    if abs(updated_guess - guess) < epsilon:
        break
    guess = updated_guess

print(f"The square root of your number is approximately {guess}")
print(f"It took {its} iterations")
