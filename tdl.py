#Mini-Project: To-Do List Application
'''
Introduction

In this project, you will apply your Python programming skills to create a functional To-Do List Application from scratch. 
The objective of this project is to reinforce your understanding of Python syntax, data types, control structures, functions, 
and error handling while building a practical and interactive application.

1*, 2*, 3, 4, 5, 6, 7*, 8^, 9*
(* - Done)
(^ - bonus)

'''
#User Interface (UI)

#TO - DO List Features --- Right below
print("Welcome to the To-Do List App!")
tdl_list = []
status = []
print("")
print("")
print("Menu:")

print("1. Add a task")
# Adding a task with a title (by default “Incomplete”).
def addt(x):
    default = "Incomplete"
    try:
         q = str(input("Please enter the Task you want to store in the list: "))
    except ValueError:
          #Code to handle incorrect input type
          print("Please enter a valid string.")
    except Exception as e:
         #Code to handle an unexpected exception
          print(f"An unexpected error occured: {e}")
    else:
          pass
    finally:
          print("Thank you for your response.")
    
    #for status of tasks -- default
    tdl_list.append(q)
    status.append(default)
    print("The task called "+q+" has been added.")


print("2. View tasks")
# Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
def viewt(x):
    print("The tasks in the To-Do List are below with their corresponding status below that.")
    print(tdl_list)
    for i in status:
         print(i)

print("3. Mark a task as complete")
# Marking a task as complete.
def markt(x):
    c = "Complete"
    defualt = "Incomplete"
    try:
         w = int(input("Please enter 1 (for Task entered now Completed) or 2 (Incomplete): "))
    except ValueError:
          #Code to handle incorrect input type
          print("Please enter a valid integer.")
    except Exception as e:
         #Code to handle an unexpected exception
          print(f"An unexpected error occured: {e}")
    else:
          pass
    finally:
          print("Thank you for your response.")
    
    if(w == 1):
         status.pop(-1)
         status.append(c)
    else:
         status.pop(-1)
         status.append(defualt)
         
    
print("4. Delete a task")
# Deleting a task.
def deletet(x):
    try:
         q = str(input("Please enter the Task you want to Delete: "))
         if q in tdl_list:
              l = tdl_list.index(q)
              tdl_list.remove(q)
              status.pop(l)
              print("The task called "+q+" has been removed.")
         else:
              print("This task does not exist in the To-Do List. Please Try again.")

    except ValueError:
          #Code to handle incorrect input type
          print("Please enter a valid string.")
    except Exception as e:
         #Code to handle an unexpected exception
          print(f"An unexpected error occured: {e}")
    else:
          pass
    finally:
          print("Thank you for your response.")

print("5. Quit")
# Quitting the application.
def quit(x):
     print("Thank You for using this TO-DO List application. GoodBye!")
    


#User Interaction
try:
      x = 0
      y = 0
      while(x != 5):
        x = int(input("Please enter a number (1-5) of what you want to do by looking at the Menu: "))
        if(x == 1):
             addt(x)
        elif(x == 2):
             viewt(x)
        elif(x == 3):
             markt(x)
        elif(x == 4):
             deletet(x)
        elif(x == 5):
             quit(x)
             break
        else:
             print("Please enter a number 1 - 5. Please Try Again")
             break                           
      
except ValueError:
      #Code to handle incorrect input type
      print("Please enter a valid integer.")
except Exception as e:
      #Code to handle an unexpected exception
      print(f"An unexpected error occured: {e}")
else:
      pass
finally:
        print("Thank you for your response.")




