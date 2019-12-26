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
with open("fuel.txt", "r") as f:
    line = f.readline()
    while line:
        module_int = int(line)
        amount =  module_int // 3 - 2
        # print(module_int, amount)
        secondary = calc_secondary(amount)
        print (amount, secondary)
        fuel += amount
        fuel += secondary
        line = f.readline()



print(fuel)

