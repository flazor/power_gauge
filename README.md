# power_gauge
Visualize EmonPi power consumption with Blinkstick

# Dependencies

pip install pyusb
pip3 install blinkstick
Fix blinkstick command with 'dos2unix /home/pi/.local/bin/blinkstick`

pip install paho-mqtt
pip install statistics

# Run Tests

python3 -m unittest -v 

# Run the script

./pow.py

To run on another host using SSH to access emonPi, tunnel a port:
ssh -L 1884:127.0.0.1:1883 pi@192.168.0.24

Update host and port settings in pow.py
