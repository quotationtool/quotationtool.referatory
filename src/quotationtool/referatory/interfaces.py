# -*- coding: utf-8 -*-

import zope.interface
from zope.schema import Int, TextLine, Choice, List, Object, Tuple
from zope.container.interfaces import IContained, IContainer 
from zope.container.constraints import contains, containers

from i18n import _


class IUniformTitleContainer(zope.interface.Interface):
    """The uniform title objects go into a destinct container. This
    interface is the schema part of this container. """

    _count = Int(
        title = u"Count",
        )


class IUniformTitleContainerContainer(IContainer):
    """The container part of the container for uniform titles. We have
    split this into to interfaces.

    Let's test if the constraints are handle correctly: Implement a
    conainer and test some dummy objects.

        >>> from quotationtool.referatory import interfaces
        >>> import zope.interface
        >>> class UniformTitleContainer:
        ...     zope.interface.implements(
        ...         interfaces.IUniformTitleContainer,
        ...         interfaces.IUniformTitleContainerContainer)

        >>> uc = UniformTitleContainer()
        >>> bad = object()
        >>> from zope.container.constraints import checkObject
        >>> checkObject(uc, 'bad', bad)
        Traceback (most recent call last):
        ...
        InvalidItemType: (<quotationtool.referatory.interfaces.UniformTitleContainer instance at ...>, <object object at ...>, [<InterfaceClass quotationtool.referatory.interfaces.IUniformTitle>])
        
        >>> class UniformTitle:
        ...     zope.interface.implements(
        ...         interfaces.IUniformTitle)

        >>> title = UniformTitle()
        >>> checkObject(uc, 'title', title)
        >>> 
    
    """

    contains('.IUniformTitle')

    
class IUniformTitle(IContained):
    """ A uniform title is vital part of the data model. We want
    search results that include reprints and translations, too. That's
    where uniform titles come in. We want to know about the
    original. This information is stored in a uniform title object.

    Usage:

        >>> from quotationtool.referatory.interfaces import IUniformTitle
        >>> import zope.interface

        >>> IUniformTitle.names()
        ['language', 'uniform_title', 'year', 'ante', 'post', 'uniform_author', '__parent__']

        >>> import zope.schema
        >>> zope.schema.getFields(IUniformTitle).keys()
        ['language', 'uniform_title', 'year', 'ante', '__name__', 'post', 'uniform_author', '__parent__']

        >>> IUniformTitle['language'].validate('de')
        >>> IUniformTitle['language'].validate('bad')
        Traceback (most recent call last):
        ...
        ConstraintNotSatisfied: bad

        >>> IUniformTitle['uniform_author'].validate(tuple())
        >>> IUniformTitle['uniform_author'].validate((u"August",))
        >>> IUniformTitle['uniform_title'].validate(tuple())
        Traceback (most recent call last):
        ...
        TooShort: ((), 1)

        >>> IUniformTitle['uniform_title'].validate((u"Confessiones",))
        >>> IUniformTitle['year'].validate(u"400")
        Traceback (most recent call last):
        ...
        WrongType:...

        >>> IUniformTitle['year'].validate(400)

    Now let's write an simple implementation and test invariants etc. 

        >>> from zope.schema.fieldproperty import FieldProperty
        >>> class UniformTitle(object):
        ...     zope.interface.implements(IUniformTitle)
        ...     language = FieldProperty(IUniformTitle['language'])
        ...     uniform_author = FieldProperty(IUniformTitle['uniform_author'])
        ...     uniform_title = FieldProperty(IUniformTitle['uniform_title'])
        ...     year = FieldProperty(IUniformTitle['year'])
        ...     post = FieldProperty(IUniformTitle['post'])
        ...     ante = FieldProperty(IUniformTitle['ante'])

        >>> title = UniformTitle()
        >>> title.language = 'de'
        >>> title.language = 'bad'
        Traceback (most recent call last):
        ...
        ConstraintNotSatisfied: bad


    uniform_author may ether hold a tuple of unicode strings or be None.

        >>> title.uniform_author = u"Malone"
        Traceback (most recent call last):
        ...
        WrongType:...
        >>> title.uniform_author = (u"Bonny", u"Clyde")
        >>> title.uniform_author = None
        >>>

    uniform_title must be a tuple of at least one unicode strings.

        >>> title.uniform_title = None
        Traceback (most recent call last):
        ...
        RequiredMissing...

        >>> title.uniform_title = ()
        Traceback (most recent call last):
        ...
        TooShort: ((), 1)
        >>> title.uniform_title = (u"Confessiones",)

    The combination of year, post and ante attributes must match
    invariant conditions:

        >>> IUniformTitle.validateInvariants(title)
        Traceback (most recent call last):
        ...
        Invalid: yearpostanteerror-repr

        >>> title.ante = 410
        >>> IUniformTitle.validateInvariants(title)
        Traceback (most recent call last):
        ...
        Invalid: yearpostanteerror-repr

        >>> title.post = 480
        >>> IUniformTitle.validateInvariants(title)
        Traceback (most recent call last):
        ...
        Invalid: postexceedsanteerror-repr

        >>> title.post = 380
        >>> IUniformTitle.validateInvariants(title)

    But if all three of these attributes are given, invariant is not
    matched: ETHER an exact year OR a range of years (by a combination
    of termini post et ante quem) has to provided.
    
        >>> title.year = 400
        >>> IUniformTitle.validateInvariants(title)
        Traceback (most recent call last):
        ...
        Invalid: yearpostanteerror-repr


    Now let's check the container restriction.

        >>> from quotationtool.referatory.interfaces import IUniformTitleContainerContainer
        >>> class UniformTitleContainer(object):
        ...     zope.interface.implements(IUniformTitleContainerContainer)

        >>> container = UniformTitleContainer()
        >>> from zope.container.constraints import checkObject
        >>> checkObject(container, 'title', title)
        >>> 
        >>> bad = object()
        >>> checkObject(bad, 'title', title)
        Traceback (most recent call last):
        ...
        InvalidContainerType: (<object object at ...>, [<InterfaceClass quotationtool.referatory.interfaces.IUniformTitleContainerContainer>])



    """

    containers('.IUniformTitleContainerContainer')

    language = Choice(
        title = _('iuniformtitle-language-title',
                  u"Original Language"),
        description = _('iuniformtitle-language-desc',
                        u"The language in which this title was originally published/written."),
        required = True,
        vocabulary = 'z3c.i18n.iso.languages',
        default = 'de',
        )

    uniform_author = Tuple(
        title = _('iuniformtitle-uniformauthor-title',
                  u"Author"),
        description = _('iuniformtitle-uniformauthor-desc',
                        u"Name(s) of the Author(s) in the original's language. Enter <i>last name, first name</i> for sorting reasons. For names of acient writers a uniform name is required if we want to keep track of all quotations in the database. You may enter the name in more than one language, e.g. the greek, latin name of Aristotle."),
        value_type = TextLine(title = _('iuniformtitle-uniformauthor-item-title',
                                        u"Author Name"),
                              description = _('iuniformtitle-uniformauthor-item-desc',
                                              'Format: <i>Lastname, Firstname</i>'),
                              required = True,
                              ),
        required = False,
        )
        
    uniform_title = Tuple(
        title = _('iuniformtitle-uniformtitle-title',
                  u"Uniform Title"),
        description = _('iuniformtitle-uniformtitle-desc',
                        u"The uniform title is required to keep track of the quotations taken form other editions or from tranlations of this writing. You may enter the title in more than one language, e.g. <i>tèchne rhetoriké</i> and <i>De arte rhetorica</i> for an edition of Aristotle's writing on rhetorics. Only the first title given will be shown most of the time."),
        required = True,
        min_length = 1,
        value_type = TextLine(title = _('iuniformtitle-uniformtitle-item-title',
                                        u"Title"),
                              required = True,
                              ),
        default = (u"", ), #TODO: remove when widget is improved
        )
        
    year = Int(
        title = _('iuniformtitle-year-title',
                  u"Year First Published"),
        description = _('iuniformtitle-year-desc',
                        u"The date of origin as gregorian year. Alternatively give a terminus post quem and a terminus ante quem."),
        required = False,
        default = None,
        )

    post = Int(
        title = _('iuniformtitle-post-title',
                  u"Terminus Post Quem"),
        description = _('iuniformtitle-post-desc',
                        u"The lower bounding year. The writing was published (written) after this year."),
        required = False,
        default = None,
        )

    ante = Int(
        title = _('iuniformtitle-ante-title',
                  u"Terminus Ante Quem"),
        description = _('iuniformtitle-ante-desc',
                        u"The upper bounding year. The writing was first published (written) before this year."),
        required = False,
        default = None,
        )

    @zope.interface.invariant
    def checkYearPostAnte(uniformtitle):
        if not uniformtitle.year:
            if not (uniformtitle.post and uniformtitle.ante):
                raise zope.interface.Invalid(
                    _('yearpostanteerror-repr',
                      u"ETHER 'year first published' OR both, 'terminus post quem' and 'terminus ante quem' have to be entered."))
            else:
                if uniformtitle.post > uniformtitle.ante:
                    raise zope.interface.Invalid(
                        _('postexceedsanteerror-repr',
                          u"The value of 'terminus post quem' must not exceed the value for 'terminus ante quem'."))
                else:
                    pass
        else:
            if uniformtitle.post or uniformtitle.ante:
                raise zope.interface.Invalid(
                    _('yearpostanteerror-repr',
                      u"ETHER 'year first published' OR both, 'terminus post quem' and 'terminus ante quem' have to be entered."))
            else:
                pass
            

class IUniformTitleIndexCatalog(zope.interface.Interface):
    """A catalog of indices for searching uniform title objects."""

    author = TextLine(
        title = _('iuniformtitleindexcatalog-author-title',
                  u"Author"),
        description = _('iuniformtitleindexcatalog-author-desc',
                        u"Search by Author."),
        required = False,
        default = u'',
        )

    title = TextLine(
        title = _('iuniformtitleindexcatalog-title-title',
                  u"Title"),
        description = _('iuniformtitleindexcatalog-title-desc',
                        u"Search by Title."),
        required = False,
        default = u'',
        )


class IReferatory(zope.interface.Interface):
    """The referatory is a container/folder. It contains all our
    references. This interface defines the schema part of the
    referatory."""

    _count = Int(
        title = u"Count",
        )


class IReferatoryContainer(IContainer):
    """This interface defines the container part of the referatory.

    Testing:

        >>> from quotationtool.referatory.interfaces import \
                IReferatory, IReferatoryContainer
        >>> import zope.interface
        >>> class Referatory(object):
        ...     zope.interface.implements(IReferatory,
        ...         IReferatoryContainer)

        >>> referatory = Referatory()
        >>> from quotationtool.referatory.interfaces import IReference
        >>> class Reference(object):
        ...     zope.interface.implements(IReference)

        >>> reference = Reference()
        >>> from zope.container.constraints import checkObject
        >>> checkObject(referatory, 'reference', reference)
        >>> bad = object()
        >>> checkObject(referatory, 'bad', bad)
        Traceback (most recent call last):
        ...
        InvalidItemType: (<quotationtool.referatory.interfaces.Referatory object at ...>, <object object at ...>, [<InterfaceClass quotationtool.referatory.interfaces.IReference>])

    """
    
    contains('.IReference')


class IReference(IContained):
    """A reference object. This is a base interface. It just defines a
    relation to a uniform title object which is needed to keep track of
    other editions, reprints, translations etc.

    Other fields must be defined by more specific reference types.
    
    A reference object is contained in the referatory.


        >>> from quotationtool.referatory.interfaces import IReference
        >>> import zope.interface
        >>> from zope.schema.fieldproperty import FieldProperty
        >>> class Reference(object):
        ...     zope.interface.implements(IReference)
        ...     uniform_title = FieldProperty(IReference['uniform_title'])

        >>> reference = Reference()

    References live in a referatory.

        >>> from quotationtool.referatory.interfaces import \
                IReferatory, IReferatoryContainer
        >>> import zope.interface
        >>> class Referatory(object):
        ...     zope.interface.implements(IReferatory,
        ...         IReferatoryContainer)

        >>> referatory = Referatory()
        >>> from zope.container.constraints import checkObject
        >>> checkObject(referatory, 'reference', reference)

    But it is not to be contained by none-IReferatoryContainer containers.

        >>> bad = object()
        >>> checkObject(bad, 'reference', reference)
        Traceback (most recent call last):
        ...
        InvalidContainerType: (<object object at ...>, (<InterfaceClass quotationtool.referatory.interfaces.IReferatoryContainer>,))

        >>> reference.__parent__ = referatory

        >>> from quotationtool.referatory.interfaces import IUniformTitle
        >>> import zope.interface
        >>> from zope.schema.fieldproperty import FieldProperty
        >>> class UniformTitle(object):
        ...     zope.interface.implements(IUniformTitle)
        ...     language = FieldProperty(IUniformTitle['language'])
        ...     uniform_author = FieldProperty(IUniformTitle['uniform_author'])
        ...     uniform_title = FieldProperty(IUniformTitle['uniform_title'])
        ...     year = FieldProperty(IUniformTitle['year'])
        ...     post = FieldProperty(IUniformTitle['post'])
        ...     ante = FieldProperty(IUniformTitle['ante'])
        ...     __name__ = __parent__ = None

        >>> uniformtitle = UniformTitle()
        >>> reference.uniform_title = uniformtitle
        Traceback (most recent call last):
        ...
        WrongContainedType:...RequiredMissing...

        
    Since the uniformtitle does not pass its schema check, it may not be set.

        >>> uniformtitle.language = 'de'
        >>> uniformtitle.title = (u"Confessiones",)
        >>> uniformtitle.year = 400
        >>> reference.uniform_title = uniformtitle
        Traceback (most recent call last):
        ...
        WrongContainedType:...RequiredMissing...
        

    The __parent__ attribute is checked, too!

        >>> from quotationtool.referatory.interfaces import IUniformTitleContainer
        >>> class UniformTitleContainer(object):
        ...     zope.interface.implements(IUniformTitleContainerContainer)

        >>> container = UniformTitleContainer()
        >>> uniformtitle.__parent__ = UniformTitleContainer()
        >>> reference.uniform_title = uniformtitle
        >>> 

"""

    containers(IReferatoryContainer)

    uniform_title = Object(title = _('ireference-uniformtitle-title',
                                     u"Uniform Title"),
                           description = _('ireference-uniformtitle-dec',
                                           u"Information on the origin (date of origin, language, title)."),
                           required = True,
                           schema = IUniformTitle,
                           default = None,
                           )


class IReferenceIndexCatalog(zope.interface.Interface):
    """A catalog of indexes that we want to search for in the
    referatory."""

    author = TextLine(
        title = _('ireferenceindexcatalog-author-title',
                  u"Author / Uniform Author"),
        description = _('ireferenceindexcatalog-author-desc',
                        u"Search by author. Even matches the author-field of the uniform title."),
        required = False,
        default = u'',
        )

    title = TextLine(
        title = _('ireferenceindexcatalog-title-title',
                  u"Title / Uniform Title"),
        description = _('ireferenceindexercatalog-title-desc',
                        u"Search by title or uniform title."
                        ),
        required = False,
        default = u'',
        )

    post = Int(
        title = _('ireferenceindexcatalog-post-title',
                  u"Published/Written After"),
        description = _('ireferenceindexcatalog-post-desc',
                  u"Matches, if published after."),
        required = False,
        )

    ante = Int(
        title = _('ireferenceindexcatalog-ante-title',
                  u"Published/Writter Before"),
        description = _('ireferenceindexcatalog-ante-desc',
                  u"Matsches, if published before."),
        required = False,
        )

    year = Int(
        title = _('ireferenceindexcatalog-year-title',
                  u"Year first published"),
        description = _('ireferenceindexcatalog-year-desc',
                  u"Matches the exact year of origin."),
        required = False,
        )

    language = TextLine(
        title = _('ireferenceindexcatalog-language-title',
                  u"Language / Original Language"),
        description = _('ireferenceindexcatalog-language-desc',
                  u"Search for items by language."),
        required = False,
        default = u'',
        )

    edition_year = TextLine(
        title = _('irefenceindexer-editionyear-title',
                  u"Year of edition"),
        description = _('ireferenceindexcatalog-edtionyear-desc',
                  u"Matches the year of the edition."),
        required = True,
        )

    editor = TextLine(
        title = _('ireferenceindexcatalog-editor-title',
                  u"Editor"),
        description = _('ireferenceindexcatalog-editor-desc',
                  u"Search by editor."),
        required = False,
        default = u'',
        )

    publisher = TextLine(
        title = _('ireferenceindexcatalog-publisher-title',
                  u"Publisher"),
        description = _('ireferenceindexcatalog-publisher-desc',
                  u"Search by publisher."),
        required = False,
        default = u'',
        )

    address = TextLine(
        title = _('ireferenceindexcatalog-address-title',
                  u"Address"),
        description = _('ireferenceindexcatalog-address-desc',
                  u"Search by address of edition (place of publication)."),
        required = False,
        default = u'',
        )
