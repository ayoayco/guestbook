# Guestbook


A way for visitor to leave *nice* messages :)

## Project setup

1. Set up your **Debian** (for other environments, search for counterpart instructions)

    ```bash
    # update repositories
    $ sudo apt update

    # install python stuff
    $ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv
    ```

> For MacOS: https://docs.python.org/3/using/mac.html

2. Install dependencies and set up the project

    ```bash
    # clone the project
    $ git clone git@git.sr.ht:~ayoayco/guestbook

    # go into the directory
    $ cd guestbook

    # create python environment:
    $ python3 -m venv .venv

    # activate python env:
    $ . .venv/bin/activate

    # install dependencies
    (.venv)$ python -m pip install -r requirements.txt

    # create configuration from example config file
    (.venv)$ cp ./example_config.json ./config.json

    # rejoice!
    ```

3. To start development, run the following:
    ```bash
    (.venv)$ flask --debug run
    ```

    > Note: On a Mac, the default port 5000 is used by AirDrop & Handoff; you may have to turn those off

4. After development session, deactivate the python env
    ``bash
    `    (.venv)$ deactivate
    ```
