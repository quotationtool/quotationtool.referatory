# -*- coding: utf-8 -*-

from zope.interface import implements
from zope import schema

from quotationtool.referatory.i18n import _
import ifield


## # boilerplate code
## class Xxx(schema.TextLine):
##     __doc__ = ifield.IXxx.__doc__

##     implements(ifield.IXxx)

##     def __init__(self, *args, **kw):
##         d = {
##             'title': _('bibtex-xxx-title', u""),
##             'description': _('bibtex-xxx-desc', u""),
##             }
##         for key, value in kw.items():
##             d[key] = value
##         super(Xxx, self).__init__(*args, **d)


class Language(schema.Choice):
    __doc__ = ifield.ILanguage.__doc__

    implements(ifield.ILanguage)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-language-title', u"Language"),
            'description': _('bibtex-language-desc', u"The language of the publication."),
            'vocabulary': 'z3c.i18n.iso.languages',
            'default': 'de',
            }
        for key, value in kw.items():
            d[key] = value
        super(Language, self).__init__(*args, **d)


class Name(schema.TextLine):
    __doc__ = ifield.IName.__doc__

    implements(ifield.IName)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-name-title', u"Name"),
            'description': _('bibtex-name-desc', u"Enter <i>last name, first name</i>."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Name, self).__init__(*args, **d)


class Author(schema.Tuple):
    __doc__ = ifield.IAuthor.__doc__

    implements(ifield.IAuthor)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-author-title', u"Author"),
            'description': _('bibtex-author-desc', u"Enter <i>last name, first name</i>. Each name goes into a seperate line."),
            'value_type': Name(required = True),
            }
        for key, value in kw.items():
            d[key] = value
        super(Author, self).__init__(*args, **d)


class Editor(schema.Tuple):
    __doc__ = ifield.IEditor.__doc__

    implements(ifield.IEditor)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-editor-title', u"Editor"),
            'description': _('bibtex-editor-desc', u"Enter <i>last name, first name</i>. Each name goes into a seperate line. If there is also an author field, then the editor field gives the editor of the book or collection in which the reference appears."),
            'value_type': Name(required = True),
            }
        for key, value in kw.items():
            d[key] = value
        super(Editor, self).__init__(*args, **d)


class TitleTupleItem(schema.TextLine):
    __doc__ = ifield.ITitleTupleItem.__doc__

    implements(ifield.ITitleTupleItem)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-titleitem-title', u"Title"),
            'description': _('bibtex-titleitem-desc', u"Without trailing dot or comma."),
            }
        for key, value in kw.items():
            d[key] = value
        super(TitleTupleItem, self).__init__(*args, **d)


class Title(schema.Tuple):
    __doc__ = ifield.ITitle.__doc__

    implements(ifield.ITitle)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-title-title', u"Title"),
            'description': _('bibtex-title-desc', u"Title, maintitle, subtitle, second subtitle etc. They all go into seperate lines. Without trailing dot or comma."),
            'value_type': TitleTupleItem(required = True),
            }
        for key, value in kw.items():
            d[key] = value
        super(Title, self).__init__(*args, **d)


class Publisher(schema.TextLine):
    __doc__ = ifield.IPublisher.__doc__

    implements(ifield.IPublisher)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-publisher-title', u"Publisher"),
            'description': _('bibtex-publisher-desc', u"The name of the publisher or publishing house."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Publisher, self).__init__(*args, **d)


class Year(schema.TextLine):
    __doc__ = ifield.IYear.__doc__

    implements(ifield.IYear)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-year-title', u"Year"),
            'description': _('bibtex-year-desc', u"The year of publication or, for an unpublished work, the year it was written. Generally it should consist of four numerals, such as 1984, although this website can handle any year whose last four nonpunctuation characters are numerals, such as `(about 1984)'."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Year, self).__init__(*args, **d)


class Volume(schema.TextLine):
    __doc__ = ifield.IVolume.__doc__

    implements(ifield.IVolume)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-volume-title', u"Volume"),
            'description': _('bibtex-volume-desc', u"The volume of a journal or multivolume book."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Volume, self).__init__(*args, **d)


class Number(schema.TextLine):
    __doc__ = ifield.INumber.__doc__

    implements(ifield.INumber)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-number-title', u"Number"),
            'description': _('bibtex-number-desc', u"The number of a journal, magazine, technical report, or of a work in a series. An issue of a journal or magazine is usually identified by its volume and number; the organization that issues a technical report usually gives it a number; and sometimes books are given numbers in a named series."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Number, self).__init__(*args, **d)


class Series(schema.TextLine):
    __doc__ = ifield.ISeries.__doc__

    implements(ifield.ISeries)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-series-title', u"Series"),
            'description': _('bibtex-series-desc', u"The name of a series or set of books. When citing an entire book, then the title field gives its title and an optional series field gives the name of a series or multi-volume set in which the book is published."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Series, self).__init__(*args, **d)


class Address(schema.TextLine):
    __doc__ = ifield.IAddress.__doc__

    implements(ifield.IAddress)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-address-title', u"Address"),
            'description': _('bibtex-address-desc', u"Usually the address (town) of the publisher or other type of institution. For major publishing houses, van Leunen recommends omitting the information entirely. For small publishers, on the other hand, you can help the reader by giving the complete address."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Address, self).__init__(*args, **d)


class Edition(schema.TextLine):
    __doc__ = ifield.IEdition.__doc__

    implements(ifield.IEdition)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-edition-title', u"Edition"),
            'description': _('bibtex-edition-desc', u"The edition of a book--for example, ``Second''. This should be an ordinal, and should have the first letter capitalized, as shown here; the standard styles convert to lower case when necessary."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Edition, self).__init__(*args, **d)


class Month(schema.TextLine):
    __doc__ = ifield.IMonth.__doc__

    implements(ifield.IMonth)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-month-title', u"Month"),
            'description': _('bibtex-month-desc', u"The month in which the work was published or, for an unpublished work, in which it was written. You should use the standard three-letter abbreviation, as described in Appendix B.1.3 of the LaTeX book."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Month, self).__init__(*args, **d)


class Note(schema.TextLine):
    __doc__ = ifield.INote.__doc__

    implements(ifield.INote)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-note-title', u"Note"),
            'description': _('bibtex-note-desc', u"Any additional information that can help the reader. The first word should be capitalized."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Note, self).__init__(*args, **d)


class Journal(schema.TextLine):
    __doc__ = ifield.IJournal.__doc__

    implements(ifield.IJournal)

    def __init__(self, *args, **kw):
        d = {
            'title': _("bibtex-journal-title",
                       u"Journal"),
            'description': _('bibtex-journal-desc',
                             u"A journal name. Abbreviations are provided for many journals; see the Local Guide."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Journal, self).__init__(*args, **d)


class Pages(schema.TextLine):
    __doc__ = ifield.IPages.__doc__

    implements(ifield.IPages)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-pages-title',
                       u"Pages"),
            'description': _('bibtex-pages-desc',
                             u"One or more page numbers or range of numbers, such as 42-111 or 7,41,73-97 or 43+ (the `+' in this last example indicates pages following that don't form a simple range). To make it easier to maintain Scribe-compatible databases, the standard styles convert a single dash (as in 7-33) to the double dash used in TeX to denote number ranges (as in 7-33)."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Pages, self).__init__(*args, **d)


class Booktitle(schema.Tuple):
    __doc__ = ifield.IBooktitle.__doc__

    implements(ifield.IBooktitle)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-booktitle-title',
                       u"Book Title"),
            'description': _('bibtex-booktitle-desc',
                             u"Title of a book, part of which is being cited."),
            'value_type': TitleTupleItem(required = True),
            }
        for key, value in kw.items():
            d[key] = value
        super(Booktitle, self).__init__(*args, **d)


class Type(schema.TextLine):
    __doc__ = ifield.IType.__doc__

    implements(ifield.IType)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-type-title',
                       u"Type"),
            'description': _('bibtex-type-desc',
                             u"The type of a technical report--for example, ``Research Note''."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Type, self).__init__(*args, **d)


class Chapter(schema.TextLine):
    __doc__ = ifield.IChapter.__doc__

    implements(ifield.IChapter)

    def __init__(self, *args, **kw):
        d = {
            'title': _('bibtex-chapter-title',
                       u"Chapter"),
            'description': _('bibtex-chapter-desc',
                             u"A chapter (or section or whatever) number."),
            }
        for key, value in kw.items():
            d[key] = value
        super(Chapter, self).__init__(*args, **d)
