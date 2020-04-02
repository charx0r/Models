from pathlib import Path

DATA_MAPPING = dict(
    location= Path('data/database.csv'),
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names= {
        'id': 'AQ'
    }
)