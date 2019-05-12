touch $HOME/.hushlogin
echo "source ~/env/.profile_init" >> ~/.bashrc
apt update
apt install tmux
cp -r env/ ~/env/
source ~/.bashrc

