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
LIBRARIES = 'libraries'
PLAINTEXT = 'plaintext'
VARIABLES = 'variables'

warnings = {
    PRONOUNS:'Found the usage of gendered pronoun: ',
    GENDERED_LANGUAGE:'Found a usage of gendered language: ',
    PROBLEM_TERMS:'Found the following term, when a more specific term may be more accurate: ',
    LIBRARIES:'Found a library that may contain gendered biases: '
}

# Errors


# Language Lists
language = {
    PRONOUNS: ['he', 'him', ' his', 'she', 'her', 'hers'],
    GENDERED_LANGUAGE: ['men', 'mankind', 'women', 'grandfather', 'grandfathered'],
    PROBLEM_TERMS: ['slave', 'blacklist', 'whitelist', 'sanity', 'blackhat', 'whitehat', 'black hat', 'white hat'],
    LIBRARIES: []
}


# checks
# plaintext strings
# variable names
# libraries
def check(type, data):
    for keyword in language[type]:
        for ele in data:
            lineNumber = ele[0]
            string = ele[1]
            p = re.compile("\b({string})\b", re.IGNORECASE)
            match = p.search(string)
            if match:
                BIAS_WARNINGS.append(biasWarning(lineNumber, type, warnings[type] + keyword))


def assembleWarning():
    dict = {}
    plaintext_list = dict[PLAINTEXT]
    variables_list = dict[VARIABLES]
    library_list = dict[LIBRARIES]
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

