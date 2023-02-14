user = input("Enter username: ")
print(user +" you're in the 1920's")
#print("Do you want to go back to the present day?")
#choice = input("Choose Yes or No: ").lower()
#user = input("Enter username: ").lower()
loop = True
def train():
  print("You are on a train going to Boston or New York. Do you want to go to Boston or New York? ")
  location = input("Boston or New York ").lower()
  if location == "boston":
    print("You just got off the train in Boston ")
    print("Do you want to go to a baseball game or jazz club? ")



    
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
    print("Staying")
    loop = False
  else:
    print("Invalid")
    loop = True
    





  
  

  #   print("You must complete the next 5 task correctly")
  # else
  #   print("Are you certain?")


    

    
  
  



