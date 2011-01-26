from zope.interface import implements
from persistent import Persistent
from zope.schema.fieldproperty import FieldProperty
from zope.container.contained import Contained

from interfaces import IReference


class Reference(Persistent, Contained):
    """This is a base class that provides common behaviour for diverse
    reference types."""

    implements(IReference)

    __name__ = __parent__ = None

    uniform_title = FieldProperty(IReference['uniform_title'])
