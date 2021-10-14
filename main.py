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
    return new_name

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
    return new_txt

master_yoda('I am home')
master_yoda('We are ready')





##ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶

#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True

def almost_there(n):
    if n >= 90 and n <= 110:
        return True
    elif n >= 190 and n <= 210:
        return True
    else:
        return False

almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)





# LEVEL 2 PROBLEMS
##FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(nums):
    counter = False

    for i in range(len(nums)-1):
        if nums[i] == 3:
            if nums[i+1] == 3:
                counter = True
                break
    return(counter)

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])





##PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    new_text = ""
    for letter in text:
        new_text += letter * 3
    return(new_text)

paper_doll('Hello')
paper_doll('Mississippi')




##BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    sum = a+b+c
    if a == 11 or b==11 or c==11:
        sum -= 10
        if (sum >21):
            return ("BUST")
        else:
            return(sum)
    else:
        if (sum >21):
            return("BUST")
        else:
            return(sum)

blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)





##SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    sum = 0
    tick = 0
    for num in arr:
        if num == 6:
            tick = 6
        if num == 9:
            tick = 9
            continue
        if tick != 6 or tick == 9:
            sum += num
    return(sum)

summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])
summer_69([])





# CHALLENGING PROBLEMS
## SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    count = 0
    check = False
    for num in nums:
        if num == 0:
            count+=1
        if num == 7:
            if count == 2:
                check = True

    return check

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])





##COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

import math
def count_prime(num):
    primeCount = 1

    for i in range(3, num+1):
        for j in range(2,math.ceil(i/2)+1):


            if i%j == 0:
                break

            if j == math.ceil(i/2):
                primeCount+=1
                break

    return primeCount

count_prime(2)
count_prime(100)
count_prime(15)