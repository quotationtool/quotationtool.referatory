from zope.interface import implements
from persistent import Persistent
from zope.schema.fieldproperty import FieldProperty
from zope.container.contained import Contained

from interfaces import IUniformTitle


class UniformTitle(Persistent, Contained):
    """This is an implementation of IUniformTitle."""

    implements(IUniformTitle)

    __name__ = __parent__ = None

    language = FieldProperty(IUniformTitle['language'])
    uniform_author = FieldProperty(IUniformTitle['uniform_author'])
    uniform_title = FieldProperty(IUniformTitle['uniform_title'])
    year = FieldProperty(IUniformTitle['year'])
    post = FieldProperty(IUniformTitle['post'])
    ante = FieldProperty(IUniformTitle['ante'])
