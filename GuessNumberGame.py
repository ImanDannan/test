import random
              


print("Guess A number Game")
print "----------------------------"

x = raw_input(" Hello , What is your Name? ")

print  "Hello " + x + " !"
guess_number= random.randint(1,30)
print "Guess a number from 1 to 30"
counter=0
for i in range(1,100):
    try: 
      entered_number= int(input("Enter A number : "))
    except:
      print "Error not integer number"
      break
    if (entered_number == guess_number):
                      print("Great ! you have guessed the number")
                      print("No of Tries : ")
                      print counter
                      file = open('score.txt','w')
                      file.write(x +'   : ' + str(counter)+'\n' )
                      file.close()
                      break
    elif (entered_number > guess_number):
                      print("big")
                      counter=counter+1
    else:
                      print("small")
                      counter=counter+1

    


                    
                      


