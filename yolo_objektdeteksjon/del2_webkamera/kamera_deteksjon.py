from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


_ORIGINAL_FIL = (
    Path(__file__).resolve().parents[2]
    / "yolo-objektdeteksjon"
    / "del2_webkamera"
    / "kamera_deteksjon.py"
)

_SPESIFIKASJON = spec_from_file_location("original_kamera_deteksjon", _ORIGINAL_FIL)
if _SPESIFIKASJON is None or _SPESIFIKASJON.loader is None:
    raise ImportError(f"Kunne ikke laste modul fra {_ORIGINAL_FIL}")

_MODUL = module_from_spec(_SPESIFIKASJON)
_SPESIFIKASJON.loader.exec_module(_MODUL)

kamera_deteksjon = _MODUL.kamera_deteksjon

__all__ = ["kamera_deteksjon"]