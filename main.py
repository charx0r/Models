from hestia.crop_builder import FarmedCropBuilder
from hestia.data_client.file_writers.json_writer import JsonWriter
from pathlib import Path

if __name__ == '__main__':
    writer = JsonWriter(Path('./'))
    builder = FarmedCropBuilder()
    crop = builder.build_crop(1041)
    writer.write(crop, 'crop20')