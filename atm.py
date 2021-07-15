class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balanceinquiry(self):
        print("Your total amount is $ 1000. ")

    def withdrawal(self,amount):
        new_amount=1000-amount
        print("you have withdrew  " + str(amount) + " ,your new balance is " + str(new_amount))

    def increase(self,amount):
        new_amount=1000+amount
        print("you have added " + str(amount) + " ,your new balance is " + str(new_amount))


def main():
    name=input("Please enter your name: ")
    print("Hello " + name + " ,welcome to Raktim International banking")
    cardnumber=input("what is your card number? : ")
    pin=input("What is your account pin number?: ")
    new_user=Atm(cardnumber,pin)

    print("please select what you would like to do today?")
    print("a, withdrawal")
    print("b,balance check")
    print("c, deposit")
    options=input("select: ")

    if options=="a":
        amount=int("How much would you like to withdrawal: ")
        new_user.withdrawal(amount)
    if options=="b":
        new_user.balanceinquiry
    if options=="c":
        fart=int(input("How much would you like to deposit: "))
        new_user.increase(fart)









main()



    
        

    