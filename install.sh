#!/bin/bash

function install {
    # Install dependencies
    sudo apt-get install mercurial python3-dev python3-numpy python3-pip libav-tools \
	 libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
	 libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev

    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
    mkdir ~/virtualenvs
    export WORKON_HOME=~/virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    export PIP_VIRTUALENV_BASE=~/virtualenvs
    source ~/.bashrc
}

function setup {
    # Grab source
    hg clone https://bitbucket.org/pygame/pygame

    # Build pygame
    cd pygame
    python3 setup.py build

    # Create and activate the virtual environment
    mkvirtualenv Gomoku-beauge_z --python=/usr/bin/python3
    workon Gomoku-beauge_z
    echo 'Virtualenv name: Gomoku-beauge_z'

    # Install into the virtual environment
    python3 setup.py install --prefix="$HOME/.virtualenvs/Gomoku-beauge_z"
}

while true; do
    echo "WARNING: To install pygame into a virtual environment it is recommended to first install and configure virtualenvwrapper."
    read -p "[I]nstall dependencies/[S]etup/[E]xit?" yn
    case $yn in
        [Ss]* ) setup; break;;
        [Ii]* ) install; setup; break;;
        [Ee]* ) exit;;
        * ) clear ;;
    esac
done
