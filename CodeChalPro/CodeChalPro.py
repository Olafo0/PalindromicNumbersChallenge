
BigBoyNumbers = [121,1001,1234321]


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
        BigBoyNumbers.append(EntNum)
        return True

    else:
        return False

def SmallestHighPalNum(EntNum):
    BigBoyNumbers.sort()

    try:
        i = BigBoyNumbers.index(EntNum)
        if BigBoyNumbers[i] < BigBoyNumbers[i+1] and BigBoyNumbers[i+1] < BigBoyNumbers[i+2]:
            print("Smallest palindromic number that is higher than the input :",BigBoyNumbers[i+1])
    except:
        print("{EntNum} Largest number in the list")

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

    else:
        print("The number isn't Palindormic!")



