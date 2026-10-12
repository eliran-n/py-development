
# Find the minimum positive integer that its sum of digits
# multiplied by 6 equals the number itself

def find_digit_product_match():

    factor = 6
    for i in range(1, 1000):
        current_number = i
        digits_sum = 0
        while current_number != 0:
            digits_sum += (current_number%10)
            current_number //= 10
        if digits_sum*factor == i:
            return i
    return -1

if __name__ == '__main__':
    res = find_digit_product_match()
    print(res)
