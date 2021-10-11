#WARMUP SECTION:
##LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a > b:
            return b

        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)


##ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶

#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    x = text.split()
    if len(x) != 2:
        print("Text is not two-word string")
    else:
        if x[0][0] == x[1][0]:
            return True
        else:
            return False

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')
animal_crackers("A C D")


## MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    if n1==20:
        return True
    elif n2==20:
        return True
    elif n1+n2==20:
        return True
    else:
        return False

makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)


#LEVEL 1 PROBLEMS
## OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶

#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    new_name=''
    for i,j in enumerate(name):
        if i==0 or i==3:
            new_name += j.capitalize()
        else:
            new_name += j
    print(new_name)

old_macdonald('macdonaldm')
old_macdonald('macdonald')


##MASTER YODA: Given a sentence, return a sentence with the words reversed

#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'
#Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
#       >>> "--".join(['a','b','c'])
#       >>> 'a--b--c'
#This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

#       >>> " ".join(['Hello','world'])
#       >>> "Hello world"

def master_yoda(text):
    txt = text.split()
    new_txt=''
    for i in range(len(txt),0,-1):
        new_txt= new_txt + txt[i-1] + ' '
    print(new_txt)

master_yoda('I am home')
master_yoda('We are ready')
