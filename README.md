# Shutdown-Pc-and-booting-commands-using-voice-commands

To work with this Project we need to have knowledge about Booting Setup Commands and their Functions in Windows Operating System.
Iam using Python 3.8 here.

Steps to be followed:

step 1:
Install all the required packages in the IDE
I have used Pycharm.
All the requirements were mentioned in requirements.txt file

Step 2:
As per the code written,
I used Google to recognise and read out the words. So we need Internet connectivity while running this.
If an error occurs while recognising, it asks to say that again.
Inorder to run normal shutdown operations and add time frame to it, user must not have any admin rights. But to go with the booting setup, user need to provide admin privilages and run.
We need to specify the number of the command that is to be executed by the command prompt of the operating system of windows.
We can also add time to specify when the operation should proceed.

Operations that can be performed are:
without admin privilages
1.Shutdown
2.Immediate shutdown
3.Restart
4.Sign out
5.Hibernate
6.Cancel Shutdown
7.Cancel Restart

with admin privilages
1.onetimeadvancedoptions
2.bootlog
3.bootmenupolicy
4.ems
5.bootstatuspolicy
6.enum
7.sos
8.lastknowngood
9.nocrashautoreboot
10.safeboot network
11.safeboot minimal
12.safebootalternateshell
13.bootuxdisabled
14.graphicsmodedisabled
15.timeout
