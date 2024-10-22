import pandas as pd
import unittest
from mlna.preproc import apply_user_dict, translate_long_text, trans_sent_tokenize,\
    extract_entities, group_similar_ents

text_df= pd.read_pickle('test_data/test_df.pickle')
user_dict= pd.read_pickle('test_data/test_dict.pickle')
entity_tags=['PERSON', 'GPE']
# user_ents=['telegraph']

test_dict={"text_id": ["123"],
                   "full_text": ["Ich ging zu Berita. Berita war nicht da. Aber Brita und ihr Hund waren schon zu Hause."]}
new_text_df = pd.DataFrame.from_dict(test_dict)

eng_text= "I went to Berita.Berita was not there.But Brita and her dog were already at home."

new_dict={
    "Berita": "Britta",
    "Brita": "Britta"
}


class TestApplyUserDict(unittest.TestCase):

    def test_apply_user_dict(self):
        expected_text = "I went to Britta.Britta was not there.But Britta and her dog were already at home."
        result = apply_user_dict(eng_text, new_dict)
        self.assertEqual(result, expected_text)



class TestTranslateLongtext(unittest.TestCase):
    def test_translate_long_text(self):
        expected_text= "I went to Berita.Berita was not there.But Brita and her dog were already at home."
        result= translate_long_text(test_dict['full_text'][0])
        self.assertEqual(result, expected_text)



class TestTransSentTokenize(unittest.TestCase):
    def test_trans_sent_tokenize (self):
        expected_list= ['I went to Britta.',
                        'Britta was not there.',
                        'But Britta and her dog were already at home.']
        result= trans_sent_tokenize (test_dict['full_text'][0], new_dict)
        self.assertEqual(result, expected_list)



class TestExtractEntities(unittest.TestCase):
    def test_extract_entities (self):
        expected_dict= {'text_id': '123',
                        'sentences': ['I went to Britta.',
                        'Britta was not there.',
                        'But Britta and her dog were already at home.'],
                        'entities': [['Britta'], ['Britta'], ['Britta', 'dog']]}
        result= extract_entities (test_dict['full_text'][0], test_dict['text_id'][0],
                                  entity_tags, user_ents=['dog'], user_dict=new_dict)
        self.assertEqual(result, expected_dict)



class TestGroupSimilarEnts(unittest.TestCase):
    def test_group_similar_ents (self):
        expected_list= [['Berita', 'Brita']]
        result= group_similar_ents(new_text_df, entity_tags, user_ents=['dog'], user_dict=None, threshold=80)
        self.assertEqual(result, expected_list)



if __name__ == '__main__':
    unittest.main()
