"""
Global config singlet
"""
_conf = {
    "DATA_ANALYTIC_DEFAULT_1D": "wesseling",
    "DATA_NUMERICAL_DEFAULT_3D": "solvcon",
    "DATA_NUMERICAL_1D": "wesseling",
    "DATA_NUMERICAL_3D": "solvcon",
    "DATA_NUMERICAL_3D_SOLVCON_INPUT_FLAG": None,
    "VIEW_EXCLUDE_LOCATION_STATIC": None,
    "VIEW_EXCLUDE_LOCATION_DYNAMIC": "interface",
    "VIEW_EXCLUDE_TIME_STATIC": None,
    "VIEW_EXCLUDE_TIME_DYNAMIC": None,
    "VIEW_DERIVED_RHO_X": None,
    "VIEW_DERIVED_RHO_Y": None,
    "VIEW_DERIVED_V_MAGANITUDE_X": None,
    "VIEW_DERIVED_V_MAGANITUDE_Y": None,
    "VIEW_DERIVED_P_X": None,
    "VIEW_DERIVED_P_Y": None,
}


class Config:
    def __init__(self):
        self._config = _conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]

class BenchmarkConfig(Config):

    @property
    def view_derived_v_maganitude_y(self):
        return self.get_property("VIEW_DERIVED_V_MAGANITUDE_Y")
