### шаблон удаления скобок
# использование стека

# s = input()
def ss(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            else:
                stack.pop()

    if len(stack)!= 0:
        return False
    return True
if ss(s):
    print("YES")
else:
    print("NO")