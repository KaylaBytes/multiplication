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
    while value % 1 != 0:
        shift_value = value
        print("shift value is", shift_value)
        for x in range(9): # multiplies by 10
            value += shift_value
            print(f"thingy {x}: {value}")
        shift += 1
    return int(value)

shift = 0
new_value_1 = value_shift(value_1)
new_value_2 = value_shift(value_2)

print(new_value_1)
print(new_value_2)
print(shift)

# Calculation

answer = 0
for _ in range(new_value_1):
    answer += new_value_2
answer = answer / (10 ** shift)
print(answer)

end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time}")

# add negative number support :)