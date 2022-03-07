users = 5
userlist = ["A","B","C","D","E","F","G"]
for i in range(len(userlist)-1):
    print("start")
    print(userlist.pop(0))
    for j in userlist:
        print(j)
    print("----")
