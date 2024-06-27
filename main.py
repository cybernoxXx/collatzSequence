import random


def collatz(startingNumber):
    collatz_list = []

    # Case returning empty list
    if startingNumber < 1:
        return collatz_list
    # Case returning list with only 1 as element
    elif startingNumber == 1:
        collatz_list.append(1)
        return collatz_list

    # Adding the starting number to the list
    collatz_list.append(startingNumber)
    while True:
        # Even number
        if startingNumber % 2 == 0:
            collatz_list.append(int(startingNumber / 2))
            startingNumber = collatz_list[-1]
        # Odd number
        else:
            collatz_list.append(3 * startingNumber + 1)
            startingNumber = collatz_list[-1]
        # Checking if the sequence is ended
        if collatz_list[-1] == 1:
            break

    return collatz_list


assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

random.seed(42)

for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum  # Make sure it includes the starting number.
    assert seq[-1] == 1  # Make sure the last integer is 1.
