from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.pesticides.pesticide_management import PesticideManagement, Pesticide
from hestia.models.activities.pesticides.pesticide_management_mapping import MODEL_MAPPING


class PestsManagementFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data = self._data_frame
        if data is None:
            data = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        # use data_table to get gapfills
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        pass

    def create(self, key):
        record = self._get_record(key)

        instance = PesticideManagement()
        instance.pest1 = Pesticide(record['pest1_name'], record['pest1_amount'])
        instance.pest2 = Pesticide(record['pest2_name'], record['pest2_amount'])
        instance.pest3 = Pesticide(record['pest3_name'], record['pest3_amount'])

        return instance
