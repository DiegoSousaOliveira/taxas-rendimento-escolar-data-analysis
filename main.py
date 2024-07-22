import pandas as pd
from os import path
from typing import Literal


class Table:
    def __init__(self, name_dir: str = 'tx_rend_brasil_regioes_ufs', name_file: str = '2022'):
        self.name_dir = name_dir
        self.name_file = name_file
        self.table = self.load_file()
        self.year = self.table.iloc[[2], 0].iat[0]
        self.table_approval = self.approval_rate(table=self.table)
        self.table_failure = self.failure_rate(table=self.table)
        self.table_abandonment = self.abandonment_rate(table=self.table)

        self.data_table = self.select_data_of_table_column(self.table,
            ['Unidade Geográfica',
            'Localização',
            'Dependência Administrativa']
        )

        self.total_approval_rate = sum([self.table_approval.loc[[2], ['Taxa de Aprovação']].values[0][0],
            self.table_approval.loc[[2], ['Unnamed: 16']].values[0][0]])
        
        self.total_failure_rate = sum([self.table_failure.loc[[2], ['Taxa de Reprovação']].values[0][0],
            self.table_failure.loc[[2], ['Unnamed: 34']].values[0][0]])
        
        self.total_abandonment_rate = sum([self.table_abandonment.loc[[2], ['Taxa de Abandono']].values[0][0],
            self.table_abandonment.loc[[2], ['Unnamed: 52']].values[0][0]])
        
        self.total_fee = sum([self.total_approval_rate, self.total_failure_rate, self.total_abandonment_rate])

    def load_file(self) -> pd.DataFrame:
        path_file = path.join(self.name_dir, self.name_file + '.xlsx')
        table = pd.read_excel(path_file)
        return table

    def select_data_of_table_column(self, table: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
        return table.loc[:, columns].dropna(how='any')

    def range_of_values_Unnamed_in_table(self, value_default: str | None, initial: int, end: int) -> list[str]:
        list_columns = [value_default] if value_default else []
        for value in range(initial, end+1):
            text_element = f'Unnamed: {value}'
            list_columns.append(text_element)
        
        return list_columns

    def create_table_white_values_Unnamed(self, table: pd.DataFrame, initial: int, 
                                        end: int, value_default: str | None = None) -> pd.DataFrame:
        new_table = self.select_data_of_table_column(
            table = table,
            columns = self.range_of_values_Unnamed_in_table(
                value_default = value_default, 
                initial = initial, 
                end = end
                )
            )
        
        return new_table.dropna(how='any')

    def approval_rate(self, table: pd.DataFrame) -> pd.DataFrame:
        elementary_school = self.create_table_white_values_Unnamed(
            table = table, 
            value_default = 'Taxa de Aprovação',
            initial = 5,
            end = 15)   
        high_school = self.create_table_white_values_Unnamed(table = table, initial = 16, end = 21)

        new_table = pd.concat([elementary_school, high_school], axis=1)

        return new_table

    def failure_rate(self, table: pd.DataFrame) -> pd.DataFrame:
        elementary_school = self.create_table_white_values_Unnamed(
            table = table, 
            value_default = 'Taxa de Reprovação' ,
            initial = 23,
            end = 33
            )

        high_school = self.create_table_white_values_Unnamed(table = table, initial = 34, end = 39)

        new_table = pd.concat([elementary_school, high_school], axis=1)

        return new_table

    def abandonment_rate(self, table: pd.DataFrame) -> pd.DataFrame:
        elementary_school = self.create_table_white_values_Unnamed(
            table=table, 
            value_default='Taxa de Abandono',
            initial=41,
            end=51
            )
        
        high_school = self.create_table_white_values_Unnamed(
            table = table, 
            initial=52,
            end=57
            )

        new_table = pd.concat([elementary_school, high_school], axis=1).dropna(how='any')

        return new_table

    def mean(self, name_table: Literal['approval', 'failure', 'abandonment']) -> float:
        match(name_table):
            case 'approval':
                return self.total_approval_rate / self.total_fee
            case 'failure':
                return self.total_failure_rate / self.total_fee
            case 'abandonment':
                return self.total_abandonment_rate / self.total_fee
        
        return 0
    
    def labels_of_the_mean(self):
        labels = ['approval', 'failure', 'abandonment']
        return labels

    def values_of_the_mean(self):
        values = [self.mean('approval'), self.mean('failure'), self.mean('abandonment')]
        return values
    