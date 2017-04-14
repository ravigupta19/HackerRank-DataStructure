list_operation = []
delete_text = []
l = []
for _ in range(int(input())):
    user_input = list(input().split())
    if user_input[0] not in ['3','4']:
        list_operation.append(user_input)

    if user_input[0] == '1':
        l += [char for char in user_input[1]]
    elif user_input[0] == '2':
        k = int(user_input[1])
        delete_text.append(l[len(l)-k:])
        l = l[:-k]
    elif user_input[0] == '3':
        k = int(user_input[1])
        print(l[k-1])
    elif user_input[0] == '4':
        oper = list_operation.pop()
        if oper[0] == '1':
            k = len(oper[1])
            l = l[:-k]
        elif oper[0] == '2':
            l.append(char for char in delete_text.pop())


