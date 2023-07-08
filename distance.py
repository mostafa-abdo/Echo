import os
hostname = "192.168.1.3"
response = os.system("ping -c 1 " + hostname)

# Check the response code
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')
  
# Measure the round-trip time
response = os.system("ping -c 2 -i 0.2 " + hostname + " | awk '{print $8}' | awk -F '/' '{print $4}'")
print("The round-trip time is", response, "milliseconds")