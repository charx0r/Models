from ...farmed_crop import FarmedCrop

class MachineryFuelEmissions:
    co2: float
    so2: float
    po4: float

    def __init__(self, crop: FarmedCrop):
        self._crop = crop
    