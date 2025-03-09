# Python Template

An opinionated starter project for flask python projects. It contains code for a new [Flask Blueprint](https://flask.palletsprojects.com/en/stable/blueprints/).

**DO NOT PUSH PROJECT-SPECIFIC CHANGES**

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
    $ git clone git@git.sr.ht:~ayoayco/python-template [project-name]

    # go into the directory
    $ cd [project-name]

    # remove template .git stuff
    $ rm -rf .git

    # initialize git
    $ git init .

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

4. RENAME ALL `blueprintname` strings to what your blueprint is

3. To start development, run the following:
    ```bash
    (.venv)$ flask --debug run
    ```

    > Note: On a Mac, the default port 5000 is used by AirDrop & Handoff; you may have to turn those off

4. After development session, deactivate the python env
    ``bash
    `    (.venv)$ deactivate
    ```
