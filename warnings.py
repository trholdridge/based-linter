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
LIBRARIES = 'Libraries'
PLAINTEXT = 'Plaintext'
VARIABLES = 'Variable'

warnings = {
    PRONOUNS: 'Found the usage of the gendered pronoun "{term}": ',
    GENDERED_LANGUAGE: 'Found a usage of gendered language "{term}": ',
    PROBLEM_TERMS: 'Found the usage of the term "{term}", when a more specific term may be more accurate: ',
    LIBRARIES: 'Found the library "{term}" that may contain gendered biases: '
}

alternatives = collections.defaultdict(lambda a:
                                       "{term} as a term has several meanings, you may have to do more research to "
                                       "find a good alternative.\n We recommend starting at Google's style wordlist: "
                                       "https://developers.google.com/style/word-list")
alternatives['mankind'] = 'humanity, humankind'
alternatives['man'] = 'If using "man" to refer to a generic person'

# Language Lists
language = {
    PRONOUNS: ['he', 'him', 'his', 'she', 'her', 'hers'],
    GENDERED_LANGUAGE: ['men', 'man', 'mankind', 'women', 'woman', 'grandfather', 'grandfathered', 'female', 'male'],
    PROBLEM_TERMS: ['master', 'slave', 'blacklist', 'whitelist', 'sanity', 'sane', 'crazy', 'blackhat', 'whitehat',
                    'black hat', 'white hat', 'lame', ],
    LIBRARIES: ['word2vec', 'fasttext', 'glove']
}


def check(warning_type, data):
    for keyword in language[warning_type]:
        # p = re.compile("[^a-z^A-Z](man)[^a-z^A-Z]", re.IGNORECASE)
        line_number = data[1]
        string = data[0]
        regex = "[^a-zA-Z0-9]({word})[^a-zA-Z0-9]|^({word})[^a-zA-Z0-9]|[^a-zA-Z0-9]({word})$|(^{word}$)".format(word=keyword)
        match = re.search(regex, string, re.IGNORECASE)
        if match is not None:
            BIAS_WARNINGS.append(
                biasWarning(line_number, warning_type, warnings[warning_type].format(term=keyword) + string))


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
    BIAS_WARNINGS.sort(key=lambda a: a.lineNumber)
    return BIAS_WARNINGS
