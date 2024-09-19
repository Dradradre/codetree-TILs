n = int(input())
lis = []

def solution(com, num):
    if com == "push_back":
        lis.append(num)
    elif com == "get":
        print(lis[num-1])

for i in range(0,n):
    command = input()
    if command == "size":
        print(len(lis))
    elif command == "pop_back":
        lis.pop()
    else:
        command_list = list(map(str, command.split()))
        com = command_list[0]
        num = int(command_list[1])
        solution(com,num)