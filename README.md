# Smart-Accident-Detection-and-Prvention-System-using-Raspberry-pi
Welcome to the Smart-Accident-Detection-and-Prvention-System-using-Raspberry-pi wiki!

The idea of our project is to incorporate the safety measures of seatbelt detection and alcohol detection and alert message using IOT devices in vehicles to significantly reduce the risk of accidents happening.

The first being the detection mechanism. It incorporates the safety measures of seatbelt detection using IR sensors and also tests the alcohol levels in inside the car using Gas detection sensors. It then uses algorithm to test if the alcohol level is below safety limit and then allows the car to advance. Another part of our project focuses on detection of accident. Vibration sensors incorporated in IOT devices inside the car checks for unexpected vibrations and detects accidents. It then proceeds GSM module to mail emergency contacts about the situation, coordinates by GPS module and time. Thus making road driving a lot more secure.

I also added the false alarm to the system so that if any case we can say that the accident is false by switching ON it. I made the code in order to work faster and first priority is for accident detection .Since the project is wired in the car, our project is secured and the message sending security is depending on the telecommunication. The results of all the sensors are accurate if in the position implemented.

# Applications:

• Can be useful in detecting the accident locations to send immediate medical help, if necessary.
• Details of drunken driving can be sent to concerned family, so that they can take appropriate action.
• Detection of seat belt system might be really helpful in avoiding fatal injuries when an accident might occur.
• With active location tracking, it would not be a problem to detect where the accident took place or the location where any drunken driving instances occur.


# Proposed Methodology:
### I am using proteus software in this project, which can show the simulation type of the it.

First our program will analyze the whether accident detected or not by vibration sensor condition so then we can check for the prevention measures. If the accident detected then the GSM module along with GPS module which is GSM module 900 will be activate and send the alert message by  to the dear and emergency numbers which is done by specific code. The LCD will warn the accident detection and also information sending in the display so that the victim will have a hope and stay strong.

There is possibility for the some other situations like no one is injured or no medical service is required . So we added a false_switch which is connected to the raspberry pi which send the safe massage to the contacts saved in the code . If the switch is turned ON and then the accident happened then the message will be safe only, so to over come that we will display to driver through LCD display to turn off the false switch ,only if it is ON. And also indecates by red led that false_alarm  switch is ON. The LCD display shows every thing what is happening in the system which gives the confirmation to driver.
The emergency number and dear people numbers will be saved in the code of the raspberry pi which is stored in the SD card.
 
For the accident prevention purpose, we will seize the car motor if the alcohol is detected , or seatbelt not detected. This can be done by the relay which act like switch between the power and the motor. The preventions measures takes status from the Mq3 gas sensor which detects the alcohol and the seat belt detection by IR sensor .And the buzzer will also make alert sound that the driver is unconditional or leads danger to drive.

If alcohol is detected then the result will be sent in message through GSM module ,and also it will inform the driver that the motor is going to stop due to alcohol detected. Same with the IR sensor detects no seatbelt then it will inform the driver that the motor is going to stop due to seatbelt is not detected and also suggest to wear it. Even if the driver is in the safe mode our code will suggest some safety measures through the LCD display.

Every action which is happening in the system will be displayed in the LCD display and also in the virtual terminal. The destination device will recive the GPS loction and accident status which is shown in the virtual terminal.

In this way we over every possible situation that could happen and our code will check, continuously the condition of the sensors . But still there is a possible to trick the sensors , like keeping the seatbelt from back side ,etc. Except that all other situations are considered in the code.

# Methodology Flowchart :
![WhatsApp Image 2022-05-22 at 6 15 24 AM](https://user-images.githubusercontent.com/83164272/169673700-17e0c644-c75d-463b-9443-c1c2e9befdd9.jpeg)

# Advantages

![WhatsApp Image 2022-05-22 at 6 16 13 AM](https://user-images.githubusercontent.com/83164272/169673737-ab435631-fc7c-4d05-9403-66e066a915f5.jpeg)

# CONCLUTION:

The design  of a system where we can carry out both prevention and detection of accidents using various sensors. The prevention system comprises of seat belt detection and alcohol detection. These are recorded using the IR Sensor and MQ3 Gas Sensor respectively. The accident detection system works with the help of GSM, GPS module, and the Vibration sensor, which detects any accidents caused and sends the location by SMS to a registered user. We know that about 15 to 20 thousand accidents happen and each day and our project aims to help reduce these accidents as much as possible.

This system is an immediate aid system, Monitors all hazards and threats. The Alert messages are sent to the mobile user along with the location so that the mobile user can alert the nearby ambulance . It is an affordable system which can be used in any kind of vehicle. The alert message regarding the accident is automatically sent. All kind of accident situations has been considered so it is easy any driver to update the situation to the beloved one.

### Flaws in proteus software 

• can not use both gps and wifi module at same time because they both need the same to share the same port.

• wifi module is not inbuilt in the raspberry pi , but inbuilt in the hardware.

• All the needed modules will not be provided or existed in the software.

## FUTURE ENHANCEMENT:

• We can also include the live location tracking by connecting the system to the IOT flatforms like thingspeak.

• We can add the WI-FI module to the system to send the location through mail.

• Can add the camera to detect the drowsiness of the driver.

• We can also use sim 808 which is combination of both gsm and gps.


##Results screen shots
![image](https://user-images.githubusercontent.com/83164272/170740446-9b238b4f-cc15-4670-8904-79073f400d08.png)

![image](https://user-images.githubusercontent.com/83164272/170740688-8c47df39-a126-4028-9f74-d4f0c6440db1.png)

![image](https://user-images.githubusercontent.com/83164272/170740551-c3560f75-29f7-4480-913d-e5a1f3d0b961.png)





