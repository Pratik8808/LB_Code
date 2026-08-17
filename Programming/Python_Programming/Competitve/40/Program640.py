import sklearn.tree
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def Performace(Datapath):
    #Step1 load data
    df=pd.read_csv(Datapath)

    #Step 2 clean Data
    df.dropna()

    #Step 3  Independent and Indepedent
    X=["Attendance","StudyHours","PreviousScore","AssignmentsCompleted"]
    Y=["FinalResult"]

    x=df[X]
    y=df[Y]

    #Step 4 Spilt the Data
    X_train,X_test,Y_train ,Y_test=train_test_split(x,y,train_size=0.6,random_state=40)


    #Step 5 Train The Model
    model=DecisionTreeClassifier()




    model.fit(X_train,Y_train)



    # step 6  Model prediction
    Y_Pred=model.predict(X_test)

  
    Data=[]
    iCount=0
    for i,v in Y_test["FinalResult"].items():
        if(v!=Y_Pred[iCount]):
            print(i,":",Y_Pred[iCount])
            Data.append(i)

        iCount=iCount+1

    print(Data)


    for i,v in Y_test["FinalResult"].items():
        print(i," ",v)

     
    print(Y_Pred)
 
      

    














def main():
    Performace("student_performance_ml.csv")



if __name__=="__main__":
    main()
