def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))
    abso_num = abs(in_num - 21)
    abso_dub = abs((in_num - 21) * 2)
    if in_num > 21 :
        print("Result:",abso_dub)
    elif in_num < 21 :
        print("Result:", abso_num)
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
