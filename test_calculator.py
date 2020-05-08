"""
Unit tests for calculator
"""
import calculator
 
class TestCalculator:
  def test_addition(self):
    assert 4 == calculator.add(1, 3)
    assert 15000 == calculator.add(10000, 5000)
    assert 0 == calculator.add(-10, 10)
    

  def test_subtraction(self):
    assert 8 == calculator.subtract(10, 2)

  def test_multiply(self):
    assert 20 == calculator.test_multiply(10, 2)