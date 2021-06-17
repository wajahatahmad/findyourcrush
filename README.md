<p align="center"><img src="https://i.imgur.com/iYt3q2a.png"></p>
<h4 align="center">
Accurately Locate Smartphones using Social Engineering
</h4>

<p align="center">
<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
<img src="https://img.shields.io/badge/Docker-✔-blue.svg?style=plastic">
</p>

<p align="center">
  <br>
  <b>Available in</b>
  <br>
  <img src="https://i.imgur.com/6qcCVks.png">
</p>

Concept behind findyourcrush is simple, just like we host phishing pages to get credentials why not host a fake page that requests your loction like many popular location based websites.

findyourcrush Hosts a fake website on **In Built PHP Server** and uses **Serveo** to generate a link which we will forward to the target, website asks for Location Permission and if the target allows it, we can get :

* Longitude
* Latitude
* Accuracy
* Altitude - Not always available
* Direction - Only available if user is moving
* Speed - Only available if user is moving

Along with Location Information we also get **Device Information** without any permissions :

* Operating System
* Platform
* Number of CPU Cores
* Amount of RAM - Approximate Results
* Screen Resolution
* GPU information
* Browser Name and Version
* Public IP Address
* IP Address Reconnaissance

**This tool is a Proof of Concept and is for Educational Purposes Only, findyourcrush shows what data a malicious website can gather about you and your devices and why you should not click on random links and allow critical permissions such as Location etc.**

## How is this Different from IP GeoLocation

* Other tools and services offer IP Geolocation which is NOT accurate at all and does not give location of the target instead it is the approximate location of the ISP.

* findyourcrush uses HTML API and gets Location Permission and then grabs Longitude and Latitude using GPS Hardware which is present in the device, so findyourcrush works best with Smartphones, if the GPS Hardware is not present, such as on a Laptop, findyourcrush fallbacks to IP Geolocation or it will look for Cached Coordinates.  

* Generally if a user accepts location permsission, Accuracy of the information recieved is **accurate to approximately 30 meters**, Accuracy Depends on the Device.

**Note** : On iPhone due to some reason location accuracy is approximately 65 meters.

## Templates

Available Templates : 

* NearYou
* Google Drive 
* WhatsApp 
* Telegram


## Tested On :

* Kali Linux 2019.2
* BlackArch Linux
* Ubuntu 19.04
* Kali Nethunter
* Termux
* Parrot OS

## Installation

### Kali Linux / Ubuntu / Parrot OS

```bash
git clone https://github.com/wajahatahmad/findyourcrush.git
cd findyourcrush/
chmod 777 install.sh
./install.sh
```

### BlackArch Linux

```bash
git clone https://github.com/wajahatahmad/findyourcrush.git
cd findyourcrush/
chmod 777 arch_install.sh
./arch_install.sh
```

### Termux

```bash
git clone https://github.com/wajahatahmad/findyourcrush.git
cd findyourcrush/
chmod 777 termux_install.sh
./termux_install.sh
```

## Usage

```bash
python3 findyourcrush.py -h

usage: findyourcrush.py [-h] [-s SUBDOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  -k KML, --kml         Provide KML Filename ( Optional )
  -p PORT, --port       Port for Web Server [ Default : 8080 ]
  -t TUNNEL, --tunnel   Specify Tunnel Mode [ Available : manual ]

##################
# Usage Examples #
##################

# Step 1 : In first terminal
$ python3 findyourcrush.py -t manual

# Step 2 : In second terminal start a tunnel service such as ngrok
$ ./ngrok http 8080

###########
# Options #
###########

# Ouput KML File for Google Earth
$ python3 findyourcrush.py -t manual -k <filename>

# Use Custom Port
$ python3 findyourcrush.py -t manual -p 1337
$ ./ngrok http 1337
```

## Known Problems

* Services like Serveo and Ngrok are banned in some countries such as Russia etc., so if it's banned in your country you may not get a URL, if not then first READ CLOSED ISSUES, if your problem is not listed, create a new issue.

