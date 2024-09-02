# Print the pattern
i = 1
increment = 1

while i != 0:
    row = "* " * i
    print(row.strip())
    if i == 5:
        increment = -1
    i += increment
