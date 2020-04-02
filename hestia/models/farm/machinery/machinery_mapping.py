from pathlib import Path

MODEL_MAPPING = dict(
    location=Path('data/database.csv'),
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'NN': 'amount',
        'NM': 'fuel_amount',
        'NO': 'hours'
        }
)