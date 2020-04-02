from pathlib import Path

MODEL_MAPPING = dict(
    location=Path('data/database.csv'),
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'NR': 'type',
        'NS': 'amount_applied',
        'NU': 'energy_fuel',
        'NT': 'energy_electr'
        }
)
