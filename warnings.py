import collections
import re

# lineNumber is the number that the warning appears on, type is a string of what type of warning it is,
biasWarning = collections.namedtuple('BiasWarning', ['lineNumber', 'type', 'warningMessage'])

BIAS_WARNINGS = []
# Strings, Variable, Class names
# Gender Associated Language
# he/him/his, she/her/hers

# String Constants
PRONOUNS = 'Pronouns'
GENDERED_LANGUAGE = 'Gendered Language'
PROBLEM_TERMS = 'Problem Terms'
LIBRARIES = 'import'
PLAINTEXT = 'plaintext'
VARIABLES = 'variable'

warnings = {
    PRONOUNS:'Found the usage of gendered pronoun: ',
    GENDERED_LANGUAGE:'Found a usage of gendered language: ',
    PROBLEM_TERMS:'Found the following term, when a more specific term may be more accurate: ',
    LIBRARIES:'Found a library that may contain gendered biases: '
}

# Errors


# Language Lists
language = {
    PRONOUNS: ['he', 'him', 'his', 'she', 'her', 'hers'],
    GENDERED_LANGUAGE: ['men', 'man', 'mankind', 'women', 'woman', 'grandfather', 'grandfathered'],
    PROBLEM_TERMS: ['slave', 'blacklist', 'whitelist', 'sanity', 'blackhat', 'whitehat', 'black hat', 'white hat'],
    LIBRARIES: []
}


# checks
# plaintext strings
# variable names
# libraries
def check(warning_type, data):
    for keyword in language[warning_type]:
        p = re.compile("[^a-z^A-Z](man)[^a-z^A-Z]", re.IGNORECASE)
        line_number = data[1]
        string = data[0]
        regex = "[^a-zA-Z0-9]({word})[^a-zA-Z0-9]|^({word})[^a-zA-Z0-9]|[^a-zA-Z0-9]({word})$".format(word=keyword)
        match = re.search(regex, string)
        if match is not None:
            BIAS_WARNINGS.append(biasWarning(line_number, warning_type, warnings[warning_type] + keyword))


def assembleWarning(parsed):
    BIAS_WARNINGS.clear()
    plaintext_list = parsed[PLAINTEXT]
    variables_list = parsed[VARIABLES]
    library_list = parsed[LIBRARIES]
    for data in plaintext_list:
        check(PROBLEM_TERMS, data)
        check(GENDERED_LANGUAGE, data)
        check(PRONOUNS, data)
    for data in variables_list:
        check(PROBLEM_TERMS, data)
        check(GENDERED_LANGUAGE, data)
    for data in library_list:
        check(LIBRARIES, data)
    return BIAS_WARNINGS

