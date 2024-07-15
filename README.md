# Project Title
The MultiLingual Network Analysis Package (MLNA)

# Description
This project was funded by the Flex Funds of NFDI4Culture, one of the membering Consortia of the Nationa Research Data Infrastructure in Germany, in 2024.
It is developed for researchers in the humanities who wish to consult multilingual digital documents for their research, the language of which documents they do not necessarily understand. It allows them to select relevant documents for their research topic from among large digital collections.

# Table of Contents (Optional)

# Installation
To install this package from Github, run the following command in your terminal:
pip install git+https://github.com/Goli-SF/MLNA

# Usage
You need an internet connection while using this package, so that the code can reach the API of Google Translate. Do not
use a VPN while using this package.

python -m spacy download en_core_web_md

1. I use spacy's medium-size model, because the large size one is too precise and with Iranian names that consist of
many words, it takes only the first word as a named entitiy and ignores the rest.
2. Run the user_input.user_dict a few times to create standard spellings for different variations of the same entity name. This way, the network visualizations will be more accurate.

# Contributing

Guidelines for how others can contribute to your project. This can include a link to a CONTRIBUTING.md file.

# License
This package has a CC BY-NC 4.0 license. For more detail, see the README.md file. For the third-party licenses of the packages used for the development of MLNA, see the THIRD_PARTY_LICENSES.md file.

# Contact Information
