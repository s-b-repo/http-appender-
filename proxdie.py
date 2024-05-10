# Open the input file in read mode
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Open a new file to write the modified lines
with open('output.txt', 'w') as file:
    for line in lines:
        file.write('http ' + line)

print('Lines modified and saved to output.txt')
