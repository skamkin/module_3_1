calls=0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    i = (len(string), string.upper(), string.lower())
    return i


def is_contains(string, list_to):
    count_calls()
    if string.lower() in list(map(lambda a: a.lower(), list_to)):
        return True
    else:
        return False



print(string_info('Sergey'))
print(string_info('Kamkin'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
count_calls()
print(calls)
