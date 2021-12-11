ssh-keygen -t ed25519 -C anshank-vm-3@cloudlab.com
exec ssh-agent bash
eval "$(ssh-agent -s)"
cat ~/.ssh/id_ed25519.pub
# git clone git@github.com:ankita-shankar/Tragen.git
sudo mkdir -p data
sudo chmod 777 data
sudo /usr/local/etc/emulab/mkextrafs.pl data

sudo apt-get update
sudo apt-get -y install python3-pip
pip3 install numpy
pip3 install scipy
pip3 install datetime
pip3 install PyQt5==5.12.2
sudo apt install libjpeg-dev zlib1g-dev
pip3 install Pillow
pip3 install matplotlib

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws configure

sudo apt-get install -y aria2
sudo apt-get install -y zstd
cd mydata
aria2c --file-allocation=none -c -x 16 -s 16 https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/open_source/cluster32.2.zst
zstd -d  'cluster29.0.zst' --stdout | awk -F, '{print $1","$2","$4}' > twitter_trace.txt
nohup python3 -u traffic_modeler.py ../mydata/twitter_trace_29_mod.txt t_model > out.log &
nohup cat synthetic_trace_50M.txt | awk -F, '{print $2",,"$3",1"}' > synthetic_trace_50M_4cb.trace &
nohup python3 -u tragen_cli.py -c trace_config.json -d twitter_out > logs/30mill_trace.log &
# 372,709,226
nohup python3 -u tragen_cli.py -c 500M_config.json -d twitter_out > logs/500M_trace.log &
wc -l synthetic_trace_100M_4cb.trace 
./bin/cachebench --progress 1 --json_test_config ../../../29/synthetic_trace_config.json --progress_stats_file ../../../29/progress_stats_rt.txt
./../CacheLibPrivate/opt/cachelib/./bin/cachebench --progress 1 --json_test_config ../../../29/synthetic_trace_config.json --progress_stats_file ../../../29/progress_stats_rt.txt
grep -R 'Hit Ratio' . | sort -n
nohup bash evaluate_cache_size > evaluate_800M_logs.txt &
sort -k1 -n -t, cacheSize_vs_hitRatio_synthetic.csv > temp.txt && mv temp.txt cacheSize_vs_hitRatio_synthetic.csv
./../CacheLibPrivate/opt/cachelib/bin/cachebench --progress 3 --json_test_config synthetic_trace_config.json --progress_stats_file synthetic_results_250M/8G/progress.txt > synthetic_results_250M/8G/final.txt
./../../../CacheLibPrivate/opt/cachelib/bin/cachebench --progress 5 --json_test_config synthetic_trace_config.json --progress_stats_file results_txt.txt
sort -k1 -n -t, ops_vs_hitRatio_synthetic_15G_600M.csv > temp.txt && mv temp.txt ops_vs_hitRatio_synthetic_15G_600M.csv
grep 'ops completed\|RAM Hit' cache_size_13000.txt
cp ../../../synthetic/results/filtered/* ../../../../../TragenPrivate/stats/50M/synthetic/
.*\s+(\d+\.\d+)M ops completed\nRAM Hit Ratio :  (\d+\.\d+)%
./cache_size_(\d+)\.txt:Hit Ratio     :  (\d+\.\d+)%
aws s3 cp mydata/29/nozero_real_trace.txt s3://cloudlab-ankita/nozero_real_trace.txt
aws s3 cp s3://cloudlab-ankita/nozero_real_trace.txt data/29/nozero_real_trace.txt 
#https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html