#!/bin/bash

tmux new-session -d "vim $1"
tmux split-window -v "run.py $1"
tmux resize-p -D 3
tmux attach-session

