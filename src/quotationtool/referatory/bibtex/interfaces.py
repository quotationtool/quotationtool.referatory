# -*- coding: utf-8 -*-
"""Interfaces for the BibTeX referatory.

Policy: Only interface definitions common to all types go here,
interfaces to special <type> go into i<type>.py, while field
interfaces go into ifield.py.
"""

import zope.interface

import field


class IBibtexReference(zope.interface.Interface):
    """Common to all bibtex types."""

    language = field.Language(required = True)
