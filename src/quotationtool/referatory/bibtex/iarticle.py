from interfaces import IBibtexReference

from quotationtool.referatory.i18n import _
import field


class IArticle(IBibtexReference):
    """Article (BibTeX data model)"""

    author = field.Author(required = False, min_length = 1, default = (u"",))
    title = field.Title(required = True, min_length = 1, default = (u"",))
    journal = field.Journal(required = True)
    year = field.Year(required = True)
    volume = field.Volume(required = False)
    number = field.Number(required = False)
    pages = field.Pages(required = False)
    month = field.Month(required = False)
    note = field.Note(required = False)
