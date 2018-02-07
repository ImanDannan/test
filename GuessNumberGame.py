# -*- coding: utf-8 -*-
import random

"""
x= "غير معروف"
file = open('score.txt','w',encoding='utf-8')
file.write(x)
file.close()
"""               
def ArabicPrint(s):
  print s.decode('utf8')


ArabicPrint("لعبة خمن الرقم")
print "----------------------------"
x= "غير معروف"
x = raw_input("  مرحبا بك ما اسمك؟  ".decode('utf8'))
#ArabicPrint(x)

print  "أهلا ".decode('utf8') + x
guess_number= random.randint(1,30)
print "لدي رقم من 1 إلى 30 و عليك أن تحزره".decode('utf8')
counter=0
for i in range(1,100):
    entered_number= input("ادخل الرقم:".decode('utf8'))
    if (entered_number == guess_number):
                      ArabicPrint("برافو لقد حزرت الرقم")
                      ArabicPrint("عدد المحاولات")
                      print counter
                      file = open('score.txt','w')
                     # file.write(x.decode('utf8'))
                      file.write('   : ' + str(counter))
                      file.write('\n')
                      file.close()
                      break
    elif (entered_number > guess_number):
                      ArabicPrint("كبير ")
                      counter=counter+1
    else:
        ArabicPrint("صغير")
        counter=counter+1


                    
                      


