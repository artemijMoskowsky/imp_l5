import unittest
import doctest

def calculate_total_minutes(segments: list):
    """
    Рахує загальний час у хвилинах
    >>> calculate_total_minutes([10, 20, 30])
    60
    >>> calculate_total_minutes([])
    0
    """
    return sum(segments)

def format_travel_time(total_minutes):
    """
    Форматує хвилини в "години + хвилини"
    >>> format_travel_time(130)
    '2 год 10 хв'
    >>> format_travel_time(50)
    '0 год 50 хв'
    """
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} год {minutes} хв"

def main():
    route = [50, 70, 80]
    total = calculate_total_minutes(route)
    print(f"Загальний час: {format_travel_time(total)}")


# UNIT TESTS

class TestTravelFunctions(unittest.TestCase):
    def test_calculate_total_minutes(self):
        self.assertEqual(calculate_total_minutes([10, 20]), 30)
        self.assertEqual(calculate_total_minutes([]), 0)
    
    def test_format_travel_time(self):
        self.assertEqual(format_travel_time(150), '2 год 30 хв')
        self.assertEqual(format_travel_time(0), '0 год 0 хв')
        self.assertEqual(format_travel_time(40), '0 год 40 хв')

if __name__ == "__main__":
    doctest.testmod()

    unittest.main()
