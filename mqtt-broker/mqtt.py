#!/usr/bin/env python3

import time
import io 
import json
import readi2c
import sys

from readi2c import readData
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.enums import PNReconnectionPolicy
from pubnub.pubnub import PubNub
 
pnconfig = PNConfiguration()
 
pnconfig.subscribe_key = 'sub-c-a57ab586-2e94-11e9-8208-aaa77ad184aa'
pnconfig.publish_key = 'pub-c-395634b8-6b43-407a-bd80-e656f030d997'
pnconfig.reconnect_policy = PNReconnectionPolicy.LINEAR
pnconfig.uuid = 'device1-custome-uuid-format'
 
pubnub = PubNub(pnconfig)
 
 
def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    print ("inside the function my_publish_callback")
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
 
 
class MySubscribeCallback(SubscribeCallback):
    def __init__(self):
      #self.f = open("/sys/class/thermal/thermal_zone0/temp", "r")
      #self.t = self.f.read().strip()
      #self.cputemp = "CPU temp "+ str(self.t)
      pass

    def presence(self, pubnub, presence):
        pass  # handle incoming presence data

    
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost
 
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc self.cputemp = "CPU temp: "+t

            pubnub.publish().channel("awesomeChannel").message("hello!!").pn_async(my_publish_callback)
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.

    def message(self, pubnub, message):
      #print(message.channel+" "+str(message.message) + "  "+ str(message.subscription) + "  "+ str(message.timetoken) +"  "+ str(message.user_metadata)+ "  "+ str(message.publisher))
      f = open("/sys/class/thermal/thermal_zone0/temp", "r")
      temperature = f.read().strip()
      f.close()
      readData()
      print(temperature)
      pubnub.publish().channel("awesomeChannel").message("current system temperature : " + str(temperature)).sync()
      time.sleep(5) 

def main():
    """run the application"""
    pubnub.add_listener(MySubscribeCallback())
    pubnub.publish().channel("awesomeChannel").message("hihello").pn_async(my_publish_callback)
    pubnub.subscribe().channels('awesomeChannel').execute()

if __name__ == '__main__':
    main()


