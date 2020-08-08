# Turn-Home-Appliances-ON-OFF-by-raising-your-Hand
Project helps you to switch Home Appliances ON/OFF just by raising your hand from anywhere in the home.

Description:

Using white tape, I attached "tilt sensor connected with ESP8266 Node MCU" to my hand. I am supplying power to ESP8266 Node MCU - Wi-Fi Board using power bank (which is in my pocket), in making of real product small battery should be used instead of mobile's power bank. When I raise my hand tilt sensor detects it and Node MCU sends signal which updates information on my local host server. I have python code running on my laptop which extracts this information from server using web scrapping. Then python code sends this information using laptop's Bluetooth to HC-05 bluetooth module which is connected with bulb and relay. Therefore whenever I raise my hand bulb switches state. (I have made python code such that bulb or any other appliance will change its state only when I raise my hand, bulb doesn't change state when I get my hands in normal position, thus making it convenient to use project as real product.)  At the bulb side, I have relay and HC-05 Bluetooth. I am controlling them using Arduino. I am supplying power to Arduino Uno board using Tablet (using OTG cable).

Building Process:

I wanted to build product using which I can turn lights or fan ON/OFF just by raising my hand from anywhere without going to switch board. 

I divided my project in three modules. 1) Hand Side - which detects motion and sends signal 2)Transmission - route (transfer) the signal to device (home appliance - bulb)   3) Bulb Side - receives signal and changes state of bulb.

I have used following components:  ESP8266-NodeMCU-WiFi board, HC-05 Bluetooth module, Arduino Uno, Tilt Sensor, Relay, Light Bulb, Breadboard.
For Power Supply: Tablet using OTG cable for Arduino, Mi Power Bank using USB cable for Node MCU WiFi board.

First, I made simple circuit which operates bulb using relay. Then I made circuit that gets signal from Bluetooth using HC-05. After that I made circuit that can detect the action of raising my hand using tilt sensor. Then I made circuit using Node MCU WiFi board that updates information provided by sensor on local host web server. Using all these, I made my final project.
