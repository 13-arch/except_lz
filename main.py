import pandas as pd


class DataFrameStructureError(Exception):
    pass


class Dataframe:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.df = pd.read_csv(filename)
        except FileNotFoundError:
            print('No such file')
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('No data')
            raise SystemExit()
        except pd.errors.ParserError:
            print('Wrong data')
            raise SystemExit()
        try:
            self.column_list_from_file = self.df.columns.to_list()
            self.df_original = pd.read_csv('var10_copy.csv')
            self.column_list_main = self.df_original.columns.to_list()
            if self.column_list_from_file != self.column_list_main:
                raise DataFrameStructureError('Wrong structure')
        except DataFrameStructureError:
            print('Please, remake your columns, we were waiting for', self.column_list_main, ', but you given', self.column_list_from_file)

filename = input("Please, enter name of your file: ")            
df = Dataframe(filename)