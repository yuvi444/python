try:
    def hap(n):
        past=set()
        while n!=1:
            n=sum(int(i)**2 for i in str (n))
            if n in past:
                return False
            past.add(n)
        return True
    a=int(input("Enter a number"))
    print(hap(a))
except ValueError:
    print("Invalid input")
