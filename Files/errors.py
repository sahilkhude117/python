error_count = 0
error_lines = []

try:
    with open('server.txt', 'r') as logfile:
        for line_number, line in enumerate(logfile, start=1):
            if "error" in line.lower():
                error_count += 1
                error_lines.append(f'Line {line_number}: {line.strip()}')


    with open("error.txt", 'w') as errorfile:
        errorfile.write(f"Total 'error' occurrences: {error_count} \n\n")
        errorfile.write("Details: \n")
        errorfile.write("\n".join(error_lines))

    print("Error report created successfully in 'error.txt'!")

except FileNotFoundError:
    print("'server.txt' not found. Please make sure the file exists.")