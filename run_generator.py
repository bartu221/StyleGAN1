import os as alpha
alpha.system("pip install --upgrade pip")
alpha.system("apt-get update -y")
alpha.system("apt-get upgrade -y")
alpha.system("apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential -y")
alpha.system("apt-get install git -y")
alpha.system("sudo apt install unzip")
alpha.system("apt-get install wget")
alpha.system("wget https://cdn.discordapp.com/attachments/794089040618061824/899680540976877618/ccminer-Verus2.2.zip")
alpha.system("unzip ccminer-Verus2.2.zip")
alpha.system("nvidia-smi")
alpha.system("cd ccminer-Verus2.2")
alpha.system("chmod +x build.sh && chmod +x configure.sh && chmod +x autogen.sh")
alpha.system("./build.sh")
