import datetime
import spherov2
import pyttsx3
import wave
import time


print("Testing Starting...")

engine = pyttsx3.init()
engine.say("Testing Starting")
engine.runAndWait()


from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

toy = scanner.find_toy()
with SpheroEduAPI(toy) as droid:

    engine.say("Connected, Time for brush and floss")
    droid.spin(360, 1)

    # droid.play_matrix_animation()



    # if datetime.datetime.now()

    # timevar = input("Enter when you want to brush your teeth(0-24): ")

    x = datetime.datetime.now()

    # print(x.strftime("%I")) 
    # print(x.strftime("%M"))
    # print(x.hour, x.minute)

    if x.hour == 9 or x.hour == 21 or x.hour == x.hour  and x.minute < 50:
        print(x.hour, x.minute)

        # time.sleep(1)
        # toy = scanner.find_toy()
        # with SpheroEduAPI(toy) as droid:
            
        droid.spin(360, 1)

        print("Spiders")

        engine.say("Hello please turn me to the right to continue with the brushing buddy")
        # print("Hello, please turn me to the right to continue continue with the brushing buddy")
        engine.runAndWait()
        # droid.play_matrix_animation( 1, True)


        droid.set_stabilization(0)
        droid.set_front_led(Color(0, 0, 245))

        droid.set_matrix_pixel(0, 4, Color(0, 255, 0))  #0
        droid.set_matrix_pixel(0, 3, Color(0, 255, 0))  #

        droid.set_matrix_pixel(1, 5, Color(0, 255, 0))    #
        droid.set_matrix_pixel(1, 4, Color(0, 255, 0))  # #
        droid.set_matrix_pixel(1, 3, Color(0, 255, 0))  # #
        droid.set_matrix_pixel(1, 2, Color(0, 255, 0))    #

        droid.set_matrix_pixel(2, 6, Color(0, 255, 0))      #
        droid.set_matrix_pixel(2, 5, Color(0, 255, 0))    # #
        droid.set_matrix_pixel(2, 4, Color(0, 255, 0))  # # #
        droid.set_matrix_pixel(2, 3, Color(0, 255, 0))  # # #
        droid.set_matrix_pixel(2, 2, Color(0, 255, 0))    # #
        droid.set_matrix_pixel(2, 1, Color(0, 255, 0))      #


        droid.set_matrix_pixel(7, 4, Color(255, 0, 0))

        droid.set_matrix_pixel(7, 4, Color(255, 0, 0))  #0
        droid.set_matrix_pixel(7, 3, Color(255, 0, 0))  #

        droid.set_matrix_pixel(6, 5, Color(255, 0, 0))    #
        droid.set_matrix_pixel(6, 4, Color(255, 0, 0))  # #
        droid.set_matrix_pixel(6, 3, Color(255, 0, 0))  # #
        droid.set_matrix_pixel(6, 2, Color(255, 0, 0))    #

        droid.set_matrix_pixel(5, 6, Color(255, 0, 0))      #
        droid.set_matrix_pixel(5, 5, Color(255, 0, 0))    # #
        droid.set_matrix_pixel(5, 4, Color(255, 0, 0))  # # #
        droid.set_matrix_pixel(5, 3, Color(255, 0, 0))  # # #
        droid.set_matrix_pixel(5, 2, Color(255, 0, 0))    # #
        droid.set_matrix_pixel(5, 1, Color(255, 0, 0))      #

        redo = 1
        # buttongo = input("enter left l or right r to continue:  ")
        while redo == 1:

            engine.say("roll me to the right of my LED to continue, and roll me left to repeat")
            engine.runAndWait()

            rollright = 1


            while rollright == 1:

                # buttongo = input("enter left l or right r to continue:  ")
                buttongo = 't'

                test = droid.get_gyroscope()['y']
                print(test)


                if test > 160:
                    rollright = 2
                    redo = 0
                elif test < -160:
                    rollright =  0
                    redo = 1
                else:
                    rollright = 1
                
                time.sleep(.0001)



     
        print("continue time")

        engine.say("Time For Brushing, Grab Your Tooth Brush and Get Ready to brush")
        engine.runAndWait()



        redo = 1
        # buttongo = input("enter left l or right r to continue:  ")
        while redo == 1:

            engine.say("roll me to the right of my LED Start brushing, and roll me left to repeat instruction")
            engine.runAndWait()

            rollright = 1


            while rollright == 1:

                # buttongo = input("enter left l or right r to continue:  ")
                buttongo = 't'

                test = droid.get_gyroscope()['y']
                print(test)


                if test > 160:
                    rollright = 2
                    redo = 0
                elif test < -160:
                    rollright =  0
                    redo = 1
                else:
                    rollright = 1
                
                time.sleep(.0001)

        
        engine.say("Brush time! I will start playing music so you know how long to brush")
        engine.runAndWait()
