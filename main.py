#Author Blake cameron date 24/05/2022 Version 0.4
def question1():
  print("Hello welcome to a Quiz I made about te reo there are 15 questions about te reo")
  print("First of all what is your name")
  name = input()
  print ("Hello " + name)
  print ("okay lets begin")
  question01 = input ("Is this the correct spelling for welcome nau mai "). lower()
  if question01 == "yes" or question01 == "Yes":
   print ("Correct good job")
  else: print ("please answer yes or no")
  if question01 == "no" or question01 == "No":
    print ("wrong")

question1()

def question2():
  question01 = input ("Is this the correct spelling for english lgorgi "). lower()
  if question01 == "No" or question01 == "no":
   print ("Correct good job this is the correct spelling Ingarihi")
  else: print ("please answer yes or no")
  if question01 == "Yes" or question01 == "Yes":
    print ("wrong")

question2()


def question3():
  question01 = input ("Is this the correct spelling for danger mōrearea "). lower()
  if question01 == "Yes" or question01 == "yes":
   print ("Correct good job this is the correct danger mōrearea")
  else: print ("please answer yes or no")
  if question01 == "no" or question01 == "No":
    print ("wrong")

question3()







































































