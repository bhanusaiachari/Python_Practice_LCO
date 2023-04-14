import DB_helper


def main():
    run = 1
    DB_helper.create_table()

    while run:
        print("\n")
        print('1. Insert New Task in todo List \n'
              '2. View the todo List \n'
              '3. Delete the Task  \n'
              '4. exit \n')
        x = input("choose any above options: ")

        if x == "1":
            task = str(input("enter your todo:"))
            DB_helper.data_entry(task)
        elif x == "2":
            DB_helper.printData()
        elif x == "3":
            indexToDelete = int(input("Enter the index of task to be deleted: "))
            DB_helper.deleteTask(indexToDelete)
        elif x == "4":
            run = 0
        else:
            print("Please choose valid option")
    DB_helper.closeCursor()


if __name__ == '__main__': main()
