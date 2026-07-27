stack = []
def push(x):
    stack.append(x)
def pop():
    if stack:
        return stack.pop()
def peek():
    if stack:
        return stack[-1]
