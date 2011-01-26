from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from iarticle import IArticle
from bibtexreference import BibtexReference

class Article(BibtexReference):
    """Implementation of a article"""

    implements(IArticle)

    author = FieldProperty(IArticle['author'])
    title = FieldProperty(IArticle['title'])
    journal = FieldProperty(IArticle['journal'])
    year = FieldProperty(IArticle['year'])
    volume = FieldProperty(IArticle['volume'])
    number = FieldProperty(IArticle['number'])
    pages = FieldProperty(IArticle['pages'])
    month = FieldProperty(IArticle['month'])
    note = FieldProperty(IArticle['note'])
