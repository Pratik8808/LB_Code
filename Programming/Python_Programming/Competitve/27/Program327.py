class Numbers:
    def __init__(self, Value):
        self.No1 = Value

    def chkPrime(self):
        if self.No1 <= 1:
            return False

        for i in range(2, self.No1 // 2 + 1):
            if self.No1 % i == 0:
                return False
        return True

    def Perfect(self):
        sum = 0
        for i in range(1, self.No1):
            if self.No1 % i == 0:
                sum += i

        return sum == self.No1

    def factors(self):
        print("Factors are:")
        for i in range(1, self.No1 + 1):
            if self.No1 % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.No1 + 1):
            if self.No1 % i == 0:
                sum += i
        return sum


def main():
    value = int(input("Enter a number: "))

    obj = Numbers(value)

    if obj.chkPrime():
        print(value, "is a Prime Number")
    else:
        print(value, "is not a Prime Number")

    if obj.Perfect():
        print(value, "is a Perfect Number")
    else:
        print(value, "is not a Perfect Number")

    obj.factors()

    print("Sum of Factors:", obj.SumFactors())


if __name__ == "__main__":
    main()