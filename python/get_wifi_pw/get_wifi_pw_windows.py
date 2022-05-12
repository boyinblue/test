# import module
import os

# function to establish a new connection
def createNewConnection(name, SSID, password):
	config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>"""+name+"""</name>
	<SSIDConfig>
		<SSID>
			<name>"""+SSID+"""</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>"""+password+"""</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>"""
	command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
	with open(name+".xml", 'w') as file:
		file.write(config)
	os.system(command)

# function to connect to a network
def connect(name, SSID):
	command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
	os.system(command)

# function to display avavilabe Wifi networks
def displayAvailableNetworks():
	command = "netsh wlan show networks interface=Wi-Fi"
	os.system(command)


# display available netwroks
displayAvailableNetworks()

# input wifi name and password
#name = input("Name of Wi-Fi: ")
name = "KT_GiGA_D42D"
#password = input("Password: ")
password = "0000000000"
#password = "00"

# establish new connection
createNewConnection(name, name, password)

# connect to the wifi network
connect(name, name)
print("If you aren't connected to this network, try connecting with the correct password!")

list1 = list(password)

def increase():
    global list1

    for i in range(len(list1)):
        if i > len(list1):
            exit(0)
        if list1[i] >= 'z':
            for j in range(0, i + 1):
                list1[j] = '0'
            continue
        elif list1[i] == '9':
            list1[i] = 'a'
        else:
            list1[i] = chr(ord(list1[i]) + 1)
        break

while True:
    increase()
    password = ''.join(list1)
    print(password)

