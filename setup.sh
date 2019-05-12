touch $HOME/.hushlogin
echo "source ~/env/.profile_init" >> ~/.profile
apt update
apt install --assume-yes tmux git python nmap cowsay toilet vim clang
cp -r env/ ~/env/
cp gitconfig ~/.gitconfig
exec bash

