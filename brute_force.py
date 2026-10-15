num = float(input("Enter a decimal number to get a square root estimate for it: "))
estimate = 0
test_num = 0
while estimate <= num:
    estimate = test_num ** 2 
    test_num += 0.000001
final_num = test_num
below_num = (test_num - 0.000001)
if abs(below_num ** 2 - num) < abs(estimate - num):
    estimate = below_num ** 2
    final_num = below_num
print(f"The square root of {num} is approximately {final_num}. It's off by {abs(test_num - num ** 0.5)}")
