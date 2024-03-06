import datetime
import spherov2
import pyttsx3
import wave
import time



from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI

toy = scanner.find_toy()
with SpheroEduAPI(toy) as droid:
    droid.spin(360, 1)

# if datetime.datetime.now()
tea = input("Enter a Tea name:  ")
print(tea)

# timevar = input("Enter when you want to brush your teeth(0-24): ")

x = datetime.datetime.now()

print(x.strftime("%I")) 
print(x.strftime("%M"))
print(x.hour, x.minute)

if x.hour == 9 or x.hour == 21 or x.hour == x.hour  and x.minute < 50:
    print(x.hour, x.minute)

    time.sleep(1)
    toy = scanner.find_toy()
    with SpheroEduAPI(toy) as droid:
        
        droid.spin(360, 1)
        print("Spiders")

        print("Hello, please turn me to the right to continue continue with the brushing buddy")

        droid.play_matrix_animation( 1, True)

        rollright = 1



        # buttongo = input("enter left l or right r to continue:  ")

        while rollright == 1:

            buttongo = input("enter left l or right r to continue:  ")

            if buttongo == 'r':
                rollright = 2
            elif buttongo == 'l':
                rollright =  0
            else:
                rollright = 1

        print("cat dogs")

        if rollright == 2:
            print("continue time")

