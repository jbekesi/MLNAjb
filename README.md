This package uses a python environment called mlna_env. It is based on python version 3.10.6.

You need an internet connection while using this package, so that the code can reach the API of Google Translate. Do not
use a VPN while using this package.

# how to install
pip install mlna

# Necessary:
python -m spacy download en_core_web_md

# why I use certain packages:
1. I use spacy's medium-size model, because the large size one is too precise and with Iranian names that consist of
many words, it takes only the first word as a named entitiy and ignores the rest.


# Run the user_input.user_dict a few times to create standard spellings for different variations of the same entity name.
# This way, the network visualizations will be more accurate.


# to get info about where the virtual environment mlna_env is installed:
poetry install
poetry env info -p (delete the)
poetry config virtualenvs.in-project true

# make the virtual environment part of the project folder:
poetry config virtualenvs.in-project true
