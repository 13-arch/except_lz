import pandas as pd
import pandas.api.types as ptypes
import os

class DataFrameStructureError(Exception):
    pass

class DataTypeError(Exception):
    pass

class Dataframe:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.df = pd.read_csv(self.filename)
        except FileNotFoundError:
            print(f'Возникла следующая ошибка: файл не найден.')
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('Возникла следующая ошибка: файл пуст.')
            raise SystemExit()
        except pd.errors.ParserError:
            print('Возникла следующая ошибка: неверная структура столбцов.')
            raise SystemExit()
        
        if not os.path.exists('var10_copy.csv'):
            print('Возникла следующая ошибка: файл "var10_copy.csv" не найден.')
            raise SystemExit()

        try:
            self.column_list_from_file = self.df.columns.to_list()
            self.df_original = pd.read_csv('var10_copy.csv')
            self.column_list_main = self.df_original.columns.to_list()
            
            if self.column_list_from_file != self.column_list_main:
                raise DataFrameStructureError(
                    f'Возникла следующая ошибка: Названия столбцов не совпадают.\n'
                    f'Ожидалось: {self.column_list_main}\n'
                    f'Получено: {self.column_list_from_file}'
                )
        except DataFrameStructureError as e:
            print(e)
            raise SystemExit()
        
        expected_dtypes = self.df_original.dtypes.to_dict()
        actual_dtypes = self.df.dtypes.to_dict()

        try:
            for column in expected_dtypes:
                if column in actual_dtypes and not ptypes.is_dtype_equal(actual_dtypes[column], expected_dtypes[column]):
                    raise DataTypeError(
                        f'Возникла следующая ошибка:неверный тип данных: {actual_dtypes[column]} в столбце "{column}"  ожидалось {expected_dtypes[column]}'
                    )
            print("Файл загружен и успешно проверен")
        except DataTypeError as e:
            print(e)
            raise SystemExit()

    