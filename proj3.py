import re
source = open('textlines.txt')
Irving = source.read()
def between_the_lines(fang):
    if type(fang) != str:
        raise TypeError('Not a String')
    result = re.findall('[A-Za-z]+at\\b', fang)
    query = []
    for element in result:
        if len(element) > 3:
            query.append(element)
    return query
between_the_lines(Irving)
