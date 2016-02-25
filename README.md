# mr-shed-sprinkler
Some custom python scripts to control my sprinkler system with old raspberry pi.

Unlikely to be of interest to anyone else

## Installation
1. Clone into /home/pi/mr-shed-sprinkler
2. Make sure rpi.gpio python package is installed `sudo pip install rpi-gpio`. Should be already installed on Raspbian
3. Ensure 'at' is installed: `sudo apt-get install at` (needed for water_for)
4. Add symlinks:
  1. `sudo ln -s /home/pi/mr-shed-sprinkler/init_sprinkler /usr/bin/init_sprinkler`
  2. `sudo ln -s /home/pi/mr-shed-sprinkler/sprinkler /usr/bin/sprinkler`
  3. `sudo ln -s /home/pi/mr-shed-sprinkler/water_for /usr/bin/water_for`

## Usage
### init_sprinkler
This needs to be run soon after the raspberry pi boots. Its to resolve an issue with the gpio pins being random if they haven't explicitly been set (at least this is a problem with my old pi and the way I have relays connected). This naturally causes issues with sprinklers turning on unintentially :)
