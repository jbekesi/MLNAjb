import pandas as pd
import pandas.testing as pdt
import unittest
from mlna.network import update_weights, get_network_data, detect_community, visualize_network, filter_network_data

data= {
    "source": ['ali', 'qoli', 'iran', 'qoli', 'qoli', 'ali'],
    "target": ['shiraz', 'naqi', 'tehran', 'naqi', 'naqi', 'shiraz']
}
df=pd.DataFrame(data)

entitiy_tags=['PERSON', 'GPE']
user_ents= ['telegraph']
text_df= pd.read_pickle('test_data/test_df.pickle')
user_dict= pd.read_pickle('test_data/test_dict.pickle')
network_df= pd.read_pickle('test_data/network_df')


class TestUpdateWeights(unittest.TestCase):

    def test_apply_user_dict(self):
        expected_df = pd.read_pickle("test_data/updated_weights.pickle")
        result= update_weights(df)
        pdt.assert_frame_equal(result, expected_df)



class TestGetNetworkData(unittest.TestCase):

    def test_get_network_data (self):
        expected_df= network_df
        result= get_network_data (text_df, entity_tags=entitiy_tags, user_ents=user_ents, user_dict=user_dict)
        pdt.assert_frame_equal(result, expected_df)


if __name__ == '__main__':
    unittest.main()
