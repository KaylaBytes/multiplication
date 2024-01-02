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
    split_value = list(str(value))
    largest_decimal = 0
    for x in range(len(split_value)):
        digit = split_value[-(x + 1)]
        try:
            if int(digit) > largest_decimal: 
                largest_decimal = int(digit)
        except ValueError:
            if largest_decimal != 0: 
                shift += x
                return str(value).replace(".", "")
            else:
                return str(value).replace(".0", "")

# potentially change to reversing the text so decimal point is more convenient

shift = 0
new_value_1 = int(value_shift(value_1))
new_value_2 = int(value_shift(value_2))

print(new_value_1)
print(new_value_2)
print(shift)

# Calculation

answer = 0
for _ in range(new_value_1):
    answer += new_value_2

if shift != 0:
    answer = str(answer)[:-shift] + "." + str(answer)[-shift:]
print(f"{value_1} x {value_2} = {answer}")


end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time}")

# add negative number support :)
# change calculation code so that it changes base and adds 0s to the end? could possibly work ngl...
# maybe make a gui for it too using tkinter? LMAOOOOO