import schedule
import datetime
import os
import sys


def DisplayMonday():
    print("Start your weekly Goal")
def DisplayWednesday():
    print("Review Your Weekly Progress")
def DisplayFriday():
    print("Weekly Work Completed")
            
            
def main():
    schedule.every().monday.at("9:00").do(DisplayMonday)
    schedule.every().wednesday.at("17:00").do(DisplayWednesday)
    schedule.every().friday.at("18:00").do(DisplayFriday)
   

if __name__=="__main__":
    main()