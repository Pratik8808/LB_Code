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
    X=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
    Y=["FinalResult"]

    X=df[X]
    Y=df[Y]

    #Step 4 Spilt the Data
    X_train,X_test,Y_train ,Y_test=train_test_split(X,Y,test_size=0.6,random_state=40)

    #Step 5 Train The Model
    model=DecisionTreeClassifier()

    model=model.fit(X_train,Y_train)

    # step 6  Model prediction
    Y_Pred=model.predict(X_test)

    # print("Predicted ANswer are",Y_Pred)
    # print("Acutally Answer are",Y_test)

    #Step 7 Accuarcy 
    Accuracy=accuracy_score(Y_test,Y_Pred)
    print("Accuarcy of mode",Accuracy*100)

    #Step 8 Confusion Matrics
    cm=confusion_matrix(Y_test,Y_Pred)
    print(cm)


    display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Pass", "Fial"]
)

    display.plot()

    plt.title("Confusion Matrix")
    plt.show()







def main():
    Performace("student_performance_ml.csv")



if __name__=="__main__":
    main()
