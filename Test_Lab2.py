import Lab2 as temperature

def test_find_min_max():
    expected_result_min_max=[11,99]
    array_list=[64, 34, 25, 12, 21, 11, 99]
    assert (temperature.calc_min_max_temperature(array_list)==expected_result_min_max)

def test_calc_average():
    expected_result_average= 38
    array_list=[64, 34, 25, 12, 21, 11, 99]
    assert (temperature.calc_average(array_list)==expected_result_average)

def test_calc_median_temperature():
    expected_result_median=25
    array_list=[11, 12, 21, 25, 34, 64, 99]
    assert (temperature.calc_median_temperature(array_list)==expected_result_median)
    