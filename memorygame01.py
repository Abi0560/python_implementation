# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import time
import collections



glob_list = collections.defaultdict(list)

def group_ana():
    print("group ana working")
    print(*glob_list.values())

def dm(message,duration):
    print(message)
    time.sleep(duration)
    

def anagram(word01,solnword,qnword,n):       
  temp1="".join(sorted(word01))
  temp2="".join(sorted(solnword))
  if len(word01) !=n :
    print("number of letters do not match")
  elif word01==qnword:
      print("U typed the same thing")            
  else:
    if temp1==temp2:  
      if word01==solnword:
          print("you are correct\ncurrent backpack is:")
          global glob_list
          glob_list[temp1].append(word01)
          glob_list[temp1].append(qnword) 
          print(*glob_list.values())
      else:
          print("u just typed random")



    

    
    
    
    
os.system('cls') 
dm("Screen cleared",5)   


dm("Start",3)
a=input("Enter your name:\n")
print(a)
j=0
i=0
print("\nlevel 1 you have to compete against a bot in a memory game ,enter the name of an animal")
print("and bot will enter next name and this process continues without repetition till you win but when you will win")
print("is a mystery , so goodluck player")
default_list = ["shark","eagle","rabbit","parrot","frog"]
lost=set()
lost.add(input("Enter first animal:\n"))
while j<12:

      if j%2==0:
          print("\nBot enters element no "+str(j+2)+":")
          if i < len(default_list):
             c = default_list[i]
             print(c)
             i += 1
             if c in lost:
              print(lost)  
              print(str(c)+" is reccuring.Bot typed the same element twice.You Win")
              break
          else:
             print("Im soryy i dont know more animal names. I give up. You win")
             break 
        
      else:
       c=input("Enter " +"Enter element no "+str(j+2)+":\n")
       if c in lost:
        print(lost)  
        print(str(c)+" is reccuring.You typed the same element twice.You lost\n")
        break

      lost.add(c) 
      j+=1
  
print("\nOver")  
dm("",5)

os.system('cls') 
dm("Screen cleared",5)   

print("LEVEL 2\n\n")

print("""An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
         typically using all the original letters exactly once. For example elbow and below""")

answord1=["below","reactive","listen","flea","enraged","admirer"]
solutionword=["elbow","creative","silent","leaf","angered","married"]

for i in range(len(solutionword)):
   word1=input("Rearrange the letters of the word  -" +answord1[i] +"-   and form another meaningful word\n")
   anagram(word1,solutionword[i],answord1[i],len(solutionword[i]))
   print("next")

print("\nhere are the words u have collected in your backpack:")
print(*glob_list.values())
print("]nYou made it\n")
os.system('cls') 
dm("Screen cleared",5)   
































 


























