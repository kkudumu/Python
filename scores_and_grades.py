#Generate ten scores between 60 and 100
#Print grade with score

import random
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...

def scores_and_grades(): #defining a function
  for i in range(0, 10): #running a loop 10 times
    score = random.randint(60, 100) # choosing a random number between 60 and 100
    if score >= 90:                 #checking random int
      print "Score:", score, "Your grade is A"
    elif score >= 80:               #checking random int
      print "Score:", score, "Your grade is B"
    elif score >= 70:
      print "Score:", score, "Your grade is C"
    elif score >= 60:
      print "Score:", score, "Your grade is D"
    elif score >= 50:
      print "Score:", score, "YOU DID NOT PASS!!!" #statement for failing grade
      
  print "End of the program.  Bye!" #signal that program is done.

scores_and_grades() #return defined function