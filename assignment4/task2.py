try:
    user_content = input("Enter something to write in the file: ")

    #open file
    file = open("output.txt","w")
    file.write(user_content + "\n")
    file.close()

    file = open("output.txt","a")
    file.write("This is the appended line.")
    file.close()

    file = open("output.txt","r")
    content = file.read()
    print("Reading File content: ")
    print(content)
    file.close()

except FileNotFoundError:
    print("The file doesn't exist.")