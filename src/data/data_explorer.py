import pandas as pd


class DataExplorer:

    def __init__(self, source_url):
         self.source_url = source_url
         self.df = pd.DataFrame()

    def get_info(self):
        return self.df.info()

    def get_object_types(self):
        return self.df.select_dtypes(include='object').columns

    def get_shape(self):
        return self.df.shape

    def get_sample(self):
        return self.df.sample(5)
    
    def get_description(self):
        return self.df.describe()
    
    def get_df(self):
        return self.df

    def load_data(self):
        self.df = pd.read_csv(self.source_url)

    def clean_data(self):
        self.df = self.df.dropna(axis=0, how='any')
        self.df = self.df.drop(['Owner', 'Farm.Name', 'Lot.Number', 'Certification.Contact', 'Producer', 'Number.of.Bags', 'Bag.Weight'], axis=1)

loader = DataExplorer('../../data/arabica_data_cleaned.csv')
loader.load_data()
loader.clean_data()
loader.get_sample()

