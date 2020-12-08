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
