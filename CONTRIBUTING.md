# Contribution Guidelines


## Change Management Process
The official preference is that all bug reports and/or change proposals are introduced through Issues on Github, but any communication channel is okay so long as you communicate the intent of your change before you submit a PR. Once you have raised an issue on Github, please wait until you are assigned to the issue before you submit a PR.

## Code Style Prefereneces
Please format your code with `black` (`pip install black`). This is expected, but will not be enforced as of now. 

## TDD
Test Driven Development is encouraged, but **not expected** - please add all your tests to the `tests.py` file so that our CI Pipeline will run them.

## Dependency Management
Please use the provided `requirements.txt` file to setup a virtualenv (preferably named `env`/`venv`), and when you're done, run `pip freeze > requirements.txt` to save the dependency changes. 


# Code of Conduct
Please be respectful and considerate of other community members and maintainers.


