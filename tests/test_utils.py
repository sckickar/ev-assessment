import math
from app.utils import calculate_haversine_distance


def test_calculate_haversine_distance():
    lat1, lon1 = 40.7128, -74.0060
    lat2, lon2 = 51.5074, -0.1278

    distance = calculate_haversine_distance(lat1, lon1, lat2, lon2)

    assert math.isclose(distance, 5570, rel_tol=0.01)


def test_distance_to_self_is_zero():
    lat, lon = 10.0, 10.0
    distance = calculate_haversine_distance(lat, lon, lat, lon)
    assert distance == 0.0
