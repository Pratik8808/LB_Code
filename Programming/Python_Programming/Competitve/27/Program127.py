class BookStore:
    NoofBooks=0

    def __init__(self,Value1,Value2):
         self.Name=Value1
         self.Author=Value2
         BookStore.NoofBooks=BookStore.NoofBooks+1
   
    def Display(self):
        result = self.Name + "by" + self.Author + "No of Books" + str(BookStore.NoofBooks)
        print(result)





def main():
    dobj=BookStore("C","Dennis  Richi")
    dobj.Display()
    dobj2=BookStore("C++","strandstop")
    dobj2.Display()
 
    
    
    

if __name__=="__main__":
    main()   