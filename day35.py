title = "\033[34mTo Do List Manager\033[0m" 
print(f"{title:^60}")
print()
print ("\033[36mManage your to-do list: view, add ,edit, remove or delete\033[0m")

import os, time
toDoList = []

def view():
  print() 
  for item in toDoList:
    print(f"{item:<30}")
  print() 

while True:
  print()
  menu = input("What would you like to do? ")
  print()
  if menu == "add":
    item = input("What should I add to the to do list?: ")
    if item in toDoList:
      print(f"{item} is already in the list")
    else:
      toDoList.append(item)

  elif menu == "edit":
    item = input("What do want to edit?:  ")
    changes = input("What do you want to change it to?: ")
    for i in range(0,len(toDoList)):
      if toDoList[i]==item:
        toDoList[i]=changes
  
  elif menu == "remove":
    item = input("What should I remove from the to do list?: ")
    if item in toDoList:
      confirm = input(f"Are you sure you want to remove {item} from the list? ")
      if confirm == "yes":
        toDoList.remove(item)
      else:
        print(f"{item} was not removed")
    else:
      print(f"{item} was not in the list")

  elif menu == "view":
    print()
    print("Here is your to do list: ")

  elif menu == "delete":
    toDoList =[]
    print("List is deleted!")
  view() 
  time.sleep(2)
  os.system("clear")
  print(f"{title:^60}")