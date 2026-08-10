
import pandas as pd

def studentperf(Datapath):
#Step 1:   read DataSet
    Border="-"*30
    print(Border)
    print("Step 1 load the data")
    print(Border)

    df=pd.read_csv(Datapath)
    print(Border)
    print(df.head())

    print("\n")
    print(df.tail())
    print(Border)


    print(df.columns)
    print(df.info)
     

    # print(df.shape)





def main():
    studentperf("student_performance_ml.csv")

if __name__=="__main__":
    main()