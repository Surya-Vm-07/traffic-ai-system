def flag_violation(speed: int, limit: int) -> bool:
    """Returns True if the vehicle is speeding."""
    return speed > limit

def check_vehicles(vehicles: list[dict]) -> list[dict]:
    """Takes a list of vehicle records and returns only violators."""
    return [v for v in vehicles if flag_violation(v["speed"], v["limit"])]

if __name__ == "__main__":
    test_data = [
        {"plate": "TN01AB1234", "speed": 85, "limit": 60},
        {"plate": "KA05CD5678", "speed": 55, "limit": 60},
        {"plate": "MH12EF9012", "speed": 110, "limit": 80},
    ]
    violations = check_vehicles(test_data)
    print(f"Violations detected: {len(violations)}")
    for v in violations:
        print(f"  Plate: {v['plate']} | Speed: {v['speed']} | Limit: {v['limit']}")