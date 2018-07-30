from string import ascii_uppercase


def from_camel_case(name):
    output = ''

    for i in range(len(name)):
        if name[i] in ascii_uppercase:
            if i == 0:
                output += name[i].lower()
            else:
                output += "_" + name[i].lower()
        else:
            output += name[i]
    return output


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")

print(from_camel_case("MyFunctionName"))
