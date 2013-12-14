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
# This is the main executable.
#

from gi.repository import Gtk, GObject, Gdk

import t9n.library

import os

import sys

import subprocess

import tropez.content

_ = t9n.library.translation_init("tropez")

GLADEFILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tropez.glade")
if not os.path.exists(GLADEFILE):
	# fallback to the package one
	GLADEFILE = "/usr/share/tropez/tropez.glade"

CSSFILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tropez.css")
if not os.path.exists(CSSFILE):
	# fallback to the package one
	CSSFILE = "/usr/share/tropez/tropez.css"

class GUI:
	def quit(self, caller):
		Gtk.main_quit()
	
	def change_content(self, content):
		""" Changes the content. """
		
		cont = tropez.content.content[content] # I love that word!
		
		self.page_title.set_text(cont["title"])
		self.page_text.set_markup(cont["text"])
		
		# Show/Hide custom button
		if "customTitle" in cont:
			self.custom_button.show()
			# Also set text
			self.custom_button.set_label(cont["customTitle"])
		else:
			self.custom_button.hide()
		
		# Set title
		self.main.set_title(_("%s - Tutorial") % cont["title"])
	
	def begin_tutorial(self, button):
		""" Starts the tutorial. """
		
		GObject.idle_add(button.hide)
		
		# Show next and back
		GObject.idle_add(self.next_button.show)
		GObject.idle_add(self.back_button.show)
		
		self.current = 0
		GObject.idle_add(self.next, None)

		# Ensure back is sensitive
		GObject.idle_add(self.back_button.set_sensitive, False)
	
	def run_custom_application(self, button):
		""" Fired when the custom button has been clicked. """
		
		executable = tropez.content.content[tropez.content.order[self.current]]["customExecutable"]
		
		subprocess.Popen(executable, shell=True)
	
	def next(self, button):
		""" Goes next. """
		
		self.current += 1
		GObject.idle_add(self.change_content, tropez.content.order[self.current])
		
		# Disable button if we are at the end...
		if button:
			if len(tropez.content.order) == self.current + 1:
				GObject.idle_add(button.set_sensitive, False)
			# Ensure back is sensitive
			GObject.idle_add(self.back_button.set_sensitive, True)

	def back(self, button):
		""" Goes back. """
		
		self.current -= 1
		GObject.idle_add(self.change_content, tropez.content.order[self.current])

		# Disable button if we are at the start...
		if self.current == 1:
			GObject.idle_add(button.set_sensitive, False)
		# Ensure next is sensitive
		GObject.idle_add(self.next_button.set_sensitive, True)

	def __init__(self, with_greeter):
		""" Initialize the GUI. """
				
		self.objects = {}
		
		self.builder = Gtk.Builder()
		self.builder.add_from_file(GLADEFILE)
		
		self.main = self.builder.get_object("main")
		self.main.connect("destroy", self.quit)
		
		self.page_title = self.builder.get_object("page_title")
		self.page_text = self.builder.get_object("page_text")
		
		self.custom_button = self.builder.get_object("custom_button")
		self.custom_button.connect("clicked", self.run_custom_application)
		
		self.next_button = self.builder.get_object("next_button")
		self.next_button.connect("clicked", self.next)
		
		self.back_button = self.builder.get_object("back_button")
		self.back_button.connect("clicked", self.back)
		
		self.start_button = self.builder.get_object("start_button")
		self.start_button.connect("clicked", self.begin_tutorial)
		
		self.close_button = self.builder.get_object("close_button")
		self.close_button.connect("clicked", self.quit)

		self.main.show_all()

		# Should we greet the user?
		if with_greeter:
			# Show first
			self.change_content(tropez.content.order[0])
		else:
			# Begin tutorial directly
			self.begin_tutorial(self.start_button)

		# Hide Next and Back
		self.next_button.hide()
		self.back_button.hide()


if __name__ == "__main__":
	# Internal start?
	if len(sys.argv) > 1 and sys.argv[1] == "--with-greeter":
		with_greeter = True
		# Remove autostart file if any
		autostart_file = os.path.expanduser("~/.config/autostart/tropez.desktop")
		if os.path.exists(autostart_file): os.remove(autostart_file)
	else:
		with_greeter = False
	
	settings = Gtk.Settings.get_default()
	settings.set_property("gtk-application-prefer-dark-theme", True)
	
	if settings.get_property("gtk-theme-name") == "SempliceNight":
		# Add SempliceNight-specific theming
		cssProvider = Gtk.CssProvider()
		cssProvider.load_from_path(CSSFILE)
		screen = Gdk.Screen.get_default()
		styleContext = Gtk.StyleContext()
		styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

	g = GUI(with_greeter)
	Gtk.main()
