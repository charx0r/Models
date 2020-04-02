from pathlib import Path

MODEL_MAPPING = dict(
    location=Path('data/database.csv'),
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'MI': 'crop_name',
        'OU': 'crop_root_depth'
        }
)
