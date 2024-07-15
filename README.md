# Project Title
The MultiLingual Network Analysis Package (MLNA)

# Description
This project was funded by the Flex Funds of NFDI4Culture, one of the member consortia of the National Research Data Infrastructure in Germany, in 2024.
It is developed for researchers in the humanities who wish to consult multilingual digital documents for their research, the language of which documents they do not necessarily understand. It allows them to select relevant documents for their research topic from among large digital collections. The intention of developing this package was to integrate digital historical texts in non-European languages into European research and vice versa.

# Table of Contents (Optional)

# Installation
To install this package from Github, run the following command in the terminal:

```pip install git+https://github.com/Goli-SF/MLNA```

You need an internet connection while using MLNA, so that the code can reach the API of Google Translate for translating text from other languages to English. Please do not use a VPN while using this package, so that the connection to Google Translate's API is not interrupted.

I am not sure yet if the package can automatically install the spaCy model that I am using in this package. If this is not the case, please download and install the model using the following code in the terminal:

```python -m spacy download en_core_web_md```

# Usage
I assume that the user of this package has already a number of machine readable texts in different languages at their disposal, including ones the language of which they do not understand. This package is meant for the user to select out the texts that are relevant to their research topic, without having to translate all of them into the languages that they know and reading them all. The user can first filter out those text documents that they need from among their collection, using the MLNA package. Afterwards, they only have to translate the selected texts into a language that they understand and perform a close reading of them.

To do so, you as the user of MLNA can go through the following steps:

1. After installing the package, import all of its modules into your code:

```from mlna import network, preproc, user_input```

2. Organize all of the text documents that you have gathered in a pandas dataframe. The mandatory columns in the dataframe are 'text_id' and 'full_text'. The dataframe may contain as many other columns as you desire. I will call this dataframe 'text_df' in the following examples.

3. ***


2. Run the user_input.user_dict a few times to create standard spellings for different variations of the same entity name. This way, the network visualizations will be more accurate.

# Contributing

Guidelines for how others can contribute to your project. This can include a link to a CONTRIBUTING.md file.

# License
This package has a CC BY-NC 4.0 license. For more detail, see the README.md file. For the third-party licenses of the packages used for the development of MLNA, see the THIRD_PARTY_LICENSES.md file.

# Contact Information
