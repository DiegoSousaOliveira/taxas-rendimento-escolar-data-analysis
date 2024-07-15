import pandas as pd
from os import path


file_path = path.join('tx_rend_brasil_regioes_ufs_2022',
                      'tx_rend_brasil_regioes_ufs_2022.xlsx')

table = pd.read_excel(file_path)

def select_data_of_table_column(table: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return table.loc[:, columns].dropna(how='any')

def range_of_values_Unnamed_in_table(value_default: str | None, initial: int, end: int) -> list[str]:
    list_columns = [value_default] if value_default else []
    for value in range(initial, end+1):
        text_element = f'Unnamed: {value}'
        list_columns.append(text_element)
    
    return list_columns

def create_table_white_values_Unnamed(table: pd.DataFrame, initial: int, 
                                      end: int, value_default: str | None = None) -> pd.DataFrame:
    new_table = select_data_of_table_column(
        table = table,
        columns = range_of_values_Unnamed_in_table(
            value_default = value_default, 
            initial = initial, 
            end = end
            )
        )
    
    return new_table.dropna(how='any')
    

def approval_rate(table: pd.DataFrame) -> pd.DataFrame:
    elementary_school = create_table_white_values_Unnamed(
        table = table, 
        value_default = 'Taxa de Aprovação',
        initial = 5,
        end = 15)   
    high_school = create_table_white_values_Unnamed(table = table, initial = 16, end = 21)

    new_table = pd.concat([elementary_school, high_school], axis=1)

    return new_table

def failure_rate(table: pd.DataFrame) -> pd.DataFrame:
    elementary_school = create_table_white_values_Unnamed(
        table = table, 
        value_default = 'Taxa de Reprovação' ,
        initial = 23,
        end = 33
        )

    high_school = create_table_white_values_Unnamed(table = table, initial = 34, end = 39)

    new_table = pd.concat([elementary_school, high_school], axis=1)

    return new_table

def abandonment_rate(table: pd.DataFrame) -> pd.DataFrame:
    elementary_school = create_table_white_values_Unnamed(
        table=table, 
        value_default='Taxa de Abandono',
        initial=41,
        end=51
        )
    
    high_school = create_table_white_values_Unnamed(
        table = table, 
        initial=52,
        end=57
        )

    new_table = pd.concat([elementary_school, high_school], axis=1).dropna(how='any')

    return new_table

data_table = select_data_of_table_column(table,
        ['Unidade Geográfica',
        'Localização',
        'Dependência Administrativa']
)

table_approval = approval_rate(table=table)
table_failure = failure_rate(table=table)
table_abandonment = abandonment_rate(table=table)

total_approval_rate = float(sum(table_approval.loc[[2], ['Taxa de Aprovação']].values,
    table_approval.loc[[2], ['Unnamed: 16']].values))

total_failure_rate = float(sum(table_failure.loc[[2], ['Taxa de Reprovação']].values,
    table_failure.loc[[2], ['Unnamed: 34']].values))

total_abandonment_rate = float(sum(table_abandonment.loc[[2], ['Taxa de Abandono']].values,
    table_abandonment.loc[[2], ['Unnamed: 52']].values))

describe =  data_table.describe().columns

total = sum([total_approval_rate, total_failure_rate, total_abandonment_rate])
mean_approval = total_approval_rate / 3
mean_failure = total_failure_rate / 3
mean_abandonment = total_abandonment_rate / 3
