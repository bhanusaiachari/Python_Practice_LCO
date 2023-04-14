import Course_Helper


def main():
    print("*" * 40)
    print("*\n:: COURSE MANAGEMENT :: \n")
    print("*" * 40)
    print("\n")

    db = Course_Helper.DatabaseManage()

    print("#" * 40)
    print("\n :: User Manual ::\n")
    print("#" * 40)

    print('\n Press 1.Insert a new Courses')
    print('\n Press 2. Show all Courses')
    print('\n Press 3. Delete a course (NEED ID OF COURSE)\n')
    print("#" * 40)
    print("\n")

    choice = input("\n Enter a choice: ")
    if choice == "1":
        name = input("\n Enter Course name: ")
        description = input("\n Enter Course description: ")
        price = input("\n Enter Course price: ")
        private = input("\n Is this course private(0/1): ")
        if db.insert_data([name, description, price, private]):
            print("Course was inserted successfully")
        else:
            print("OOPS!!!!!!!!!!!!!! Course was not inserted successfully")
    elif choice == "2":
        print("\n :: Course List :: \n")
        for index, item in enumerate(db.fetch_data()):
            print("\n SL NO: " + str(index + 1))
            print("\n Course ID: " + str(item[0]))
            print("\n Course Name: " + str(item[1]))
            print("\n Course desc: " + str(item[2]))
            print("\n Course Price: " + str(item[3]))
            private = 'Yes' if item[4] else 'NO'
            print("\n is private " + private)
            print("\n")
    elif choice == "3":
        record_id = input('Enter course ID:')
        if db.delete_data(record_id):
            print("Course was deleted successfully")
        else:
            print("OOps Something went wrong!!")
    else:
        print("BAD CHOICE")


if __name__ == '__main__':
    main()
