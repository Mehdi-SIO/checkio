#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
    result = []
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    #if number % 3 == 0 and number % 5 == 0:
    #    result = "Fizz Buzz"
    if number % 3 == 0:
        result.append("Fizz")
    if number % 5 == 0:
        result.append("Buzz")
    if number % 10 == 0:
        result.append("Cat")

    #replace this for solution
    return " ".join(result)
#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(10) == "Buzz Cat", "5 is divisible by 5"
    #assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print "ok"
