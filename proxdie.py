def add_http_and_replace_colon(filename):
    # Open the input file in read mode
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Open a new file to write the modified lines
    with open('output.txt', 'w') as file:
        for line in lines:
            modified_line = 'http ' + line + line.replace(':', ' ')
            file.write(modified_line)

    print('Lines modified with http and colon replaced with space, saved to output.txt')

# Call the combined function with the file name as argument
add_http_and_replace_colon('input.txt')
