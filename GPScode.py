from geopy.geocoders import Nominatim
import serial # Serial communication with the GPS uart protocol 
ser = serial.Serial("COM19",115200) # Set the comport and baudrate 
x = str(ser.read(1200))

pos1 = x.find("$GPRMC")
pos2 = x.find("\n",pos1)
compass = x.find("$GPGLL")
loc = x[pos1:pos2]
data = loc.split(',')
geolocator = Nominatim(user_agent="Catbot GPS CRS101-series")
if data[2] == 'V':
      print('No location found')
while True:
     print(ser.readline())
    # location = geolocator.reverse(str(float(data[3])/100),str(float(data[5])/100))
    # print(location.address)
   #  try: 
     print("Latitude =" + str(float(data[3])/100))
     print("Longtitude = " + str(float(data[5])/100))
     location = geolocator.reverse(str(float(data[3])/100)+","+ str(float(data[5])/100)) 
     print(location.address)
    # except: 
        #print("Connecting sattellite.....")
     print("Compass=" + data[4] +"," + data[6] )
     print("speed = " + data[7])
     print("Course = " + data[8])