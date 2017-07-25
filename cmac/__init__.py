"""

.. currentmodule:: cmac

X-SAPR CMAC function for determing gate ids, detect second trip returns and
more.

Functions
=========

.. autosummary::
    :toctree: generated/

    cmac
    quicklooks
    snr_and_sounding
    get_texture
    cum_score_fuzzy_logic
    do_my_fuzz
    return_csu_kdp
    retrieve_qvp

"""

from .cmac_xsapr import cmac
from .cmac_quicklooks import quicklooks
from .processing_code import snr_and_sounding, do_my_fuzz
from .processing_code import get_texture, cum_score_fuzzy_logic
from .processing_code import return_csu_kdp, retrieve_qvp

__all__ = [s for s in dir() if not s.startswith('_')]
