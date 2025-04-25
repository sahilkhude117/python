filename = input("Enter file name to create: ")
content = input("Enter content to write in the file")

with open(filename, 'w') as file:
    file.write(content)
print("\n Content written successfully!")

print("\n--- Reading using read()---")
with open(filename, 'r') as file:
    data = file.read()
    print(data)

print("\n--- Reading using readline() ---")
with open(filename, 'r') as file:
    file.seek(0)
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

print("\n--- Reading using readlines() ---")
with open(filename, "r") as file:
    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line.strip())