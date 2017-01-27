import sys

import chardet

# Version Hacking
# ---------------

_ver = sys.version_info
is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)

if is_py2:
    str = unicode
elif is_py3:
    str = str


def drink(content, encoding=None):
    """Will attempt to turn any given bytes into unicode, and attempt
    to use the given encoding.
    """

    ring = DecoderRing(content)
    ring.encoding = encoding
    return ring.text


class DecoderRing(object):
    """A secret decoder ring, which decodes secret messages (e.g. bytes
    of unknown, or simply undeterministic, encoding).
    """
    def __init__(self, content):
        super(DecoderRing, self).__init__()
        self.content = content
        self.encoding = None

    def __repr__(self):
        return '<DecoderRing len={0!r}, encoding={1!r}, apparently={2!r}>'.format(len(self.content), self.encoding, self.apparently)

    @property
    def apparently(self):
        """Returns the apparent encoding of the content."""
        return chardet.detect(self.content)['encoding']

    @property
    def text(self):
        """Returns the unicode representation of the content."""

        encoding = self.encoding

        # Fallback to auto-detected encoding.
        if self.encoding is None:
            encoding = self.apparently

        # Decode unicode from given encoding.
        try:
            content = str(self.content, encoding, errors='replace')
        except (LookupError, TypeError):
            # A LookupError is raised if the encoding was not found which could
            # indicate a misspelling or similar mistake.
            #
            # A TypeError can be raised if encoding is None.
            #
            # So we try blindly encoding.
            content = str(self.content, error='replace')

        return content
