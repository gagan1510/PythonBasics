text_to_insert = input("Enter the text to be inserted: ")

f = open('poem.txt', 'w')

f.write(text_to_insert)

f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end="")

f.close()