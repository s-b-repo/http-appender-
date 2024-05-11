# Read the content of the file
with open('input.txt', 'r') as file:
    data = file.readlines()

# Function to convert the format
def convert_format(ip_port):
    ip, port = ip_port.split(':')
    ip_parts = ip.split('.')
    new_ip = f'http {int(ip_parts[0])}.{int(ip_parts[1])}.{int(ip_parts[2])}.{int(ip_parts[3])}'
    new_port = f'    {int(port)}'
    return f"{new_ip}{new_port}\n"

# Convert the formats for each line
converted_data = [convert_format(line.strip()) for line in data]

# Write the converted data to a new file
with open('output.txt', 'w') as file:
    file.writelines(converted_data)
