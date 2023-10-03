

BigBoyNumbers = []

def initList():
    # Gets all the palindromic numbers
    for i in range(0,100):
       print(f"Initilizing..{i} / 999999")
       temp_list = []
       temp_revslist = []
       strI = str(i)


       for e in strI:
           temp_list.append(e)
           temp_revslist.append(e)
       temp_revslist.reverse()

       if temp_list == temp_revslist:
           BigBoyNumbers.append(int(i))




def UserNumber():
    num = int(input("Please enter your number of choice :"))
    if len(str(num)) > 20:
        print("Number entered is to long")
    else:
        return num 

def IsNumPali(EntNum):
    List = []
    ReverseList = []
    strNum = str(EntNum)

    for e in strNum:
        List.append(e)
        ReverseList.append(e)
    ReverseList.reverse()

    if List == ReverseList:
        return True

    else:
        return False

def SmallestHighPalNum(EntNum):
    BigBoyNumbers.sort()
    i = BigBoyNumbers.index(EntNum)
    print(i)

    try:
       
        if BigBoyNumbers[i] < BigBoyNumbers[i+1] and BigBoyNumbers[i+1] < BigBoyNumbers[i+2]:
            print("Smallest palindromic number that is higher than the input :",BigBoyNumbers[i+1])
            print("s")
    except:
        print(f"{EntNum} Largest number in the list")




def BigDiffPali():
    BigBoyNumbers.sort()
    i = 0
    temp = 0 

    
    for i in range(0,len(BigBoyNumbers)-1):
        Diff = BigBoyNumbers[i+1] - BigBoyNumbers[i]

        if temp < Diff:
            x = BigBoyNumbers[i+1]
            y = BigBoyNumbers[i]
            temp = Diff

    print("Largest Difference",temp)
    print(f"Between the numbers {x} and {y}")



def PaliDoesNotEqual():
    eq = 0
    neq = 0
    i = 0

    for i in range(0,len(BigBoyNumbers)):
        try:
            if BigBoyNumbers[i] + BigBoyNumbers[i+1] != BigBoyNumbers[i+3]:
                neq = neq + 1
            else:
                eq = eq + 1
        except:
            pass

    print(f"Palindormic which are not the sum of two : {neq}")
    print(f"Palindormic which are the sum of two : {eq}")





initList()
print(BigBoyNumbers)
Flag = True 
while Flag:
    Flag = False

    EntNum = UserNumber()
    IsNumPaliMsg = IsNumPali(EntNum)

    if IsNumPaliMsg ==  True:
        #Telling the user if the number is palindromic
        print("The number is Palindormic!")
        # Task 1
        SmallestHighPalNum(EntNum)
        # Task 2
        BigDiffPali()
        #Task 3
        PaliDoesNotEqual()

    else:
        print("The number isn't Palindormic!")



