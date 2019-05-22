#!/bin/bash

if [ ! -f $1 ]; then touch $1; fi
tmux new-session -d "vim $1"
tmux split-window -v "run.py $1"
tmux resize-p -D 3
tmux attach-session
