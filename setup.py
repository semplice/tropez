#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# tropez - the Semplice introducer!
# Copyright (C) 2013 Eugenio "g7" Paolantonio
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# This is the distutils-based installation program.
#

from distutils.core import setup

setup(name='tropez',
	version='0.0.1',
	description='The Semplice introducer!',
	author='Eugenio Paolantonio',
	author_email='me@medesimo.eu',
	url='http://github.com/semplice/tropez',
	# package_dir={'bin':''},
	scripts=['tropez.py'],
	packages=[
		"tropez",
      ],
	data_files=[("/usr/share/tropez", ["tropez.glade", "tropez.css"]), ("/etc/skel/.config/autostart", ["tropez.desktop"])],
	requires=['gi.repository.Gtk', 'gi.repository.GObject', 'gi.repository.Gdk, ''t9n', 'subprocess', 'os'],
)
