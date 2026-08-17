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


    importance=model.feature_importances_ *100
    
    print("This importance  data",importance)

    # step 6  Model prediction
    Y_Pred=model.predict(X_test)

    # print("Y PRed",Y_Pred)
    # print("Y_test is :")
    # print(Y_test.values)

    # print("Predicted ANswer are",Y_Pred)
    # print("Acutally Answer are",Y_test)

    #Step 7 Accuarcy 
   
    iCount=0
    # print(Y_test[0].values)
    Data=[]
    for i in range(len(Y_test.values)):
         if(Y_test.values[i]!=Y_Pred[i]):
             iCount=iCount+1
           

    print(iCount)
    # print(len(Y_Pred))

    acc=((iCount/len(Y_Pred))*100)
    accOrignal=accuracy_score(Y_test,Y_Pred)*100

    print("This Manually ",acc)
    print("This is ORiginal",accOrignal)










def main():
    Performace("student_performance_ml.csv")



if __name__=="__main__":
    main()
