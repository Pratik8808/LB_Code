
import pandas as pd

def studentperf(Datapath):
#Step 1:   read DataSet
    Border="-"*30
    print(Border)
    print("Step 1 load the data")
    print(Border)

    df=pd.read_csv(Datapath)
  
   
    #Q1
    print(df.shape[0])
    print(Border)

    #Q2 q3
    Count=0
    count2=0
    X=df["FinalResult"]
    for i in X:
        if(i==1):
            Count+=1
        if(i==0):
            count2+=1
    
    print("Pass Student Count is : ",Count)
    print("Failed Student  is :",count2)

    #Q3
    


        
    
    

     

    # print(df.shape)





def main():
    studentperf("student_performance_ml.csv")

if __name__=="__main__":
    main()