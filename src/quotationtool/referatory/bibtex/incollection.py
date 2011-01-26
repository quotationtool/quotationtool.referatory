from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from iincollection import IIncollection
from bibtexreference import BibtexReference

class Incollection(BibtexReference):
    """Implementation of a incollection"""

    implements(IIncollection)

    author = FieldProperty(IIncollection['author'])
    title = FieldProperty(IIncollection['title'])
    booktitle = FieldProperty(IIncollection['booktitle'])
    editor = FieldProperty(IIncollection['editor'])
    publisher = FieldProperty(IIncollection['publisher'])
    year = FieldProperty(IIncollection['year'])
    volume = FieldProperty(IIncollection['volume'])
    number = FieldProperty(IIncollection['number'])
    series = FieldProperty(IIncollection['series'])
    type_ = FieldProperty(IIncollection['type_'])
    chapter = FieldProperty(IIncollection['chapter'])
    pages = FieldProperty(IIncollection['pages'])
    address = FieldProperty(IIncollection['address'])
    edition = FieldProperty(IIncollection['edition'])
    month = FieldProperty(IIncollection['month'])
    note = FieldProperty(IIncollection['note'])
