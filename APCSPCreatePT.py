grades = []
num = 0
gpa = 0
grade_cred = [] # initializes variables
total_cred = 0
apgrades = []
apgrade_cred = []

def reset(ans):
    global grades, grade_cred, num, gpa, total_cred, apgrades, apgrade_cred
    grades = []
    num = 0
    gpa = 0
    grade_cred = []
    total_cred = 0 # resets variables for next round
    apgrades = []
    apgrade_cred = []
    
    ans = ans.lower()
    
    if ans == "yes":
        print("\nCalculating again...\n") # resets if yes
        main_code(input("Do you take AP/IB/Honor classes? (yes or no)"))
    else:
        print("\nClosing...") # closes program if no

def main_code(aps):
    global grades, grade_cred, num, gpa, total_cred, apgrades, apgrade_cred
    aps = aps.lower()
    num = int(input("How many classes do you take? (a number)")) 
    # asks general info about number of classes & aps
    if aps == "yes":
        aps = int(input("How many AP/IB/Honor classes did you take?"))
        if aps > num:
            print("Uh oh! You added more honors classes then your total amount of classes.")
            reset(input("Do you want to calculate again? (yes or no)")) 
        else:
        
            for x in range (aps):
                temp = ""
                temp = input("What grade did you get in AP/IB/Honor class " + str(x+1) + "? (A, B, C, D, or F)") 
                temp = temp.upper() # asks for ap grades
                apgrades.append(temp)
            
            for y in range(aps):
                if apgrades[y] == "A": # calculate ap grade weighting
                    apgrade_cred.append(int(5))
                elif apgrades[y] == "B":
                    apgrade_cred.append(int(4))
                elif apgrades[y] == "C":
                    apgrade_cred.append(int(3))
                elif apgrades[y] == "D":
                    apgrade_cred.append(int(2))
                else:
                    apgrade_cred.append(int(0))
            if aps < num:
                for x in range(num-aps):
                    temp = ""
                    temp = input("What grade did you get in regular class " + str(x+1) + "? (A, B, C, D, or F)")
                    temp = temp.upper()
                    grades.append(temp) # if still regular classes, calculate those weights
                for y in range(num-aps):
                    if grades[y] == "A":
                        grade_cred.append(int(4))
                    elif grades[y] == "B":
                        grade_cred.append(int(3))
                    elif grades[y] == "C":
                        grade_cred.append(int(2))
                    elif grades[y] == "D":
                        grade_cred.append(int(1))
                    else:
                        grade_cred.append(int(0))
        grade_cred = grade_cred + apgrade_cred   
        for z in range(num): # calculate gpa
            total_cred = total_cred + grade_cred[z]
        gpa = total_cred/num    
        print("Your gpa is " + str(gpa) + ".")       
    else: 
        for x in range(num):
            temp = ""
            temp = input("What grade did you get in class " + str(x+1) + "? (A, B, C, D, or F)")
            temp = temp.upper()
            grades.append(temp) # if only regular, ask for those grades
        
        for y in range(num): # calculate the weights for regular classes
            if grades[y] == "A":
                grade_cred.append(int(4))
            elif grades[y] == "B":
                grade_cred.append(int(3))
            elif grades[y] == "C":
                grade_cred.append(int(2))
            elif grades[y] == "D":
                grade_cred.append(int(1))
            else:
                grade_cred.append(int(0))
        
        grade_cred = grade_cred + apgrade_cred   
        for z in range(num):
            total_cred = total_cred + grade_cred[z] # calculate gpa
        gpa = total_cred/num    
        print("Your gpa is " + str(gpa) + ".")       
         
    
    reset(input("Do you want to calculate again? (yes or no)")) # ask to run again
    
main_code(input("Do you take AP/IB/Honor classes? (yes or no)"))

