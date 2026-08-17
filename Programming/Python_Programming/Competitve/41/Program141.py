
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier

def WinePrediction(DataPath):
    Border="-"*40
    #Step 1 Load The Data Set
    df=pd.read_csv(DataPath)


    print(Border)
    print(df.head())
    print("Data set loaded")
    print(Border)



    #step 2 Click Data
    df.dropna()
    # df.drop_duplicates()

    #Step 3: Spilt Data X and Y   

    X= df[
		[	
			"Alcohol",
			"Malic acid",
			"Ash",
			"Alcalinity of ash",
			"Magnesium",
			"Total phenols",
			"Flavanoids",
			"Nonflavanoid phenols",
			"Proanthocyanins",
			"Color intensity",
			"Hue",
			"OD280/OD315 of diluted wines",
			"Proline"
		]
	]
    Y=df["Class"]

  
    print(Border)
    #step 4 :Spilt the Data
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
    print("Data set Spilted Sucessfully")

    # print(X_test,"")
    print(Border)
    # Step 5 :Train the Model

    print(Border)
    model=DecisionTreeClassifier()
    model=model.fit(X_train,Y_train)
    print("Training of model")

    #Step 6 :Predict the model

    Y_Pred=model.predict(X_test)
    print("Predicition of model")


    #Step7 Accuarcy Scores
    print(Border)
    Accuarcy=accuracy_score(Y_test,Y_Pred)
    
    print("Accuracy of the model is :",Accuarcy*100)
    print(Border)
    
def main():
    WinePrediction("WinePredictor.csv")



if __name__=="__main__":
    main()




# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import (accuracy_score)

# def WineDataSet(DataPath):
	
	
# 	Border = "-"*40

# 	###
# 	## Step1 -> Add the data 
# 	###

# 	print(Border)
# 	print("Step1 -> Add the data")
# 	print(Border)


# 	df = pd.read_csv(DataPath)


# 	print(Border)
# 	print("Few Data int the data set will be:")
# 	print(df.head())
# 	print("last data of the dataset")
# 	print(df.tail())
# 	print(Border)


# 	###
# 	## Step2 -> Analysing the data
# 	###
# 	print(Border)
# 	print("Step2 -> Data Analysis")
# 	print(Border)

# 	print("Shape of dataset:", df.shape)
# 	print("Column Names:", list(df.columns))

# 	print("Missing Values per Column")
# 	print(df.isnull().sum())
# 	print(Border)



# 	###
# 	## Step3 -> Seperate the dependent variable and independent variable
# 	###

# 	print(Border)
# 	print("Step3 -> Seperate the dependent variable and independent variable")
# 	print(Border)


# 	# here we use the onl sing [] symbol then it will contain the one coloum
# 	# But for all coloums we have to add [[]]
# 	X = df[
# 		[	
# 			"Alcohol",
# 			"Malic acid",
# 			"Ash",
# 			"Alcalinity of ash",
# 			"Magnesium",
# 			"Total phenols",
# 			"Flavanoids",
# 			"Nonflavanoid phenols",
# 			"Proanthocyanins",
# 			"Color intensity",
# 			"Hue",
# 			"OD280/OD315 of diluted wines",
# 			"Proline"
# 		]
# 	]
# 	Y = df["Class"]

# 	print("Shape of independent variable:",X.shape)
# 	print("Shape of dependent variable:",Y.shape)

# 	X_train,X_test,Y_train,Y_test = train_test_split( 
# 		X,
#         Y,
#         test_size=0.2,
#         random_state=42
# 		)

# 	print("Data split successfully")


# 	###
# 	## Step4 -> build the model
# 	###

# 	print(Border)
# 	print("Step4 -> build the model")
# 	print(Border)


# 	model = DecisionTreeClassifier()

# 	print("Model build successfully")
# 	print(Border)

# 	###
# 	## Step5 -> train the model
# 	###

# 	print(Border)
# 	print("Step5 -> train the model")
# 	print(Border)

# 	model = model.fit(X_train,Y_train)


# 	print("Model is train successfully")
# 	print(Border)


# 	###
# 	## Step6 -> test the model
# 	###
# 	print(Border)
# 	print("Step6 -> test the model")
# 	print(Border)

# 	y_pred = model.predict(X_test)

# 	print("Model tested successfully")

# 	###
# 	## Step7 -> Cheak the accuracy of they model
# 	###

# 	print(Border)
# 	print("Cheakingg the accuracy of the model")
# 	print(Border)

# 	Accuracy = accuracy_score(Y_test,y_pred)

# 	print("Accuracy of the model will be:",Accuracy*100)

# 	print(Border)

# 	print("ML Pipeline will be ended")
# 	print(Border)




# def main():

# 	WineDataSet("WinePredictor.csv")

	

# if __name__ == "__main__":
# 	main()
