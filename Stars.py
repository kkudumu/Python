#create function draw stars. need to convert array to stars
y = [4, 6, 1, 3, 5, 7, 25] # Variable for Testing
def draw_stars(arr): # defining function
  for x in arr: #run through arr with var x
    print "*" * x #print stars times value of the array
    
draw_stars(y) 


z = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"] # Variable for testing
def draw_stars_2(arr): #defining function

  for x in arr: #run through array with var x
    if isinstance(x, int): #if value of x is an integer
      print "*" * x # print stars times value of array
    if isinstance(x, str): #if it is a string
      print (x[0].lower()) * len(x) #print the lowercase letter of the first value of each array item
      
    
draw_stars_2(z)

