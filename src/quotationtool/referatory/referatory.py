from zope.interface import implements
from zope.component import adapter
from zope.container.btree import BTreeContainer
from zope.schema.fieldproperty import FieldProperty
from zope.dublincore.interfaces import IWriteZopeDublinCore

from interfaces import IReferatory, IReferatoryContainer


class Referatory(BTreeContainer):
    """Implementation of an referatory"""

    implements(IReferatory,
               IReferatoryContainer)

    _count = FieldProperty(IReferatory['_count'])
