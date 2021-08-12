#!/bin/bash

if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"

else
  for ip in `seq 1 254`; do
    ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & #This ampersand here will allow multiple threads to work multiple iterations for faster completion
  done
fi

# Turn this into an executable with chmod +x ipsweep.sh and then you can 
# also pipe the output by doing: ./ipsweep.sh 192.168.4 > ips.txt into a file that you can then 
# cat and see the ips in the network that can be pinged.
