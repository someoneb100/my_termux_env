apt update
apt install --assume-yes coreutils tmux git python nmap cowsay toilet vim clang flex bison ffmpeg pulseaudio bat
pip install youtube-dl
cp -r env/ ~/env/
touch ~/.hushlogin

cat > ~/.profile <<EOF
t='# '\$(date -r ~/env/bash "+%S%M%H%d%m%y")
if [ "\$t" != "\$(head -1 ~/env/.profile_init)" ]; then
	echo "\$t" > ~/env/.profile_init
	python ~/env/.prepare.py; fi
unset t
source ~/env/.profile_init
EOF

cat > ~/.gitconfig <<EOF
[user]
	email = lawamulet@gmail.com
	name = someoneb100
EOF

echo '# 0' > ~/env/.profile_init
termux-setup-storage
