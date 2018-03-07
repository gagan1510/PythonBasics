def enqueue(num):
    global front
    global rear
    global q

    if front == -1 and rear == -1:
        front = 0
        rear = 0
        q[rear] = num
        print("{} entered".format(q[rear]))

    elif rear == 5:
        print("queue is full")

    else:
        rear += 1
        q[rear] = num
        print("{} enqueued".format(q[rear]))

    return

def dequeue():
    global front
    global rear
    global q

    if front == rear and front == -1:
        print("Queue is empty")

    elif front == rear and front != -1:
        v = q[front]
        front = -1
        rear = -1
        print("{} dequeued".format(v))

    else:
        v = q[front]
        front += 1
        print("{} dequeued".format(v))

    return

front = -1
rear = -1
q = [0,0,0,0,0,0,0,0,0,0,0]
enqueue(1)
enqueue(2)
enqueue(4)
enqueue(7)
enqueue(1)
enqueue(2)
enqueue(4)
enqueue(7)
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()