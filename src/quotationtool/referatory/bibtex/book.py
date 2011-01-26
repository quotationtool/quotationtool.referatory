from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from ibook import IBook
from bibtexreference import BibtexReference


class Book(BibtexReference):
    """Implementation of a book"""

    implements(IBook)

    author = FieldProperty(IBook['author'])
    editor = FieldProperty(IBook['editor'])
    title = FieldProperty(IBook['title'])
    publisher = FieldProperty(IBook['publisher'])
    year = FieldProperty(IBook['year'])
    volume = FieldProperty(IBook['volume'])
    number = FieldProperty(IBook['number'])
    series = FieldProperty(IBook['series'])
    address = FieldProperty(IBook['address'])
    edition = FieldProperty(IBook['edition'])
    month = FieldProperty(IBook['month'])
    note = FieldProperty(IBook['note'])
