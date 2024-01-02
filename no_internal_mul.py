import time

# Ask user for numbers to multiply

try:
    value_1 = float(input("value 1: ")) # first number to multiply
    value_2 = float(input("value 2: ")) # second number to multiply
except ValueError:
    print("Error: please input a real number and try again.")
    exit()

start_time = time.perf_counter()

# Shift numbers to make them integers

def value_shift(value):
    global shift
    flip_value = list(str(value)[::-1])
    print(flip_value)
    if flip_value[0] == "0":
        del flip_value[0:1]
    for x in enumerate(flip_value):
        if x[1] == ".":
            shift += x[0]
            del flip_value[x[0]]
            return "".join(x for x in flip_value[::-1])


shift = 0
new_value_1 = int(value_shift(value_1))
new_value_2 = int(value_shift(value_2))

print(new_value_1)
print(new_value_2)
print(shift)

# Calculation

def calculation(base, multiplier):
    magnitudes = [base, 1]
    magadd = magnitudes[0]
    while magadd <= multiplier:
        for x in range(base - 1):
            magadd += magnitudes[0]
        magnitudes.insert(0, magadd)

    based_number = []
    for x in magnitudes:
        total_mag = 0
        while x <= multiplier:
            multiplier -= x
            total_mag += 1
        based_number.append(total_mag)

    del based_number[0]
    based_number.append(0)

    answer = 0
    for x in enumerate(magnitudes):
        for y in range(based_number[x[0]]):
            answer += x[1]
    return answer


if new_value_1 - new_value_2 > 0:
    answer = calculation(new_value_2, new_value_1)
else:
    answer = calculation(new_value_1, new_value_2)


if shift != 0:
    answer = str(answer)[:-shift] + "." + str(answer)[-shift:]
print(f"{value_1} x {value_2} = {answer}")


end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time}")

# add negative number support :)
# maybe make a gui for it too using tkinter? LMAOOOOO
# I really gotta figure out how classes work, as I've never learnt them and they seem necessary here


# 4.5 and 3.6 took 0.0001405780203640461 seconds
# 1003 and 2819 took 0.00018717796774581075 seconds
# 23436362 and 54345342 took 0.8370736400247552 seconds
# 10212.1213 and 2839472.65925 took 4.516522707999684 seconds
# use 2839472.65925 and 10212.1213 as example in future, took too long this test