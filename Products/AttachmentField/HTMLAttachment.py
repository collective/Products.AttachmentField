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


import AttachmentHandler

import os
import os.path
import string
import re
import sys


if sys.platform == "win32":
    program = "type"
else:
    program = "cat"


class HTMLAttachment(AttachmentHandler.AbstractHandler):
    """
    MSWord file abstraction
    """
    icon_file = "html.gif"
    small_icon_file = "html_small.gif"
    content_types = ('text/html', )
    converter_type = "HTML"

    is_external_conv = True
    is_working = True
    index_path = program
    index_arguments = r"%s"
    index_encoding = None

    preview_path = program
    preview_arguments = r" %s"
    preview_encoding = None
    preview_format = "html"


AttachmentHandler.registerHandler(HTMLAttachment)
