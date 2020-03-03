import time
import os
import threading

class RadioStation:
    def __init__(self):
        super().__init__()

    def setStation(self, station):
        if (float(station) > 1000 or float(station) < 88):
             raise ValueError("Not a valid radio station")
        else:
            self.station = station
    def setVolume(self, volume):
        if (float(volume) > 10 or float(volume) < 0):
             raise ValueError("Not a valid volumw")
        else:
            self.volume = volume
    


class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                print("Current time: {}:{}:{}".format(now.tm_hour, now.tm_min, now.tm_sec))
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    if (input("BUZZ BUZZ BUZZ! Snooze? (Y/N)") == "Y"):
                        print("Snooze Alarm set to: {}:{}".format(self.hours, self.minutes+9))
                        alarm = Alarm(self.hours, self.minutes+9)
                        alarm.start()
                    else:
                        print("Alarm was shut off")
                        self.kill()
                time.sleep(1)
            time.sleep(60)
        except:
            return
    def kill(self):
        self.keep_running = False



alarm_HH = input("Enter the hour you want to wake up at: ")
alarm_MM = input("Enter the minute you want to wake up at: ")

radiostation = input("Enter the radio station: " )
volume = input("Volume? (0-10): ")
print("You want to wake up at: {}:{}".format(alarm_HH, alarm_MM), " Press Ctrl+C to stop the alarm clock")
print("The radio was turned on and is playing {} at volume {}".format(radiostation, volume))

radio = RadioStation()
radio.setStation(radiostation)
radio.setVolume(volume)
alarm = Alarm(alarm_HH, alarm_MM)
alarm.start()

try:
    while True:
         text = str(input())
         if text == "stop":
            alarm.kill()
            break
except:
    print("Alarm App Stopped")
    alarm.kill()