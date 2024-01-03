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
    global neg
    flip_value = list(str(value)[::-1])
    if flip_value[0] == "0":
        del flip_value[0:1]
    if flip_value[-1] == "-":
        del flip_value[-1]
        neg += 1
    for x in enumerate(flip_value):
        if x[1] == ".":
            shift += x[0]
            del flip_value[x[0]]
            return "".join(x for x in flip_value[::-1])


shift = 0
neg = 0
new_value_1 = int(value_shift(value_1))
new_value_2 = int(value_shift(value_2))

# Calculation

def calculation(smaller, larger):
    split_small = list(str(smaller)[::-1]) # reverse smaller number to make calculation easier
    totals = []
    for x in enumerate(split_small):
        placeholder = 0
        for _ in range(int(x[1])):
            placeholder += larger
        totals.append(int(str(placeholder) + str(0) * x[0]))
    return sum(totals)


if new_value_1 - new_value_2 > 0:
    answer = calculation(new_value_2, new_value_1)
else:
    answer = calculation(new_value_1, new_value_2)


if shift != 0:
    answer = str(answer)[:-shift] + "." + str(answer)[-shift:]
if neg % 2 != 0:
    answer = "-" + answer
print(f"{value_1} x {value_2} = {answer}")


end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time}")

# maybe make a gui for it too using tkinter? LMAOOOOO
# I really gotta figure out how classes work, as I've never learnt them and they seem necessary here


# 4.5 and 3.6 took 0.0001009589759632945 seconds
# 1003 and 2819 took 0.00011400901712477207 seconds
# 23436362 and 54345342 took 0.00010792800458148122 seconds
# 10212.1213 and 2839472.65925 took 0.00013760896399617195 seconds