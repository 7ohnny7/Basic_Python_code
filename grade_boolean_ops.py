marks = int (input('enter test result'))

if marks < 40:
    grade = 'Unfortunately you did not pass'
    print(grade)
if marks >= 40 and marks <= 60:
    grade = 'Well done you got a Pass'
    print(grade)
if marks > 60 and marks < 80:
    grade = 'Congratulations you got a merit'
    print(grade)
if marks >= 80 and marks <= 100:
    grade = 'Congratulations, wow! you got a distinction'
    print(grade)


