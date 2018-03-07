def push(num):
    global top
    global stack

    if top == 5:
        print("Stack overflow!")

    elif top == -1:
        top = 0
        stack[top] = num
        print("{} pushed".format(stack[top]))

    else:
        top += 1
        stack[top] = num
        print("{} pushed".format(stack[top]))

    return

def pop():
    global top
    global stack

    if top == -1:
        print("Stack underflow!")

    elif top == 0:
        v = stack[top]
        top -= 1
        print("{} popped".format(v))

    else:
        v = stack[top]
        top -= 1
        print("{} popped".format(v))

    return

stack = [0,0,0,0,0,0,0,0]
top = -1
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
pop()
pop()
pop()
pop()
pop()
pop()
pop()
pop()