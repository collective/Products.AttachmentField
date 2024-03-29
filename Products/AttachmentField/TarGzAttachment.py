# -*- coding: utf-8 -*-
## AttchmentField
## Copyright (C)2006 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
AttchmentField
"""
__version__ = "$Revision$"
# $Source: /cvsroot/ingeniweb/PloneSubscription/SubscriptionTool.py,v $
# $Id$
__docformat__ = 'restructuredtext'


from global_symbols import *

import os
import sys
import string
import CompressedAttachment
import AttachmentHandler

if sys.platform == "win32":
    program = None
else:
    program = "tar"


class TarGzAttachment(CompressedAttachment.CompressedAttachment):
    """
    Tar / compressed file abstraction
    """
    converter_type = "TarGz"
    content_types = (
        'application/x-tar',
        'application/x-gtar',
        'application/tgz',
        )

    is_external_conv = True
    is_working = True
    index_path = program
    index_arguments = r'-tzvf %s'
    index_encoding = ('iso-8859-15', 'utf8')

    preview_path = program
    preview_arguments = r'-tzvf %s'
    preview_encoding = ('iso-8859-15', 'utf8')
    preview_format = 'pre'



AttachmentHandler.registerHandler(TarGzAttachment)
