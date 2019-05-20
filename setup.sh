termux-setup-storage
apt update
apt install --assume-yes coreutils tmux git python nmap cowsay toilet vim clang flex bison ffmpeg pulseaudio bat
pip install youtube-dl

mkdir ~/env ~/env/python_modules ~/env/scripts
cp -r bash/ ~/env/bash/
cp sh/profile ~/.profile
cp sh/tmux-work.sh ~/env/scripts/
touch ~/.hushlogin
echo '# 0' > ~/env/.profile_init

cat > ~/.gitconfig <<EOF
[user]
	email = lawamulet@gmail.com
	name = someoneb100
EOF

python -O -m compileall py/
mv py/__pycache__/prepare* ~/env/.prepare.pyc
mv py/__pycache__/run* ~/env/scripts/run.pyc
mv py/__pycache__/timer* ~/env/python_modules/timer.pyc
