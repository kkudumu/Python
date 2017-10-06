class Bike(object):
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
    
  def displayInfo(self):
    print "The price is:", self.price 
    print "The Max Speed is:", self.max_speed
    print "The miles are:", self.miles
    return self
    
  def ride(self):
    self.miles += 10
    print "Riding", self.miles
    return self
  
  def reverse(self):
    self.miles += 5
    print "Reversing", self.miles
    return self

Bike1 = Bike(200, "25mph").ride().ride().ride().reverse().displayInfo()
Bike2 = Bike(100, "15mph").ride().ride().reverse().reverse().displayInfo()
Bike3 = Bike(50, "5mph").reverse().reverse().reverse().displayInfo()