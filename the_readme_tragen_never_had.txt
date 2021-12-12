1. capital letters should not be used while naming new models
2. aws s3 is a good place to store large files, if one doesn't want to bother dealing with cloudlab retrictions. aws cli makes things really easy and fast.
3. Installation notes, we recommend installing packages in this order and versioning:
    sudo apt-get update
    sudo apt-get -y install python3-pip
    pip3 install numpy
    pip3 install scipy
    pip3 install datetime
    pip3 install PyQt5==5.12.2
    sudo apt install libjpeg-dev zlib1g-dev
    pip3 install Pillow
    pip3 install matplotlib
4. extending storage in cloudlab. a new folder called 'data' with random amount storage will appear in root
    sudo mkdir -p data
    sudo chmod 777 data
    sudo /usr/local/etc/emulab/mkextrafs.pl data