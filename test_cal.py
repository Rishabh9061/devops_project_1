import pytest
from cal import sum

def test_code():
	a = 5
	b = 10
	assert sum(a,b) == 15
test_code()