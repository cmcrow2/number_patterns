# this function takes a number and evaluates whether the number is prime or not

def detect_prime(num):
    # two edge cases (1 & 2)
    if num == 1:
        print("false") 
        return False
    if num == 2: 
        print("true")
        return True

    # modding by two first eliminates all even numbers immediately
    if num % 2 == 0:
        print("even", num)
        return False


    mod_num = 3
    # iterates through all the odds up to the mid point
    while mod_num <= num / 2:
        # if you have found a factor, the number is not prime
        if num % mod_num == 0:
            print("false", num, mod_num)
            return False
        # increase mod_num by two to go to the next prime number
        mod_num += 2
    
    # the loop ended, so the number has to be prime!
    print("true", num)
    return True

# detect_prime(15)
