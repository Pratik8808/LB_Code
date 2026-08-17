import sklearn.tree
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

def Performace(Datapath):
    #Step1 load data
    df=pd.read_csv(Datapath)

    #Step 2 clean Data
    df.dropna()

    #Step 3  Independent and Indepedent
    X=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
    Y=["FinalResult"]

    X=df[X]
    Y=df[Y]

    #Step 4 Spilt the Data
    X_train,X_test,Y_train ,Y_test=train_test_split(X,Y,test_size=0.6,random_state=40)

    #Step 5 Train The Model
    model=DecisionTreeClassifier(max_depth=8)

    model=model.fit(X_train,Y_train)

    

    # step 6  Model prediction
    Y_Pred=model.predict(X_test)
    print(X_test)

    # print("Predicted ANswer are",Y_Pred)
    # print("Acutally Answer are",Y_test)

    #Step 7 Accuarcy  Tesing Accuarcy
    Accuracy=accuracy_score(Y_test,Y_Pred)
    print("Testing Accuarcy  of model",Accuracy*100)

    # Training accuracy
    train_Pred = model.predict(X_train)
    train_Accuracy = accuracy_score(Y_train, train_Pred)

    print("Training Accuracy:", train_Accuracy * 100)

  
    X_Test2 = pd.DataFrame(
    [[6, 85, 66, 7, 7]],
    columns=[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
)

   
    Y_Pred2=model.predict(X_Test2)

    print(Y_Pred2[0])






def main():
    Performace("student_performance_ml.csv")



if __name__=="__main__":
    main()
