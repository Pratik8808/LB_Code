
import pandas as pd
import matplotlib.pyplot as plt

def studentperf(Datapath):

        Border="-"*30
        print(Border)
        print("Step 1 load the data")
        print(Border)
    
        df=pd.read_csv(Datapath)

        studyhours=df["StudyHours"]
        PreviousScore=df["PreviousScore"]

        plt.scatter(df.index,df["StudyHours"],color="blue",marker="o", label="Study Hours")
        plt.scatter(df.index,df["PreviousScore"],color="red",marker="X", label="Study Hours")



        plt.title("Study Hour vs Previous Score")
        plt.xlabel("StudyHours")
        plt.ylabel("Previous Score")
        plt.show()






    

    


        
    
    

     







def main():
    studentperf("student_performance_ml.csv")

if __name__=="__main__":
    main()