from pathlib import Path

MODEL_MAPPING = dict(
    location=Path('data'),
    location_type='directory',
    data_format='json',
    id_key='country',
    column_names={
        'List_C1Factors_Crops': 'crop',
        'List_C1Factors': 'c1',
        }
)