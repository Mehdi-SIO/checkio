text = ""

def find_message(text):
    result = ""
    size = len(text)
    for i in range(0, size):
        if text[i].isupper():
            result += text[i]
    """Find a secret message"""
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message(u"How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message(u"hello world!") == "", "Nothing"
    assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print('ok')

