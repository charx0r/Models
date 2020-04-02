from pathlib import Path

MODEL_MAPPING = dict(
    location=Path('data'),
    location_type='directory',
    data_format='json',
    id_key='country',
    column_names={
        'List_FAO_Countries_H': 'country',
        'List_C2Factors_Ctry': 'c2',
        }
)