from interfaces import IBibtexReference

from quotationtool.referatory.i18n import _
import field


class IIncollection(IBibtexReference):
    """Incollection (BibTeX data model)"""

    author = field.Author(required = True, min_length = 1, default = (u"",))
    title = field.Title(required = True, min_length = 1, default = (u"",))
    booktitle = field.Booktitle(required = True, min_length = 1, default = (u"",))
    editor = field.Editor(required = False)
    publisher = field.Publisher(required = True)
    year = field.Year(required = True)
    volume = field.Volume(required = False)
    number = field.Number(required = False)
    series = field.Series(required = False)
    type_ = field.Type(required = False)
    chapter = field.Chapter(required = False)
    pages = field.Pages(required = False)
    address = field.Address(required = False)
    edition = field.Edition(required = False)
    month = field.Month(required = False)
    note = field.Note(required = False)
