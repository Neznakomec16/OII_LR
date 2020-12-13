experience_affiliation = [[0, 0, 2, 5], [3, 5, 10, 13], [9, 14, 42, 42]]
age_affiliation = [[18, 18, 26, 30], [27, 31, 38, 41], [39, 51, 60, 60]]


def get_age_affiliations(value):
    value = float(value)
    return {
        'small': _get_affiliation(value, age_affiliation[0]),
        'middle': _get_affiliation(value, age_affiliation[1]),
        'big': _get_affiliation(value, age_affiliation[2]),
    }


def get_experience_affiliations(value):
    value = float(value)
    return {
        'small': _get_affiliation(value, experience_affiliation[0]),
        'middle': _get_affiliation(value, experience_affiliation[1]),
        'big': _get_affiliation(value, experience_affiliation[2]),
    }


def _get_affiliation(value, dots):
    if dots[0] <= value <= dots[1]:
        return round(1 - (dots[1] - value) / (dots[1] - dots[0]), 3)
    elif dots[1] <= value <= dots[2]:
        return 1
    elif dots[2] <= value <= dots[3]:
        return round(1 - (value - dots[2]) / (dots[3] - dots[2]), 3)
    return 0


def get_temperature_affiliation(temperature: float):
    if 0 < temperature <= 50:
        high = 0
        middle = round(1 - (50 - temperature) / 50, 3)
        low = 1
    elif 50 <= temperature <= 100:
        high = round(1 - (100 - temperature) / 50, 3)
        middle = 1
        low = round(1 - (temperature - 50) / 50, 3)
    elif temperature >= 100:
        high = 1
        middle = round(1 - (temperature - 100) / 50, 3)
        low = 0
    else:
        low = middle = high = -1
    return low, middle, high


def get_consumption_affiliation(consumption: float):
    if 0 < consumption <= 4:
        high = 0
        middle = round(1 - (4 - consumption) / 2, 3)
        low = round(1 - (2 - consumption) / 2, 3) if consumption <= 2 else round(1 - (consumption - 2) / 2, 3)
    elif consumption > 4:
        high = round(1 - (6 - consumption) / 2, 3) if consumption <= 6 else round(1 - (consumption - 2) / 2, 3)
        middle = round(1 - (consumption - 4) / 2, 3) if consumption <= 6 else 0
        low = 0
    else:
        low = middle = high = -1
    return low, middle, high


def get_pressure_affiliation(pressure: float):
    if 0 < pressure <= 100:
        high = round(1 - (100 - pressure) / 100, 3)
        middle = round(1 - (100 - pressure) / 100, 3) if pressure < 50 else round(1 - (pressure - 50) / 100, 3)
        low = round(1 - pressure / 100, 3)
    else:
        low = middle = high = -1
    return low, middle, high


def rule_small(number: float):
    if number < 0.25:
        return - number * 25 + 100
    return 25


def rule_middle(number: float):
    return 100 - 50 * number


def rule_high(number: float):
    return 75 * number if number < 0.75 else 0.75


def fasification(temperature, consumption, pressure):
    return {
        'temperature': {
            k: v for k, v in zip(['low', 'middle', 'high'], get_temperature_affiliation(temperature))
        },
        'consumption': {
            k: v for k, v in zip(['low', 'middle', 'high'], get_consumption_affiliation(consumption))
        },
        'pressure': {
            k: v for k, v in zip(['low', 'middle', 'high'], get_pressure_affiliation(pressure))
        }
    }
