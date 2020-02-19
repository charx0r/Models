from hestia.models.crops.crop_characteristics import CropCharacteristics
from hestia.models.crops.crop_characteristics_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory


class CropCharacteristicsFactory(ModelFactory):
    def _gapfill(self, data_fame):
        pass

    def __init__(self):
        super().__init__()

    def create(self,key):
        data_row = self._get_record(key)
        instance = CropCharacteristics()
        return self._map(instance, data_row)

    def _map(self,instance, data_row):
        instance.crop_name=data_row['crop_name']
        instance.crop_root_depth=['crop_root_depth']
        return instance

    def _get_record(self, key):
        df = self._data_frame
        if df is None:
            df = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        return data_table.loc[key]