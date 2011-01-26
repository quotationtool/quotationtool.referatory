import zope.interface
import zope.component
import zc.catalog
from zope.catalog.text import TextIndex
from zope.catalog.interfaces import ICatalog
from zc.catalog.catalogindex import ValueIndex
import BTrees

from quotationtool.site.interfaces import INewQuotationtoolSiteEvent
import interfaces


class ReferenceIndexDescriptor(object):
    """A python descriptor helping to index the attributes inherited from
    IReferenceIndexCatalog."""

    def __init__(self, name):
        self.name = name

    def __get__(self, inst, class_ = None):
        return getattr(inst.reference_indexer, self.name, u'')

    def __set__(self, inst, val):
        pass


class ReferenceIndexerBase(object):
    """A base class for adapters for indexing iquotation objects in a
    IReferenceIndexCatalog."""

    zope.interface.implements(interfaces.IReferenceIndexCatalog)

    def __init__(self, context):
        raise NotImplemented

    # IReferenceIndexCatalog
    author = ReferenceIndexDescriptor('author')
    title = ReferenceIndexDescriptor('title')
    post = ReferenceIndexDescriptor('post')
    ante = ReferenceIndexDescriptor('ante')
    year = ReferenceIndexDescriptor('year')
    language = ReferenceIndexDescriptor('language')
    edition_year = ReferenceIndexDescriptor('edition_year')
    edition = ReferenceIndexDescriptor('edition')
    publisher = ReferenceIndexDescriptor('publisher')
    address = ReferenceIndexDescriptor('address')


def createReferenceIndices(cat, interface = interfaces.IReferenceIndexCatalog):
    """Add indexes defined in IReferenceIndexCatalog to the catatlog
    passed in via the first argument."""

    cat['author'] = TextIndex(
        interface = interface,
        field_name = 'author')
    
    cat['title'] = TextIndex(
        interface = interface,
        field_name = 'title')

    cat['post'] = ValueIndex(
        interface = interface,
        field_name = 'post')

    cat['ante'] = ValueIndex(
        interface = interface,
        field_name = 'ante')

    cat['year'] = ValueIndex(
        interface = interface,
        field_name = 'year')

    cat['language'] = ValueIndex(
        interface = interface,
        field_name = 'language')


def filter(extent, uid, obj):
    """An extent filter that only IReference objects pass."""
    assert zc.catalog.interfaces.IFilterExtent.providedBy(extent)
    return interfaces.IReference.providedBy(obj)

    
@zope.component.adapter(INewQuotationtoolSiteEvent)
def createReferatoryCatalog(event):
    sm = event.object.getSiteManager()

    extent = zc.catalog.extentcatalog.FilterExtent(filter)#, family = BTrees.family64)

    sm['default']['referatory_search_catalog'] = cat = zc.catalog.extentcatalog.Catalog(extent)

    createReferenceIndices(cat)

    sm.registerUtility(cat, ICatalog,
                       name = "referatory")


class UniformTitleIndexer(object):
    """An adapter that helps indexing uniform title objects."""

    zope.interface.implements(interfaces.IUniformTitleIndexCatalog)

    zope.component.adapts(interfaces.IUniformTitle)

    def __init__(self, context):
        self.context = context

    def getAuthor(self):
        if getattr(self.context, 'uniform_author', None) is None:
            return u""
        rc = u""
        for au in self.context.uniform_author:
            rc += au + u" "
        return rc
    author = property(getAuthor)

    def getTitle(self):
        rc = u""
        for tit in self.context.uniform_title:
            rc += tit + u" "
        return rc
    title = property(getTitle)


def createUniformTitleIndices(cat, interface = interfaces.IUniformTitleIndexCatalog):
    """Add indexes defined in IUniformTitleIndexCatalog to the catatlog
    passed in via the first argument."""

    cat['author'] = TextIndex(
        interface = interface,
        field_name = 'author')
    
    cat['title'] = TextIndex(
        interface = interface,
        field_name = 'title')


def uniformTitleFilter(extent, uid, obj):
    """An extent filter that only lets IUniformTitle objects pass."""
    assert zc.catalog.interfaces.IFilterExtent.providedBy(extent)
    return interfaces.IUniformTitle.providedBy(obj)


@zope.component.adapter(INewQuotationtoolSiteEvent)
def createUniformTitleCatalog(event):
    """Create a catalog for unioform titles when a new quotationtool
    site is created."""
    sm = event.object.getSiteManager()

    extent = zc.catalog.extentcatalog.FilterExtent(uniformTitleFilter)#, family = BTrees.family64)

    sm['default']['uniformtitle_search_catalog'] = cat = zc.catalog.extentcatalog.Catalog(extent)

    createUniformTitleIndices(cat)

    sm.registerUtility(cat, ICatalog,
                       name = "uniformtitles")
