from pathlib import Path

MODEL_MAPPING = dict(
    location=Path('data'),
    location_type='directory',
    data_format='json',
    separator='|',
    id_key='value',
    column_names={
        # ToDO: create List_Climate_Name '': 'name',
        'List_Climate_Zone': 'value',
        'List_Climate_Class': 'class',
        'List_Climate_N2ON': 'n2o_n',
        'List_Climate_NOxN': 'nox_n'
    }
)