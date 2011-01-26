import zope.interface
from zope.schema.interfaces import IList, ITuple, ITextLine, IChoice


class IBibtexField(zope.interface.Interface):
    """A marker interface for bibtex fields."""

class ILanguage(IChoice, IBibtexField):
    u"""A field holding a python uncode stirng."""

class IName(ITextLine):
    u"""A name field holding a python unicode string."""

class IAuthor(ITuple, IBibtexField):
    u"""A field holding a python tuple of IAuthorTupleItem objects."""

class IEditor(ITuple, IBibtexField):
    u"""A field holding a python tuple of IEditorTupleItem objects."""

class ITitle(ITuple, IBibtexField):
    u"""A field holding a python tuple of ITitleTupleItem objects."""

class ITitleTupleItem(ITextLine):
    u"""A field holding a python unicode string."""

class IPublisher(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class IYear(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class IVolume(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class INumber(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class ISeries(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class IAddress(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class IEdition(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class IMonth(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class INote(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class IJournal(ITextLine, IBibtexField):
    u"""A field holding a unicode string."""

class IPages(ITextLine, IBibtexField):
    u"""A field holding a unicode string."""
    
class IBooktitle(ITuple, IBibtexField):
    u"""A tuple of ITitleItem objects."""

class IType(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""

class IChapter(ITextLine, IBibtexField):
    u"""A field holding a python unicode string."""
