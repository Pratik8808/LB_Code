import os
import sys
import schedule
import time

def Display(FileName):
    try:
        if not os.path.exists(FileName):
            print("File does not exist.")
            return

        if not os.path.isfile(FileName):
            print("Invalid file.")
            return

        if os.path.getsize(FileName) == 0:
            print("File is empty.")
            return

        with open(FileName, "r") as fobj:
            print("File Contents:")
            print(fobj.read())

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")

def main():
    if len(sys.argv) != 2:
        print("Invalid Arguments")
        return

    schedule.every(1).minutes.do(Display, FileName=sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()