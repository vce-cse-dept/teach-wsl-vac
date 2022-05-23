def palindrome(n):
    if(str(n)==str(n[::-1])):
        return True
    return False

print ("111 is a palindrome : " +palindrome(111))