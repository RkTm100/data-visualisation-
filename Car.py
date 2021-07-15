


class Car:
    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.company=company
        self.model=model
        self.speedlimit=speedlimit

    def start(self):
        print("started")


    def stop(self):
        print("stopped")



    def accelerate(self):
        print("accelerating")

audi=Car("a6","red","audi","80")
print(audi.color)
    
    

