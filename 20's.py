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
      print("You feel asleep on the train. The next and last stop on this train is Boston. Have fun getting back to the present day in Boston. ")
      boston()
    
def boston():    
    print("You just got off the train in Boston ")
    activity = input("Do you want to go to a baseball game or jazz club? ")
    if activity == "baseball game" or activity == "baseball" or activity == "b":
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
    print(user + " you want to ride a horse? Well, you decide to ride a horse to get back to the present day. You go into the dark woods when you find a two-way road. Man, it's almost like you're playing a game with how many story-dependent choices you have to make.")

    road = input("Looking both ways, do you go right or left?").lower()

    if road == "left":

      print(" I hope you know where you're going, because you chose to go left. Even if you did know where you were going, you apparently didn't read the sign that clearly said: 'Watch out for wolves.' Or maybe you did it on purpose, because what kind of person goes for a horse ride the second they unexpectedly go back in time? I think you know what happens next. You kind of deserved that.")

    elif road == "right":
      print(" Did you choose this at random, or was it because of the saying 'right is right'? Either way, you got lucky and traveled through the cartoonishly scary woods, emerging in the real world on the other side. How did this even happen? Well, you made it home.")

    else:
      print("That's not an option... can you read?")




  
while loop:
  choice = input("Do you want to go back to the present day? ").lower()
  if choice == "yes" or choice == "y":
    travel = input("To get back to the present day you have two options. You can either ride a horse or train? Which one do you prefer? ").lower()
    if travel == "train":
      train()
      loop = False
    elif travel == "horse":
      horse()
      loop = False
    else:
      print("Invalid")
      loop = False
  elif choice == "no" or choice == "nope":
    print("To stay you will have to answer all three questions correctly. If you don't answer correctly...")
    riddle = input("A sphere has three, a circle has two, a point has zero. What is it?\n A.Sides\n B.Line\n C.Dimensions\n D.All of the above\n").lower()
    if riddle == "dimensions" or riddle == "c":
      print("Lucky guess. You get to move onto the next question.")
      cereal = input("Is cereal a soup? ").lower()
      if cereal == "no":
        print("Correct, you have the right opinion. Lets see if you ecan answer the next question correctly.")
      # elif cereal == "yes" or cereal == "y":
      #   print("Really? It's not a soup. For that you are being sent to the dinosaur age, have fun with the meteor!")
        kevin = input("Who is the main character in Home Alone? ").lower()
        if kevin == "kevin":
            print("Good job " + user + " you get to stay in the 1920's. Until we see you again!")
        else:
          print("How did you mess that one up? With that you can't stay in the 1920's anymore and have to be sent back to the present day. Have a good life!")
      
        
      
      
    else:
      print("Wrong choice. Prepare to be transported back to the present day in five seconds")
   
  
      

    
    
    loop = False
  else:
    print("Invalid")
    loop = True
    





  
  

  #   print("You must complete the next 5 task correctly")
  # else
  #   print("Are you certain?")


    

    
  
  



