todo_list = []
def addList():
    item = input("Enter a new task:")
    todo_list.append(item)
    print(f"{item} added to the todo list")

def displayList():
    print("TODO list")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index} - {item}")  #means  1 - call a friend

def removeList():
    displayList()
    index = int(input("enter item no to remove:"))-1  #int, coz list is int also in list index no is o,1..so to covert n that range -1 s gvn

    if 0<= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"{removed_item} removed from the list")
    else:
        print("invalid input")

while True:
    print('To Do List App')
    print("1- Add to list")
    print("2- Display list")
    print("3- Remove from list")
    print("4- Exit")

    option = input("Enter the option")
    if option == '1':
        addList()
    elif option == '2':
        displayList()
    elif option == '3':
        removeList()
    elif option == '4':
        print('exit')
        break
    else:
        print("invalid")