#!/usr/bin/env python
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
# This file contains the content.
#

import os
import t9n.library

_ = t9n.library.translation_init("tropez")

# Check if LIVE...
if os.path.exists("/etc/semplice-live-mode"):
	LIVE = True
else:
	LIVE = False

# Obtain version
VERSION = ""
if os.path.exists("/etc/semplice_version"):
	with open("/etc/semplice_version") as f:
		VERSION = f.readline().replace("\n","")

content = {
	"welcome": {
		"title": _("Welcome to Semplice %s") % VERSION,
		"text": _("""You have successfully installed Semplice on your Personal Computer. Congratulations!

To help you get started, we have crafted a simple and short tutorial.
Just press the <b>Start tutorial</b> button to start.

You can run the tutorial every time you want by opening <b>Applications → Accessories → Tutorial</b>.


We hope you'll like Semplice as we do!
""")
	},

	"welcome_live": {
		"title": _("Welcome to Semplice Live %s") % VERSION,
		"text": _("""You have successfully booted Semplice.

To help you get started, we have crafted a simple and short tutorial.
Just press the <b>Start tutorial</b> button to start.

You can run the tutorial every time you want by opening <b>Applications → Accessories → Tutorial</b>.


We hope you'll like Semplice as we do!
""")
	},

	"desktop": {
		"title": _("Hey!"),
		"text": _("""Hello and welcome to the Semplice tutorial!

Have a look around. What do you see? A gorgeous wallpaper and an eye-catching panel.
That's everything you need to have.

By default, desktop icons are disabled.
If you really want to enable it, just press the <b>Enable desktop icons</b> button."""),
		"customTitle": _("Enable desktop icons"),
		"customExecutable": _("semplice-desktop-settings"),
	},

	"menu": {
		"title": _("System menu"),
		"text": _("""In Semplice you won't find boring buttons to open the main menu. Just right-click anywhere in your desktop and you are right to go!

And when you are using a maximized application, just right-click in the task bar.
Easy, uh?

Of course our menu is easily customizable. Just click the <b>Configure the menu</b> button to launch the configuration tool."""),
		"customTitle" : _("Configure the menu"),
		"customExecutable" : _("alan-settings")
	},

	"panel": {
		"title": _("Panel"),
		"text": _("""In the bottom of your screen there is a panel which houses all your open applications and the system tray.

By clicking on the clock a nifty calendar will show up. Clicking on the clock again will hide it.

At the left of the panel you'll find various launchers for your applications. You can obviously configure it as you like!
Click on the <b>Manage launchers</b> button to do so.

Keep in mind that you can modify the launchers whenever you want, just open <b>Applications → Preferences → Panel</b>."""),
		"customTitle": _("Manage launchers"),
		"customExecutable": _("semplice-tint2-settings")
	},
	
	"install": {
		"title": _("Excited?"),
		"text": _("""Semplice is ready to be installed! Click the <b>Install Semplice now</b> button to launch our much acclaimed installation wizard.

It will take only 15 minutes!

Are you ready to join the revolution?

If you are still unsure, keep in mind that you can launch the installation program at any time by launching <b>Install Semplice → Start Installer</b>."""),
		"customTitle": _("Install Semplice now"),
		"customExecutable": _("sudo linstaller -f=glade start")
	},
	
	"end": {
		"title": _("Rock on!"),
		"text": _("""We hope you'll like Semplice as we do every day.

Semplice is our try to create a desktop operating system designed with performance and simplicity in mind.

And if we in your opinion succeeded, please drop a line about us wherever you want.
We always love when people are happy when using our products.

We do not only release an awesome distribution, we release <b>happiness</b>.


You can now press the <b>Close</b> button to close this tutorial."""),
		"customTitle": _("Spread the love!"),
		"customExecutable": _("xdg-open http://semplice-linux.org")
	}
}

if LIVE:
	welcome_content = "welcome_live"
else:
	welcome_content = "welcome"

order = (welcome_content, "desktop", "menu", "panel", "install", "end")
