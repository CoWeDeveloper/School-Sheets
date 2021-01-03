#!/usr/bin/env python
# coding: utf-8

# In[ ]:


stuName  = input("Enter the student name :")

sub      = ["English","Chemistry","Calculus  ","Physics","Islamiat"]
markObt  = []
percent  = []
totMarks = [100, 100, 100, 100,100]
totpercent = 0

for i in range(len(sub)) :
    print(f"enter the marks of {sub[i] }")
    marks = int(input())
    markObt.append(marks)
    percent.append((marks/100)*100 )
    
Stdpercent = 0
for i in range(5):
    Stdpercent += percent[i] #75+65+98 =?? 

totpercent  = Stdpercent/len(percent)

grade = "k"
if (totpercent >80):
    grade = "A+"

elif (totpercent >70):
    grade = "A"    
elif (totpercent >60):
    grade = "B"    
elif (totpercent >50):
    grade = "C"
elif (totpercent >40):
    grade = "E"    
else:
    grade = "F"    
    



print("*************** Marks Sheet ****************")
print("STUDENT NAME : ",stuName)
print("STUDENT GRADE : ",grade )
print("TOTAL PERCENTAGE : ",totpercent)
print("\n ********************************************")  
print("\t\t Subject \t\t Marks Obtained \t\t Total Marks \t\t Percentage  ")
print("\n**********************************************************************************************************")
for i in range(len(sub)):
    print(f"\t\t{sub[i]} \t\t {markObt[i]} \t\t \t\t  {totMarks[i] } \t\t\t {percent[i] } ")


# In[ ]:


# Q:7 make attendance sheet of students for 5 students and 5 subjects containing students attendance ,
# roll numbers and total days are 15 print their attendance percentages and if less than 75% print you are
# not eligible to appear in exam-. you can use lists ,arrays,loops , conditional statements . use any raw
# data where necessary. [10]

# Note:take roll numbers data as your roll-number and next 4 roll numbers like your roll-number is 8 then
# roll-numbers data will be 8,9,10,11,12.
students      = ["arif", "ali", "ahmed"]
subjects      = ["islamic", "Calculs", "English"]
Roll_no       = ["61", "42", "62"]
days          = []
percent       = []
allResult = []

for i in range (len(students)):
    print("No. of days ",students[i], " was present")
    stdday = int(input(""))
    days.append(stdday)
    percent.append(int((stdday/15)*100))

    
result = "" 
for i in range(len(students)):
    if   (percent[i] > 75):
        result= "eligible for exam"
        allResult.append(result)
    elif (percent[i] < 75):
        result= "ineigible for exam"
        allResult.append(result)

print("\n********************Attendence Sheets********************\n")                

print(" Students Name \t : \t Subject : \t Roll No \t : \t Days \t : \t Percent \t :\t Result \t")
   
                

for i in range(len(students), ):
    print(f" {students[i]}\t\t\t {subjects[i]} \t {Roll_no[i]} \t\t\t {days[i]} \t\t {percent[i]}% \t\t    {allResult[i] }")
    
    
    
    
#     print (": "+ students[i] + " "*(14-len(students[i]))+": " +subjects[i] + " "*(7-len(subjects[i]))+" : " 
#            + Roll_no[i] + " "*(8-len(Roll_no[i]))+": " + str(days[i]) + " "*(5-len(str(days[i])))+ ": " 
#            +  str(percent[i])+ "%" +" "*(7-len(str(percent[i])))+": "+ allResult[i] )
    


# In[ ]:


print('i will make your mark sheet but before making it,i need to know your marks ')
Math = input('please type your marks Math ')
English = input('please type your marks English ')
Chemistry = input('please type your marks Chemistry ')
Physic = input('please type your marks Physic ')
Biology = input('please type your marks Biology ')
print('your marksheet is ready')
print('Math = ' + Math)
print('English = ' + English)
print('Chemistry = '+ Chemistry)
print('Physic = '+ Physic)
print('Biology = '+ Biology)
Total = int(Math) + int(English) + int(Chemistry) + int(Physic) + int(Biology)
print('Total marks = ' + str(Total))
Percentage =(Total/500)*100
print('% ' + str(Percentage))
if Total > 400 :
    print('your Grade is A+')
elif Total > 300 :
    print('your Grade is A')
elif Total > 200 :
    print('your Grade is B')
elif Total > 100 :
    print('your Grade is C')
else:
    print('you fail')


# In[ ]:


library = {
"fiction" : {
        "a" : "comedy",
        "b" : "graphic-novel",
        "c" : "science-fiction",
        "d" : "fastasy",
        "f" : "histroy-fastasy",
    },
"non_fiction" : {
        "f" : "histroy and geography",
        "g" : "arts",
        "h" : "sicence and technology",
        "i" : "other"
    }
    } 
q1 = input("enter the genra fiction or non-fiction : ")
if (q1 == "fiction" ):
    print(  
        "chose your genra \n"
        "a : comedy \n"
        "b : graphic-novel  \n"
        "c : science-fiction \n"
        "d : fastasy \n"
        "f : histroy-fastasy \n"
    )
    q2 =input("enter the genra : ")
    for key,value in library["fiction"].items():
        if ( q2 ==key):
            print("here is your "+value+ " book have a great day!")
elif (q1 =="non-fiction" ):    
    print(
          "chose your genra \n"
          "f : histroy and geography \n"
          "g : arts \n"
          "h : sicence and technology \n"
          "i : other \n"
    )
    q2 =input("enter the genra")
    for key,value in library["non_fiction"].items():        
        if ( q2 ==key):            
            print("here is your "+value+ " book have a great day!")
else:
    print("sorry there is no such book avaliable, come again!")


# In[ ]:


name = input("Enter the word or sentence " ).strip().replace(" ","")
vowels = 0 
consonant = 0

for i in name :
    if ( i == "a" or i == "e" or i == "i" or i == "o" or i== "u"  ):
        vowels +=1
    
    else:
        consonant +=1
    
print ("vowels :" , vowels)
print ("consonant:", consonant)
print ("length:",len(name))


# In[ ]:


a = input("enter")
num = 0
for i in a:
    if i in "aeiou":
        num+=1
        print(i,num)
        
print(a)


# In[ ]:


test_str = input("enter")

 
print("The original string is : " + test_str) 

res = [] 
for ele in range(len(test_str)): 
    if test_str[ele] in "aeiou": 
        res.append(ele) 
 
    
print("The vowel indices are : " + str(res)) 

