def checkio(text):
    "Convert Euro style currency in dollars to US/UK style"
    text = text.split(" ")
    out = []
    flag = 0
    for elem in text:
        if '$' in elem:
            if elem.count(',') > 1 and '.' not in elem:
                out.append(elem)
                continue
            if elem[-1] == ',':
                elem = elem[:-1]
                flag = 1
            if elem[-1] == '.':
                elem = elem[:-1]
                flag = 2
            try:
                if elem[-3] != '.':
                    elem = elem.replace('.', '#').replace(',', '.').replace('#', ',')
            except IndexError:
                pass
            if flag == 1:
                elem = elem + ','
                flag = 0
            if flag == 2:
                elem = elem + '.'
                flag = 0
        out.append(elem)
    return ' '.join(out)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
           "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
           "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
           "$1,234, $5,678 and $9", "Dollars without cents"

print(checkio("$4.545,45 is less than $5,454.54."))


