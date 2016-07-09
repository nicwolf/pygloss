"""Silly linguistic translators.

Inspired by a problem from the Google Code
Jam that asked contestants to write a program that could translate 'alien'
numerical systems into arbitrarily many other 'alien' languages. See:

https://code.google.com/codejam/contest/dashboard?c=agxjb2RlamFtLXByb2RyEAsSCGNvbnRlc3RzGIP6AQw#

Notes
==========

Author
==========
Nicholas Wolf

Licencse
==========
TODO
"""


def translate_integer_string(number, source, target):
    r"""Translate a numeric string from one numeral system to another.

    From the original problem:

        The decimal numeral system is composed of ten digits, which we represent
        as "0123456789" (the digits in a system are written from lowest to
        highest). Imagine you have discovered an alien numeral system composed
        of some number of digits, which may or may not be the same as those used
        in decimal. For example, if the alien numeral system were represented as
        "oF8", then the numbers one through ten would be (F, 8, Fo, FF, F8, 8o,
        8F, 88, Foo, FoF). We would like to be able to work with numbers in
        arbitrary alien systems. More generally, we want to be able to convert
        an arbitrary number that's written in one alien system into a second
        alien system.

    Parameters
    ----------
    number : string
        Original numeric string
    source : string
        The numeral system of the source language --- e.g. decimal system would
        be represented by "0123456789", binary by "01".
    target : string
        The numeral system of the target language.

    Returns
    ----------
    translated_number : string
    
    Raises
    ----------
    TypeError
        If the 

    Notes
    ----------
    Assumes that both numeral systems are MSB. 

    Examples
    ----------
    >>> translate_number('12', '0123456789', '01')
    1100
    >>> translate_number('Foo', 'oF8', '0123456789')
    9
    """
    base_source = len(source)
    base_target = len(target)

    # First, convert the number to base 10
    base_10_number = 0
    # Iterate over each digit of the input number, starting with the least 
    # significant. 
    for i, n in enumerate(number[::-1]):
        base_10_number += base_source ** i * source.index(n)
    remainder = base_10_number % base_target
    quotient = base_10_number // base_target
    out_number_indices = [remainder]
    while quotient > 0:
        remainder = quotient % base_target
        out_number_indices.insert(0, remainder)
        quotient = (quotient - remainder) // base_target
    
    translated_number = ''.join([target[i] for i in out_number_indices])
    return translated_number

