Ovaltine: a Secret Encoding Decoder Ring for Python
===================================================

**Ovaltine** (extracted from Requests) is a simple Python library for
working with unicode embedded within an undeterministic encoding.

For example, many web servers lie about what encoding their responses are.
You can use Ovaltine, which in turn uses chardet, to detect the apparent
encoding and get back as much usable data as possible.

Usage
-----

Simply get back unicode, no matter what::

    >>> import ovaltine

    >>> ovaltine.drink(b'foo bar')
    u'foo bar'

Or, for more advanced usage::

    >>> from ovaltine import DecoderRing

    >>> content = requests.get('https://kennethreitz.org/').content
    >>> r = DecoderRing(content)

    >>> r
    <DecoderRing len=74773, encoding=None, apparently='ISO-8859-2'>
    >>> r.apparently
    'ISO-8859-2'
    >>> r.text
    ... # Unicode is shown here.

    # Set the encoding yourself.
    >>> r.encoding = 'UTF-8'
    >>> r.text
    ... # Unicode is shown here.

