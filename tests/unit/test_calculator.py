"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply, multiplication, division

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Adding negative numbers"""
        assert add(-2,-1) == -3
        assert add(-10,-5) == -15

    def test_subtract_negative_numbers(self):
        """Subtracting negative numbers"""
        assert subtract(-2,-3) == 1
        assert subtract(-10,-15) == 5

class TestMultiplyDiv:
    def test_multiply_positive_numbers(self):
        assert multiplication(3,4) == 12
        assert multiplication(2,8) == 16

    def test_divide_positive_numbers(self):
        assert division(15,3) == 5
        assert division(16,2) == 8
            
class TestSqrtPower:
    def test_root_positive_numbers(self):
        assert sqrt(25,5) == 5
        assert sqrt(36,6) == 6

    def test_power_positive_numbers(self):
        assert power(3,2) == 9
        assert power(5,3) == 125

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class