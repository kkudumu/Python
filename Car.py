class Car(object):
  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    self.tax
    self.tax()
    self.display_all()
    
    
    
    
  def tax(self):
    if self.price >= 10000:
      self.tax = .15
    else:
      self.tax = .12
    return self
  
  def display_all(self):
    print "Price:", self.price
    print "Speed:", self.speed
    print "Fuel:", self.fuel
    print "Mileage", self.mileage
    print "Tax:", self.tax
    return self
    
  


car1 = Car(9000, "80mph", "Full", "10mpg")
car2 = Car(30000, "90mph", "Not Full", "15mpg")
car3 = Car(40000, "100mph", "Full", "20mpg")
car4 = Car(50000, "110mph", "Not Full", "25mpg")
car5 = Car(7500, "60mph", "Full", "10mpg")
car6 = Car(70000, "150mph", "Full", "35mpg")
    
    