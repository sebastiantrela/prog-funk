def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

file_name = "plik.txt"
generator = read_file(file_name)

for line in generator:
    print(line)
