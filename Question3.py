# START

def camel_to_hyphen(text: str) -> str:
    """
    Converts a string from camelCase to hyphen-case.
    """

    result = []

    for char in text:
        if char.isupper():
            result.append("-" + char.lower())
        else:
            result.append(char)

    return "".join(result)

# print(camel_to_hyphen("helloPython")) -> hello-python

# STOP