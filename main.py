def remove_lines_starting_with_and_empty(file_path, prefix):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() and not line.startswith(prefix):
                file.write(line)

		
file_path = 'command.log'
prefix = '#@'

remove_lines_starting_with_and_empty(file_path, prefix)
