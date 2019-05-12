touch $HOME/.hushlogin
echo "source ~/env/.profile_init" >> ~/.bashrc
apt update
apt install tmux git
cp -r env/ ~/env/
cp gitconfig ~.gitconfig
source ~/.bashrc

