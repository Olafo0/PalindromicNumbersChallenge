
#BigBoyNumbers = [121,1001,1234321]
BigBoyNumbers = [0,11,121,1221,12321,1234554321,1234567898765421,1111444444441111]




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
    i = 0

    for i in range(0,len(BigBoyNumbers)-1):




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

    else:
        print("The number isn't Palindormic!")



