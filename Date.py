import time
import calendar
print(time.localtime())
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

print(calendar.isleap(2023))



def main():
    file = open("bhanu.txt","w+")
    for i in range(20):
        file.write("this is python code: %d\n"%(i))
    file.close()


if __name__ == "__main__":
    main()


def main():
    file = open("bhanu.txt","a+")
    for i in range(19,30):
        file.write("this is python code: %d\n"%(i))
    file.close()


if __name__ == "__main__":
    main()



def main():
    file = open("bhanu.txt","r")
    if file.mode == 'r':
        filecontent = file.read()
        print(filecontent)
        file.close()


if __name__ == "__main__":
    main()