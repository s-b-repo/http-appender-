def modify_txt_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            modified_line = line.replace('http', 'http ').replace(':', ' ')
            file.write(modified_line)

# Usage
modify_txt_file('your_file.txt')
