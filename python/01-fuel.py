import os


def calc_secondary(amount):
    secondary = amount // 3 - 2
    if secondary > 0:
        higher = calc_secondary(secondary)
    else:
        higher = 0
    if higher > 0:
        return secondary + higher
    else:
        return secondary


fuel = 0
fuel_corr = 0
python_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(os.path.dirname(python_dir), "input/01-fuel.txt")

with open(input, "r") as f:
    line = f.readline()
    while line:
        module_int = int(line)
        amount = module_int // 3 - 2
        secondary = calc_secondary(amount)
        fuel += amount
        fuel_corr += secondary
        line = f.readline()

fuel_corr += fuel
print(f"Fuel without correction: {fuel}")
print(f"Fuel with correction: {fuel_corr}")
