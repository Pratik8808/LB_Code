def main():
    robj=open("Demo.txt","r")
    Data=(robj.readlines())
    print(len(Data))
if __name__=="__main__":
    main()
