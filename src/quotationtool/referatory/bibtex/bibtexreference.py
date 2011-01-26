import zope.interface
from zope.schema.fieldproperty import FieldProperty

import interfaces
from quotationtool.referatory.reference import Reference


class BibtexReference(Reference):
    """A base class for BibTeX references."""

    zope.interface.implements(interfaces.IBibtexReference)

    language = FieldProperty(interfaces.IBibtexReference['language'])

