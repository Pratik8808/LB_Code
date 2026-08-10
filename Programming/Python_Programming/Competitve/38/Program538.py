
import pandas as pd
import matplotlib.pyplot as plt

def studentperf(Datapath):

        Border="-"*30
        print(Border)
        print("Step 1 load the data")
        print(Border)
    
        df=pd.read_csv(Datapath)

        studyhours=df["StudyHours"]

        plt.hist(
             studyhours,
             bins=5,
             edgecolor="black",
             alpha=0.8,
             rwidth=0.9

        )
        plt.title("Study Hours")
        plt.xlabel("Hours")
        plt.ylabel("Frequency of hours")
        plt.show()






    

    


        
    
    

     







def main():
    studentperf("student_performance_ml.csv")

if __name__=="__main__":
    main()