def modify_txt_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        modified_lines = []
        for line in lines:
            modified_line = line.strip().replace(':', ' ').replace('http', 'http ')
            modified_lines.append(modified_line)

        file.write(' '.join(modified_lines))

# Usage
modify_txt_file('your_file.txt')
