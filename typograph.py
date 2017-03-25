import re


def replace_quotes(text):
    text = re.sub(r'([\'"])(.*?)(\1)(?![^<]*>)', r'&laquo;\2&raquo;', text)
    return text


def correct_phone_numbers(number):
    number = re.sub(r'([0-9]{2,4})\-([0-9]{2,4})\-([0-9]{2,4})(?![^<]*>)',
                    r'\1{0}\2{0}\3'.format('&ndash;'), number)
    return number


def delete_extra_spaces(text):
    text = re.sub(r'{0}{{2,}}'.format(' '), ' ', text)
    text = re.sub(r'(?:^{0}+|{0}+$)'.format(' '), '', text)
    text = text.replace('\n ', '\n')
    return text


def replace_special_symbols(text):
    text = text.replace('№', '&#8470;')
    text = text.replace('(R)', '&reg;')
    text = text.replace('+-', '&plusmn;')
    text = text.replace('(С)', '&copy;')
    text = text.replace('...', '&hellip;')
    return text


def replace_hyphen_by_dash(text):
    text = re.sub(r'({0}(за|под|то|либо|нибудь|ли))'.format('-'),
                  r'{0}\2'.format('&ndash;'), text)
    text = text.replace('--', '&mdash;')
    text = text.replace('-', '&mdash;')
    return text


def add_nonbreakable_spaces(text):
    whitespace = ' '
    words = r'[^\W\d_]'
    nonbreakable_space = '&nbsp;'
    text = re.sub(
        r'\b(\d{{1,3}}){0}(?=[0-9]+\b|{1}|{2})(?![^<]*>)'.format(
            whitespace,
            words,
            r'[\-{0}\*xх{1}\+\=±≤≥≠÷\/]'.format('−', '×')),
        r'\1' + nonbreakable_space,
        text)
    text = re.sub(
        r'\b({1}{{1,2}}){0}+(?![^<]*>)'.format(whitespace, words),
        r'\1' + nonbreakable_space,
        text)
    return text


def typograph(text):
    if not text:
        return "Введена пустая строка"
    text_after_typograph = add_nonbreakable_spaces(
        replace_hyphen_by_dash(
            replace_special_symbols(
                delete_extra_spaces(
                    correct_phone_numbers(
                        replace_quotes(text)
                    )
                )
            )
        )
    )
    return text_after_typograph
