from interfaces import IBibtexReference

from quotationtool.referatory.i18n import _
import field


class IBook(IBibtexReference):
    """Book (BibTeX data model)"""

    author = field.Author(required = False)
    editor = field.Editor(required = False)
    title = field.Title(required = True, min_length = 1, default = (u"",))
    publisher = field.Publisher(required = True)
    year = field.Year(required = True)
    volume = field.Volume(required = False)
    number = field.Number(required = False)
    series = field.Series(required = False)
    address = field.Address(required = False)
    edition = field.Edition(required = False)
    month = field.Month(required = False)
    note = field.Note(required = False)
