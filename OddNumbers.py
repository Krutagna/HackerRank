def evenOdd(maxNum):
    # Start with empty lists for even and odd numbers
    evens = []
    odds = []

    # Loop through every integer up to the input maxNum
    for num in range(1, maxNum + 1):
        # Test if the number is even
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    print("Evens:", evens)
    print("Odds:", odds)
def __getDecDigit(digit):
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x

decNum = 0
    power = 0decNum = 0
    power = 0
    for digit in range(len(line), 0, -1):
        decNum = decNum + 16 ** power * __getDecDigit(line[digit-1])
        power += 1
    print (str(decNum))
    for digit in range(len(line), 0, -1):
        decNum = decNum + 16 ** power * __getDecDigit(line[digit-1])
        power += 1
    print (str(decNum))