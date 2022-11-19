'''
Script to Test our Tool On

Contains poor language to test if our tool is working properly
'''



man_hours = [10, 5, 4, 5, 6, 9]

for hour in man_hours:
    print("He worked for", hour, "hours")

# master and slave devices

devices = {'master' : 'COM12',
           'slave' : 'COM3'}

# print ports
for key, val in devices.items():
    if key == 'master':
        print("Master COM Port:", val)
    elif key == 'slave':
        print("Slave COM Port:", val)



# pronoun options
pronouns = {'male' : 'he/him',
            'female': 'she/her'}



