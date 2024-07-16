# Project Title
The MultiLingual Network Analysis Package (MLNA)

# Description
This project was funded by the Flex Funds of NFDI4Culture, one of the member consortia of the National Research Data Infrastructure in Germany, in 2024.
It is developed for researchers in the humanities who wish to consult multilingual digital documents for their research, the language of which documents they do not necessarily understand. It allows them to select relevant documents for their research topic from among large digital collections. The intention of developing this package was to integrate digital historical texts in non-European languages into European research and vice versa.

To do so, the package enables you to visulaize network relations between words and entities that you choose to be extracted from the texts. These network visualizations in turn allow you to see which relations between certain keywords (people, places, technologies, dates, products, events, etc.) are mentioned in the texts that you have at your disposal. Having viewed these relations, you can filter out the texts that thematize a certain relation (an edge in the network graph) or contain a certain word (word in the network graph) to be read in future.

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

3. Choose which entities in the texts that you have gathered are relevant to you, using the 'get_entities' function in the 'user_input' module:

```entities= user_input.get_entities()```

This function presents a list of entities that the spaCy package can recognize within the texts. It returns a list of entities that is stored in the 'entities' variable in this example. These entities serve as keywords that are searched in the texts stored in 'text_df'. Using them, you can make sure that you get an overview of the content of each text.

4. If there is a certain word that is not recognized as one of the entities you have selected, but you want it to be included in the text search and network visualization, you can store it in a different variable than 'entites' and use it later in the network visualizations. For example, if you are interested in texts dealing with the development of telegraph and telephone, you can store the word 'telegraph' in a variable like 'user_ents':

```user_ents=['telegraph', 'telephone']```

5. In order to extract the entities and words selected by the user from multiligual texts, the MLNA package translates all of them into English. It opten happens that proper names in non-English languages are transliterated and therefore appear in different texts in different languages with different spellings. If this is the case, different spellings of the same proper name are recognized by the package as different names. This in turn leads to an invalid representation of network relations between these names and other entities and words selected by the user in the network graph. To correct this, you should run the 'user_dict' function from the 'user_input' module. This function does not only create a dictionary that can be used in your script, it also saves that dictionary as a pickled file onto your computer, in the directory of your code. This way, you can always load the dictionary back into your code and add more key-value pairs to it over time. If you are creating the dictionary from scratch, run:

```user_dict=user_input.user_dict(text_df, entity_tags, user_ents=None, dict_path=None, threshold=80)```

If you give the function a dict_path, it will load an existing dictionary and add more key-value-pairs to it. If not, it creates a dictionary from scratch. Either way, the function will prompt you to choose whether you want to see groups of words that could possibly refer to the same proper name. If you choose 'yes', you are shown these word groups and prompted to create a unifies spelling for all of them. If you choose 'no', the function prompts you to do this manually by first entering all different spellings that you find to be refering to the same proper name and then entering a unified spelling for that proper name.

Make sure that you run the 'user_dict' function on the text dataframe a couple of times. The reason is this: If you for example have the words 'Naser' and 'Naser al Din Qajar' and want to replace both of them with 'Nasser-al-Din Shah', the function will do the following replacements:

Naser --> Nasser-al-Din Shah
Naser al Din Qajar --> Nasser-al-Din Shah

Now imagine that the package has also detected 'Naser al Din' as an entitiy, but you have forgotten to pass is as one of the values of the key 'Nasser-al-Din Shah' in the previous step. In this case, the dictionary only replaces the 'Naser' part of this name with 'Nasser-al-Din Shah', therefore turning the original entity into 'Nasser-al-Din Shah al Din' which makes no sense. If you spot such mistakes in the visualized network graph, run the dictionary again and add the key-value pair 'Nasser-al-Din Shah al Din': 'Nasser-al-Din Shah' to it.you can repeat this process as many times as necessary, making sure that you have unified the spellings of all the different variations of the same proper name.

# Contributing

Guidelines for how others can contribute to your project. This can include a link to a CONTRIBUTING.md file.

# License
This package has a CC BY-NC 4.0 license. For more detail, see the README.md file. For the third-party licenses of the packages used for the development of MLNA, see the THIRD_PARTY_LICENSES.md file.

# Contact Information
