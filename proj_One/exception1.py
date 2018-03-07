try:
    text = input("Enter a text: ")
except EOFError:
    print("You did an End of file")
except KeyboardInterrupt:
    print("You cancelled the operation")
else:
    print("You entered: {}".format(text))