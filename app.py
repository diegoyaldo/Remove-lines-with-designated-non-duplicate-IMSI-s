with open(input_file, 'r') as input_file:
    imsi_list = set(line.strip() for line in imsi_file.readlines())
    
with open(output_file, 'r') as output_file:
    kinds_lines = kinds_file.readlines()
    
filtered_kinds_lines = [line for line in kinds_lines if any(imsi in line for imsi in imsi_list)]
with open(output_file, 'w') as output_file:
    kinds_file.writelines(filtered_kinds_lines)

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
filter_lines(input_file, output_file)
