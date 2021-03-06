text = ""
def checkio(text):
    tri = sorted(text.lower())
    most_wanted_letter = ""
    max = 0
    size = len(tri)

    for i in range(0, size):
        if str(tri[i]).isalpha() and tri.count(tri[i]) > max:
            most_wanted_letter = tri[i]
            max = tri.count(tri[i])

    return most_wanted_letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")

