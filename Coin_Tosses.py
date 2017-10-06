#need to run a function 5000 times that defines head as 1 and tails as 0
#need to have heads and tails have a count that applies to each of them
import random

def coinToss(x): #defining a function
  heads = 0     # defining variables
  tails = 0
  attempt = 0
  for i in xrange(0,5000):  #for loop for a range of 5000
    toss = random.randint(0,1) #setting a random choice for heads and tails
    if (toss == 0): #deciding between heads and tails, heads = 0, tails = 1
      heads += 1 #iterating heads
      attempt += 1 #iterating the attempt number
      print ("Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far").format(attempt, tails, heads)
                    #printing with format to append variables to our string
    else:
      tails += 1
      attempt += 1
      print ("Attempt #{}: Throwing a coin... It's a tails! ... Got {} head(s) so far and {} tail(s) so far").format(attempt, tails, heads)
    if attempt == 5000:
      print ("Attempt #{}: Throwing a coin... It's a tails! ... Got {} head(s) so far and {} tail(s) so far '\n' Ending the program, thank you!").format(attempt, tails, heads) 

      
coinToss(5000) # run this 5000 times