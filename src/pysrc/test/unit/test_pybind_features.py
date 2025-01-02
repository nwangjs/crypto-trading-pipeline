import pytest
from pysrc import intern


def test_pybind_features() -> None:
    ntf = intern.NTradesFeature()
    assert ntf.compute_feature([(1, 1, False)]) == 1
    assert ntf.compute_feature([(2, 1, False), (2, 2, True)]) == 2

    ptf = intern.PercentBuyFeature()
    assert abs(ptf.compute_feature([(1, 1, False)]) - 0) < 1e-2
    assert abs(ptf.compute_feature([(1, 1, False), (1, 1, True)]) - 0.5) < 1e-2
    assert abs(ptf.compute_feature([(1, 1, True)]) - 1) < 1e-2

    psf = intern.PercentSellFeature()
    assert abs(psf.compute_feature([(1, 1, False)]) - 1) < 1e-2
    assert abs(psf.compute_feature([(1, 1, False), (1, 1, True)]) - 0.5) < 1e-2
    assert (
        abs(psf.compute_feature([(1, 1, False), (1, 1, True), (1, 2, False)]) - 0.67)
        < 1e-2
    )

    vf = intern.FiveTickVolumeFeature()
    assert vf.compute_feature([(2, 1, False)]) == 1
    assert vf.compute_feature([(1, 1, False)]) == 2
    assert vf.compute_feature([(1, 1, False), (1, 1, True)]) == 4
    assert vf.compute_feature([(1, 1, False), (1, 1, True)]) == 6
    assert vf.compute_feature([(2, 1, False), (1, 1, True)]) == 8
    assert vf.compute_feature([(1, 1, False), (1, 1, True)]) == 9
    assert vf.compute_feature([(2, 1, False), (1, 1, True)]) == 10
