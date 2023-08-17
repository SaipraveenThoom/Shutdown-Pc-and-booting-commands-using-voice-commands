# Importing required modules
# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# importing os module
import os
import ctypes
import sys
import time




# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening........')
        r.adjust_for_ambient_noise(source)

        r.pause_threshold = 0.7

        # storing audio/sound to audio variable
        audio = r.listen(source, phrase_time_limit=2)


        try:
            # print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)

            print("Say that again sir")
            Speak("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    import time
    time.sleep(2)
    return Query


# creating Speak() function to giving Speaking power
# to our voice assistant
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()

print("What can i do for u sir Booting Setup or Shutdown Operations")
Speak("What can i do for u sir Booting Setup or Shutdown Operations")

while True:
    command = take_commands()
    if "Exit" in command:
        exit()


    if "shutdown " in command:
        Speak("Which operation would you like to perform from below")
        Speak("Say option number")
        print("Which operation would you like to perform from below:")
        print("1.Shutdown")
        print("2.Immediate shutdown")
        print("3.Restart")
        print("4.Sign out")
        print("5.Hibernate")
        print("6.Cancel Shutdown")
        print("7.Cancel Restart")
        print("8.Exit")
        command1 = take_commands()
        if "2" in command1:
            Speak("ok sir i will shutdown immediately")
            os.system("shutdown /p")
            break

        if "6" in command1:
            os.system("shutdown /a")
            Speak("ok sir i will abort shutting down")
            break
        if "1" in command1:
            Speak("Do you like to add time sir")
            print("Yes/No")
            command2 = take_commands()
            if "yes" in command2:
                Speak("can u specify time in seconds")
                command3 = take_commands()
                Speak("Thank u sir I will shut down the computer in " + command3 + "seconds")
                print("Thank u sir I will shut down the computer")
                os.system("shutdown /s /t " + command3)
                break

            if "no" in command2:
                Speak("ok sir i will shutdown in a minute")
                os.system("shutdown /s /t 60")
                break


        if "3" in command1:
            Speak("Do you like to add time sir")
            print("Yes/No")
            command4 = take_commands()
            if "yes" in command4:
                Speak("can u specify time in seconds")
                command5 = take_commands()
                Speak("Thank u sir I will restart the computer in" + command5 + "seconds")
                print("Thank u sir I will restart the computer in" + command5 + "seconds")
                os.system("shutdown /r /t " + command5)

            if "no" in command4:
                Speak("The computer will restart")
                print("The computer will restart")
                os.system("shutdown /r /t 120")
        if "7" in command1:
            Speak("The computer will cancel the restart command")
            print("The computer will cancel the restart command")
            os.system("shutdown /a ")
            break

        if "5" in command1:
            Speak("The computer will hibernate")
            print("The computer will hibernate")
            os.system("shutdown /h ")
            break

        if "6" in command1:
            Speak("The computer will cancel the above command")
            print("The computer will cancel the above command")
            os.system("shutdown /a ")
            break

        if  "4" in command1:
            Speak("The computer will sign out")
            print("The computer will sign out")
            os.system("shutdown /l ")
            break

        if "8" in command1:
            #Speak("ok sir I will exit")
            #print("ok sir I will exit")
            break




    if "booting setup" in command:
        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if is_admin():
            Speak("What Operation do you like to perform in booting setup from below")
            print("What Operation do you like to perform in booting setup from below:")
            print("1.onetimeadvancedoptions")
            print("2.bootlog")
            print("3.bootmenupolicy")
            print("4.ems")
            print("5.bootstatuspolicy")
            print("6.enum")
            print("7.sos")
            print("8.lastknowngood")
            print("9.nocrashautoreboot")
            print("10.safeboot network")
            print("11.safeboot minimal")
            print("12.safebootalternateshell")
            print("13.bootuxdisabled")
            print("14.graphicsmodedisabled")
            print("15.timeout")
            print("16.Exit")
            command1 = take_commands()
            if "1" in command1:
                Speak("Do you like to switch onetime advanced options On or Off")
                print("Do you like to switch onetime advanced options On or Off")
                command2 = take_commands()
                if "on" in command2:
                    os.system("bcdedit /set onetimeadvancedoptions on")
                    time.sleep(10)
                    break
                if "off" in command2:
                    os.system("bcdedit /set onetimeadvanncedoptions off")
                    time.sleep(10)
                    break

            if "2" in command1:
                Speak("Do you like to switch bootlog On or Off")
                print("Do you like to switch bootlog On or Off")
                command3 = take_commands()
                if "on" in command3:
                    os.system("bcdedit /set bootlog on")
                    time.sleep(10)
                    break
                if "off" in command3:
                    os.system("bcdedit /set bootlog off")
                    time.sleep(10)
                    break

            if "3" in command1:
                Speak("Do you like to switch bootmenupolicy to Standard or Legacy")
                print("Do you like to switch bootmenupolicy to Standard or Legacy")
                command4 = take_commands()
                if "Standard" in command4:
                    os.system("bcdedit /set bootmenupolicy Standard")
                    time.sleep(10)
                    break
                if "Legacy" in command4:
                    os.system("bcdedit /set bootmenupolicy Legacy")
                    time.sleep(10)
                    break

            if "4" in command1:
                Speak("Do you like to switch EMS on or off")
                print("Do you like to switch EMS on or off")
                command5 = take_commands()
                if "on" in command5:
                    os.system("bcdedit /set ems on")
                    time.sleep(10)
                    break
                if "off" in command5:
                    os.system("bcdedit /set ems off")
                    time.sleep(10)
                    break

            if "5" in command1:
                Speak("What would you like to display from boot status policy")
                print("What would you like to display from boot status policy")
                print("1.DisplayAllFailures")
                print("2.IgnoreAllFailures")
                print("3.IgnoreShutdownFailures")
                print("4.IgnoreBootFailures")
                print("5.IgnoreCheckpointFailures")
                print("6.DisplayShutdownFailures")
                print("7.DisplayBootFailures")
                print("8.DisplayCheckpointFailures")

                command6 = take_commands()
                if "1" in command6:
                    os.system("bcdedit /set bootstatuspolicy DisplayAllFailures")
                    time.sleep(10)
                    break

                if "2" in command6:
                    os.system("bcdedit /set bootstatuspolicy IgnoreAllFailures")
                    time.sleep(10)
                    break

                if "3" in command6:
                    os.system("bcdedit /set bootstatuspolicy IgnoreShutdownFailures")
                    time.sleep(10)
                    break

                if "4" in command6:
                    os.system("bcdedit /set bootstatuspolicy IgnoreBootFailures")
                    time.sleep(10)
                    break

                if "5" in command6:
                    os.system("bcdedit /set bootstatuspolicy IgnoreCheckpointFailures")
                    time.sleep(10)
                    break

                if "6" in command6:
                    os.system("bcdedit /set bootstatuspolicy DisplayShutdownFailures")
                    time.sleep(10)
                    break

                if "7" in command6:
                    os.system("bcdedit /set bootstatuspolicy DisplayBootFailures")
                    time.sleep(10)
                    break

                if "8" in command6:
                    os.system("bcdedit /set bootstatuspolicy DisplayCheckpointFailures")
                    time.sleep(10)
                    break

            if "6" in command1:
                os.system("bcdedit /enum")
                time.sleep(20)
                break

            if "7" in command1:
                Speak("Do you like to switch S O S on or off")
                print("Do you like to switch sos on or off")
                command7 = take_commands()
                if "on" in command7:
                    os.system("bcdedit /set sos on")
                    time.sleep(10)
                    break

                if "off" in command7:
                    os.system("bcdedit /set sos off")
                    time.sleep(10)
                    break

            if "8" in command1:
                Speak("Do you like to switch last known good on or off")
                print("Do you like to switch lastknowngood on or off")
                command8 = take_commands()
                if "on" in command8:
                    os.system("bcdedit /set lastknowngood on")
                    time.sleep(10)
                    break

                if "off" in command8:
                    os.system("bcdedit /set lastknowngood off")
                    time.sleep(10)
                    break

            if "9" in command1:
                Speak("Do you like to switch no crash auto reboot on or off")
                print("Do you like to switch nocrashautoreboot on or off")
                command9 = take_commands()
                if "on" in command9:
                    os.system("bcdedit /set nocrashautoreboot on")
                    time.sleep(10)
                    break

                if "off" in command9:
                    os.system("bcdedit /set nocrashautoreboot off")
                    time.sleep(10)
                    break

            if "10" in command1:
                Speak("Do you like to switch  safe boot with network on or off")
                print("Do you like to switch safeboot network on or off")
                command10 = take_commands()
                if "on" in command10:
                    os.system("bcdedit /set {current} safeboot network on")
                    time.sleep(10)
                    break

                if "off" in command10:
                    os.system("bcdedit /deletevalue {current} safeboot")
                    time.sleep(10)
                    break

            if "11" in command1:
                Speak("Do you like to switch  safe boot minimal on or off")
                print("Do you like to switch safeboot minimal on or off")
                command11 = take_commands()
                if "on" in command11:
                    os.system("bcdedit /set {current} safeboot minimal on")
                    time.sleep(10)
                    break

                if "off" in command11:
                    os.system("bcdedit /deletevalue {current} safeboot")
                    time.sleep(10)
                    break

            if "12" in command1:
                Speak("Do you like to switch  safe boot in alternate shell on or off")
                print("Do you like to switch safeboot alternateshell on or off")
                command12 = take_commands()
                if "on" in command12:
                    os.system("bcdedit /set safeboot minimal on")
                    os.system("bcdedit /set safebootalterrnateshell yes")
                    time.sleep(10)
                    break

                if "off" in command12:
                    os.system("bcdedit /deletevalue {current} safeboot")
                    time.sleep(10)
                    break

            if "13" in command1:
                Speak("Do you like to switch  boot ux disabled on or off")
                print("Do you like to switch bootuxdisabled on or off")
                command13 = take_commands()
                if "on" in command13:
                    os.system("bcdedit /set bootuxdisabled on")
                    time.sleep(10)
                    break

                if "off" in command13:
                    os.system("bcdedit /set bootuxdisabled off")
                    time.sleep(10)
                    break

            if "14" in command1:
                Speak("Do you like to switch  graphics mode disabled on or off")
                print("Do you like to switch graphicsmodedisabled on or off")
                command14 = take_commands()
                if "on" in command14:
                    os.system("bcdedit /set graphicsmodedisabled on")
                    time.sleep(10)
                    break

                if "off" in command14:
                    os.system("bcdedit /set graphicsmodedisabled off")
                    time.sleep(10)
                    break

            if "15" in command1:
                Speak("To how much time would you like to change the default time")
                print("To how much time would you like to change the default time")
                print("Say in Seconds")
                command14 = take_commands()
                os.system("bcdedit /timeout" + command14)
                time.sleep(10)
                break

            if "16" in command1:
                break

        else:
            # Re-run the program with admin rights
            # easygui.msgbox("check for administration rights!", title="Boot Manager")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            time.sleep(10)
