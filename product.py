class Product(object):
  def __init__(self, price, name, weight, brand, cost, status):
    self.price = price
    self.name = name
    self.weight = weight
    self.brand = brand
    self.cost = cost
    self.status = "For Sale"
    
  
  def sell(self):
    if self.sell == True:
      self.status = "Sold"
    return self
    
  def add_tax(self):
    self.add_tax = .20
    print "The Price of your item is", self.price, "and your tax is", (self.price * self.add_tax)
    return self
    
  def go_back(self, defective, new_in_box, opened_box):
    self.defective = defective
    self.in_box = new_in_box
    if self.defective:
      self.status = "defective"
      self.price = 0
    if self.new_in_box:
      self.status = "For Sale"
    if self.opened_box:
      self.status = "Used"
      self.price = self.price - (self.price * self.add_tax)
    return self
      
  def display_Info(self):
    print "Price:", self.price
    print "Name:", self.name
    print "Weight:", self.weight
    print "Brand:", self.brand
    print "Cost:", self.cost
    print "Status", self.status
    return self

product1 = Product(100, "Hoverboard", "5lbs", "Swagway", 80, "For Sale").display_Info()

  


  
  
      
    
    
    