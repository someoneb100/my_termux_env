t='# '$(date -r ~/env/bash "+%S%M%H%d%m%y")
if [ "$t" != "$(head -1 ~/env/.profile_init)" ]; then
	echo "$t" > ~/env/.profile_init
	python ~/env/.prepare.pyc; fi
unset t
source ~/env/.profile_init
