class BankAccounts:
    ROI=10.5
    def __init__(self,Name):
        self.Amount=0
        self.Name=Name
    def display(self):
        Result="Account Holder name is"+self.Name+"Current Balance is"+str(self.Amount)
        print(Result)
    def Deposit(self):
        newAmount=int(input("Enter the Amount"))
        self.Amount=self.Amount+newAmount

    def withDraw(self):
        newAmount=int(input("Enter the Amount to WithDraw"))
        if(newAmount>self.Amount):
            print("WithDraw Amount is greater than balance no overdraft avaiable")
            return

        self.Amount=self.Amount-newAmount
        print("Avaiable balance is ",self.Amount)
    def CalculateInterest(self):
        Interest=(self.Amount *BankAccounts.ROI)/100
        return Interest


def main():
    Bobj= BankAccounts("Pratik")
    Bobj.Deposit()
    Bobj.display()
    Bobj.withDraw()
    Ret = Bobj.CalculateInterest()
    print(Ret,"Interset")
             
if __name__=="__main__":
    main()
        

        
