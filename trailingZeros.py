# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 * ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples

# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros



def zeros(n):
    factorial = 1
    zeros_list = []
    trailing_zeros = 0
    while (n>0):
        factorial = factorial * n
        n -= 1
    
    for idx, i in enumerate(str(factorial)):
        if i == '0':
            trailing_zeros += 1
            if idx == len(str(factorial))-1:
                 zeros_list.append(trailing_zeros)    
        if i != '0':
            zeros_list.append(trailing_zeros)
            trailing_zeros = 0
    return max(zeros_list)





# test.assert_equals(zeros(6), 1)
# test.assert_equals(zeros(12), 2)