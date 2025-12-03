# Testing the snake_to_camel Function
import pytest
from snake_to_camel_solutions import snake_to_camel

def test_default_lower_camel():
    # default parameter (lower_camel=True)
    assert snake_to_camel('variable_name') == 'variableName'

def test_explicit_lower_camel_true():
    # explicitly passing lower_camel=True
    assert snake_to_camel('variable_name', lower_camel=True) == 'variableName'

def test_upper_camel():
    # converting to UpperCamelCase
    assert snake_to_camel('variable_name', lower_camel=False) == 'VariableName'

def test_long_variable_lower_camel():
    # longer snake_case variable
    assert snake_to_camel('some_long_variable_name', lower_camel=True) == 'someLongVariableName'

def test_leading_underscore_lower_camel():
    # leading underscore edge case
    assert snake_to_camel('_variable_name', lower_camel=True) == 'variableName'

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

