# try except



def main():
    # TODO Exception
    try:
        myfile=open("banu.txt","r")
        print("success in reading file")
    except IOError:
        print("file doesn't exist")

    finally:
        print("Task Done")

if __name__ == "__main__":
    main()