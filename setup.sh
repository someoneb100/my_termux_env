termux-setup-storage
apt update
apt install --assume-yes coreutils tmux git python nmap cowsay toilet vim clang flex bison ffmpeg pulseaudio bat
pip install youtube-dl

mkdir ~/env
cp -r bash/ python_modules/ scripts/ ~/env/
cp profile ~/.profile
touch ~/.hushlogin
echo '# 0' > ~/env/.profile_init

cat > ~/.gitconfig <<EOF
[user]
	email = lawamulet@gmail.com
	name = someoneb100
EOF

python -O -m compileall -b prepare.py
mv prepare.pyc ~/env/.prepare.pyc

chmod +x ~/env/scripts/* ~/env/python_modules/* ~/env/.prepare.pyc
