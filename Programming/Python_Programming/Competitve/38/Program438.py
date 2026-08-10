
import pandas as pd

def studentperf(Datapath):
#Step 1:   read DataSet
    Border="-"*30
    print(Border)
    print("Step 1 load the data")
    print(Border)

    df=pd.read_csv(Datapath)
  
   
    studyHours=df["StudyHours"]
    sum=0
    count=0
    for i in studyHours:
        sum+=i
        count+=1

    Average=sum /count
    print(Average)

    Attendance=df["Attendance"]
    result=Attendance.mean()
    print("Attendacne",result)

    #Q3 max
    Max=df["PreviousScore"]
    Largest=0
    for i in Max:
        if(Largest<i):
            Largest=i
    print(Border)
    print("Largest from Previous",Largest)
    print(Border)

    print(Border)
    SleepHour=df["SleepHours"].min()
    print("Minium Sleep hours",SleepHour)
    print(Border)

    #Q4
    print(Border)
    Result=df["FinalResult"].value_counts(normalize=True)
    print(Result)
    print("perentage of passed student",Result[1]*100)
    print("Percentage of failed  student",Result[0]*100)
   # Reasonable Balanced dataset has 60 pass and 40 failed not balanced completely eg(50,50)
     
    print(Border)



    #Q5

    




    




    

    


        
    
    

     

    # print(df.shape)





def main():
    studentperf("student_performance_ml.csv")

if __name__=="__main__":
    main()