!#bin/bash

for cred in $(cat somefile.txt); do echo -n $cred | base64; done 
