x = input('Enter the percentage obtained (eg: 40%): ')
x = x.split('%')
percentage_obtained = float(x[0])
if percentage_obtained >100:
    print('Not valid percentage')
else:
    if(percentage_obtained >= 80):
        print('Distinction')
    elif(percentage_obtained >=65):
        print('First Division')
    elif(percentage_obtained >= 55):
        print('Second Division')
    elif(percentage_obtained >= 40):
        print('Third Division')
    else:
        print('Fail')