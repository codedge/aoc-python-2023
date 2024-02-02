from d1.calibration import calibrate_p1, calibrate_p2


def test_calibrate_p1():
    assert 54390 == calibrate_p1()


def test_calibrate_p2():
    assert 54277 == calibrate_p2()
