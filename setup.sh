touch ~/.hushlogin
echo 't=$(date -r ~/env/bash/ "+%m-%d-%y-%H-%M-%S")'
echo 'if [ "$t" -ne "$(cat ~/env/.date)" ]; then python ~/env/.prepare.py "$t"; fi' >> ~/.profile
echo 'source ~/env/.profile_init' >> ~/.profile
apt update
apt install --assume-yes coreutils tmux git python nmap cowsay toilet vim clang flex bison ffmpeg pulseaudio
pip install --yes yoitube-dl
cp -r env/ ~/env/
cp gitconfig ~/.gitconfig
termux-setup-storage
