import time
import datetime
from pygame import mixer

current_time = time.strftime("%H:%M:%S")
work_start_time = '09:00:00'
work_end_time = '17:00:00'

# Water Configuration:
water_limit = 3500 # in ml
glass_size = 250 # in ml
no_of_glass = 14
total_working_time = 8*60*60 # in secs
water_interval = total_working_time/no_of_glass # seconds
water_mp3_file = 'C:\Python Prog\Healthy Programmer\water.mp3'

# Eye Configuration:
eye_interval = 30*60 # Every 30 mins
eye_mp3_file = 'C:\Python Prog\Healthy Programmer\eyes.mp3'

# Physical Configuration:
physical_interval = 45*60 # Every 45 mins
physical_mp3_file = 'C:\Python Prog\Healthy Programmer\physical.mp3'

print("Welcome to Healthy Programmer. This is developed by Virat Chauhan.\nIt will keep track of your body health!")

def music_play(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)

def water_drinking_reminder(glass):
    i = ''
    while (i != 'drank'):
        music_play(water_mp3_file)
        i = input("\nDid you drank water? If yes, reply with 'Drank'\n> ").lower()
        if i == 'drank':
            print("Good Job!")
            mixer.music.stop()
            time.sleep(water_interval)
            break

def eye_exercise_reminder():
    i = ''
    while (i != 'EyDone'):
        music_play(eye_mp3_file)
        i = input("\nDid you did eyes exercise? If yes, reply with 'EyDone'\n> ").lower()
        if i == 'eydone':
            print("Good Job!")
            mixer.music.stop()
            time.sleep(eye_interval)
            break
        
def physical_exercise_reminder():
    i = ''
    while (i != 'PyDone'):
        music_play(physical_mp3_file)
        i = input("\nDid you did physical exercises? If yes, reply with 'PyDone'\n> ").lower()
        if i == 'pydone':
            print("Good Job!")
            mixer.music.stop()
            time.sleep(physical_interval)
            break

try:
    glass = 0
    while(current_time != work_end_time):
        if current_time >= work_start_time and current_time <= work_end_time:
            if glass == no_of_glass:
                pass
            else:
                water_drinking_reminder(glass)
                glass += 1
            eye_exercise_reminder()
            physical_exercise_reminder()
            current_time = time.strftime("%H:%M:%S")

except Exception as e:
    print("Something went wrong!")