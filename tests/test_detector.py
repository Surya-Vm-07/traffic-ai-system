from src.detector import flag_violation, check_vehicles

def test_speeding_vehicle():
    assert flag_violation(85, 60) == True

def test_compliant_vehicle():
    assert flag_violation(55, 60) == False

def test_check_vehicles_returns_only_violators():
    data = [
        {"plate": "TN01AB1234", "speed": 85, "limit": 60},
        {"plate": "KA05CD5678", "speed": 55, "limit": 60},
    ]
    result = check_vehicles(data)
    assert len(result) == 1
    assert result[0]["plate"] == "TN01AB1234"