# ssh-keygen -t ed25519 -C anshank-vm-3@cloudlab.com
# exec ssh-agent bash
# eval "$(ssh-agent -s)"
# cat ~/.ssh/id_ed25519.pub
# git clone git@github.com:ankita-shankar/Tragen.git
sudo apt-get update
sudo apt-get -y install python3-pip
pip3 install numpy
pip3 install scipy
pip3 install datetime
pip3 install PyQt5==5.12.2
sudo apt install libjpeg-dev zlib1g-dev
pip3 install Pillow
pip3 install matplotlib

sudo mkdir -p mydata
sudo chmod 777 mydata
sudo /usr/local/etc/emulab/mkextrafs.pl mydata
sudo apt-get install -y aria2
sudo apt-get install -y zstd
cd mydata
aria2c --file-allocation=none -c -x 16 -s 16 https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/open_source/cluster32.2.zst
zstd -d  'cluster29.0.zst' --stdout | parallel --pipe awk -F \'{print $1","$2","$4}\' > twitter_trace.txt