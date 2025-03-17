import pytest
from your_module import calculate_discount

def test_vip_discount():
    assert calculate_discount(200, "VIP") == 180.0

def test_high_purchase_discount():
    assert calculate_discount(600, "Regular") == 480.0

def test_no_discount():
    assert calculate_discount(100, "Regular") == 100.0

def test_edge_case_500():
    assert calculate_discount(500, "Regular") == 500.0

def test_vip_and_high_purchase():
    assert calculate_discount(600, "VIP") == 540.0

def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_discount(-100, "VIP")

def test_unknown_customer_type():
    with pytest.raises(ValueError):
        calculate_discount(200, "Alien")