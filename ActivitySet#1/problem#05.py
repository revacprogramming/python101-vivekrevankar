score = input("Enter Score: ")
score = float(score)
if score>0 and score<1:
    if score >= 0.9:
        print("A grade")
    elif score >= 0.8:
        print("B grade")
    elif score >= 0.7:
        print("C grade")
    elif score >= 0.6:
        print("D  grade")
    elif score < 0.6:
        print("F grade")
else :
    print("the entered score is out of range")




