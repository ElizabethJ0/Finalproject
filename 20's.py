import random
user = input("Enter username: ")
print(user +" you're in the 1920's")
#print("Do you want to go back to the present day?")
#choice = input("Choose Yes or No: ").lower()
#user = input("Enter username: ").lower()
loop = True
def train():
  print("You are on a train going to Boston and New York.")
  print("Do you want to stop in Boston or New York?")
  location = input("Boston or New York: ").lower()
  if location == "boston":
    boston()
  else:
      print("You feel asleep on the train. The next and last stop on this train is Boston.")
      boston()
    
def boston():    
    print("You just got off the train in Boston ")
    activity = input("Do you want to go to a baseball game or jazz club?")
    if activity == "baseball game" or activity == "baseball":
      print("You are watching the baseball and need to find a device to take you back to the present day. You do not find the device but when you look up you are hit by a baseball, instantly taking you back to the present day. ")
    else:
      print("You're in the jazz club when you are pulled on stage, now forced to play one of four instruments.")
      instrument = input("What instrument? Guitar, drums, singer, or saxophone ").lower()
      if instrument == "guitar":
        print("You were a really good guitar player so you were allowed to go back to the present day!")
      elif instrument == "drums" and "saxophone":
        print("You are horrible at playing this instrument. Everyone in the club kicks you out and you are stuck in the 1920's forever.")
      elif instrument == "singer" or instrument == "sing":
        num = random.randint(0,1)
        # print(num)
        if num == 0:
          print("The people are divided in opinion of how your performance was. Everyone that liked you wanted to send you back but the people that were unsure did not. On accident you were sent to the early 2000's and you have to stay there. ")
        else:
          print("Everyone loved your singing and tried to send you back. When being sent back something happened and you are now in year 7000.")
          
        
      else:
        print("You got kicked out of the club and are now on the streets stuck in the 1920's. ")
        
      
      
      
      
      


    
def horse():
  print("Horse")


  
while loop:
  print("Do you want to go back to the present day?")
  choice = input("Choose Yes or No: ").lower()
  if choice == "yes":
    travel = input("Do you want to use a Train or Horse to get back to the present day? ").lower()
    if travel == "train":
      train()
      loop = False
    elif travel == "horse":
      horse()
      loop = False
    else:
      print("Invalid")
      loop = False
  elif choice == "no":
    print("To stay you will have to answer all three questions correctly. If you don't answer correctly...")
    riddle = input("A sphere has three, a circle has two, a point has zero. What is it?\n A.Sides\n B.Line\n C.Dimensions\n D.All of the above\n").lower()
    if riddle == "dimensions" or riddle == "c":
      print("Lucky guess. You get to move onto the next question.")
      cereal = input("Is cereal a soup? ").lower()
      if cereal == "no":
        print("Correct, you have the right opinion. Lets see if you can answer the next question correctly.")
      else:
        print("Really? It's not a soup. For that you are being sent to the dinosaur age, have fun with the meteor!")
        
      
      
    else:
      print("Wrong choice. Prepare to be transported back to the present day in five seconds")
   
  
      

    
    
    loop = False
  else:
    print("Invalid")
    loop = True
    





  
  

  #   print("You must complete the next 5 task correctly")
  # else
  #   print("Are you certain?")


    

    
  
  



