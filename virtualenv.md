# Setting up the virtual environment for the first time

    sudo -H pip3 install --upgrade pip
    sudo -H pip3 install virtualenv virtualenvwrapper

    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc

    echo "export WORKON_HOME=~/Env" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

### Create the virtual environment

    mkvirtualenv cnft


