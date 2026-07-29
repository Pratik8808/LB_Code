import os
import shutil
import schedule
import time
import datetime
import sys

def CopyFiles(Source, Destination):

    if not os.path.isdir(Source):
        print("Source directory does not exist.")
        return

    if not os.path.isdir(Destination):
        print("Destination directory does not exist.")
        return

    with open("CopyLog.txt", "a") as fobj:

        fobj.write("\n-----------------------------------\n")
        fobj.write("Time : " +
                   datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                   "\n")

        for FolderName, SubDirectory, FileNames in os.walk(Source):

            for File in FileNames:

                if File.endswith(".txt"):

                    SourcePath = os.path.join(FolderName, File)

                    try:
                        shutil.copy2(SourcePath, Destination)
                        print(File, "Copied")
                        fobj.write(SourcePath + "\n")

                    except Exception as e:
                        print("Cannot Copy :", File)

def main():

    if len(sys.argv) != 3:
        print("Usage : python Program.py Source Destination")
        return

    schedule.every(10).minutes.do(
        CopyFiles,
        Source=sys.argv[1],
        Destination=sys.argv[2]
    )

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()