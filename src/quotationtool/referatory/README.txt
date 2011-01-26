This module contains all things required for a bibliographic database.

Let's start by investigating the interface for UniformTitle objects:

    >>> from quotationtool.referatory import interfaces
    >>> import zope.interface
    >>> interfaces.IUniformTitle.names()
    ['language', 'uniform_title', 'year', 'ante', 'post', 'uniform_author', '__parent__']

    >>> import zope.schema
    >>> zope.schema.getFields(interfaces.IUniformTitle).keys()
    ['language', 'uniform_title', 'year', 'ante', '__name__', 'post', 'uniform_author', '__parent__']

Now let's create some objects:

    >>> from quotationtool.referatory.uniformtitle import UniformTitle
    >>> from quotationtool.referatory.uniformtitlecontainer import UniformTitleContainer

    >>> confessiones = UniformTitle()
    >>> confessiones.language = u'de'
    >>> confessiones.author = (u"Augustinus",)
    >>> confessiones.title = (u"Confessiones",)
    >>> confessiones.post = 380
    >>> confessiones.ante = 410

UniformTitle objects live in a special container, in a
UniformTitleContainer:

    >>> uniformtitles = UniformTitleContainer()
    >>> uniformtitles['confessiones'] = confessiones
    >>> confessiones.__name__
    u'confessiones'

    >>> confessiones.__parent__
    <quotationtool.referatory.uniformtitlecontainer.UniformTitleContainer object at ...>

The bibliographic information is stored on reference objects. There is
a base class which should be derived from by every specific reference
object class (e.g. a class for books, a class for articles etc.). 

Now let's investigate the schema of reference base class:

    >>> interfaces.IReference.names()
    ['__parent__', 'uniform_title']

    >>> zope.schema.getFields(interfaces.IReference).keys()
    ['__name__', '__parent__', 'uniform_title']


The uniform_title attribute of a reference object must be a
UniformTitle object:

    >>> from quotationtool.referatory.reference import Reference
    >>> bekenntnisse = Reference()
    >>> bekenntnisse.uniform_title = confessiones
    >>> bekenntnisse.uniform_title = object()
    Traceback (most recent call last):
    ...
    SchemaNotProvided


Reference objects are stored in a special container, a referatory:

    >>> from quotationtool.referatory.referatory import Referatory
    >>> referatory = Referatory()
    >>> referatory['confessiones-de'] = bekenntnisse
    >>> bekenntnisse.__name__
    u'confessiones-de'

    >>> bekenntnisse.__parent__
    <quotationtool.referatory.referatory.Referatory object at ...>
