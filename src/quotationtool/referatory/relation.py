import zope.component
from zope.app.intid.interfaces import IIntIds
from zope.app.intid.interfaces import IIntIdAddedEvent, IIntIdRemovedEvent
import zc.relation
import BTrees

import interfaces
from quotationtool.site.interfaces import INewQuotationtoolSiteEvent
import quotationtool.relation


@zope.component.adapter(INewQuotationtoolSiteEvent)
def addRelationIndex(event):
    cat = zope.component.getUtility(
        zc.relation.interfaces.ICatalog,
        context = event.object)
    cat.addValueIndex(interfaces.IReference['uniform_title'],
                      dump = quotationtool.relation.dump,
                      load = quotationtool.relation.load,
                      name = 'ireference-uniform_title')

                      
#BBB: We have a single relation catalog
def dump(obj, catalog, cache):
    intids_ut = cache.get('intids_ut')
    if not intids_ut:
        intids_ut = zope.component.getUtility(IIntIds)
        cache['intids_ut'] = intids_ut
    return intids_ut.getId(obj)

def load(token, catalog, cache):
    intids_ut = cache.get('intids_ut')
    if not intids_ut:
        intids_ut = zope.component.getUtility(IIntIds)
        cache['intids_ut'] = intids_ut
    return intids_ut.getObject(token)


class ReferatoryCatalog(zc.relation.catalog.Catalog):
    """A catalog that indexes the reference-to-uniformtitle-relation.

    This catalog is expected to be registered by other components as a
    zc.relation.interfaces.ICatalog utility by the name 'referatory'."""

    def __init__(self):
        super(ReferatoryCatalog, self).__init__(dump, load,
                                                family = BTrees.family64
                                                )

        # index to search reference objects with a given uniformtitle
        self.addValueIndex(interfaces.IReference['uniform_title'],
                           dump, load)
        

@zope.component.adapter(IIntIdAddedEvent)
def indexSubscriber(event):
    cat = zope.component.queryUtility(
        zc.relation.interfaces.ICatalog,
        name = 'referatory', context = event.object)
    if cat is not None:
        cat.index(event.object)

@zope.component.adapter(IIntIdRemovedEvent)
def unindexSubscriber(event):
    cat = zope.component.queryUtility(
        zc.relation.interfaces.ICatalog,
        name = 'referatory', context = event.object)
    if cat is not None:
        cat.unindex(event.object)

    
@zope.component.adapter(IIntIdAddedEvent)
def testSubscriber(event):
    if interfaces.IReference.providedBy(event.object):
        raise Exception(event, event.object)



@zope.component.adapter(INewQuotationtoolSiteEvent)
def createReferatoryCatalog(event):
    # TODO: hardcoded names are not nice, but where can we put this?
    sm = event.object.getSiteManager()
    cat = sm['default']['referatory_relation_catalog'] = ReferatoryCatalog()
    sm.registerUtility(cat, zc.relation.interfaces.ICatalog,
                       name = 'referatory')
