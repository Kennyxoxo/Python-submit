try:
    file = open("sample.txt","r")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")