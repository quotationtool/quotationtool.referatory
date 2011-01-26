from zope.interface import implements
from zope.component import adapter
from zope.container.btree import BTreeContainer
from zope.schema.fieldproperty import FieldProperty
from zope.dublincore.interfaces import IWriteZopeDublinCore

from interfaces import IUniformTitleContainer, IUniformTitleContainerContainer


class UniformTitleContainer(BTreeContainer):
    """Implementation of an container for uniform titles."""

    implements(IUniformTitleContainer,
               IUniformTitleContainerContainer)

    _count = FieldProperty(IUniformTitleContainer['_count'])
