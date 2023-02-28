from python_primes.global_functions.detect_primes import *

def test_prime_one():
    assert detect_prime(1) == False
def test_prime_two():
    assert detect_prime(2) == True
def test_prime_three():
    assert detect_prime(3) == True
def test_prime_four():
    assert detect_prime(99) == False
def test_prime_five():
    assert detect_prime(113) == True
def test_prime_six():
    assert detect_prime(119) == False
