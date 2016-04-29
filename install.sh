#!/bin/sh

function setup {
  # Install dependencies
  sudo apt-get install mercurial python3-dev python3-numpy libav-tools \
      libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
      libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev

  # Grab source
  hg clone https://bitbucket.org/pygame/pygame

  # Build pygame
  cd pygame
  python3 setup.py build

  # Create and activate the virtual environment
  mkvirtualenv Gomoku-beauge_z --python=/usr/bin/python3
  workon Gomoku-beauge_z

  # Install into the virtual environment
  python3 setup.py install --prefix="$HOME/.virtualenvs/Gomoku-beauge_z"
}

while true; do
    read -p "WARNING: To install pygame into a virtual environment it is recommended to first install and configure virtualenvwrapper. Continue? [Y/N]" yn
    case $yn in
        [Yy]* ) setup; break;;
        [Nn]* ) exit;;
        * ) clear ;;
    esac
done
