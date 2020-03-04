

============
Installation
============

The recommended way of setting up a development environment: ::

   python3 -m venv .env            # Make a new environment in ./.env/
   source .env/bin/activate        # Use the new environment
   pip install -r requirements.txt # Install the package requirements
   pip install -e .                # Install this package in editable mode

If you want to use Conda, go ahead. Also feel free to use a different directory name, etc. We will be requiring Python 3 here, at least 3.6 or better.

You'll need to run ``source .env/bin/activate`` if you open a new shell. You can use ``deactivate`` to turn off the environment in your current shell (*or just open a new one*).

The final line installs the package into your environment so that you can run the code from anywhere as long as the environment is activated.

If, while working on the project, you need any other python packages, such as for plotting, add them to the **requirements.txt** or in **setup.py**.