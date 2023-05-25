import sys
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GObject


class ExampleDialog(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="My Dialog", transient_for=parent)

        self.add_buttons(
            "_OK",
            Gtk.ResponseType.OK,
            "_Cancel",
            Gtk.ResponseType.CANCEL,
        )

        box = self.get_content_area()
        print(type(box))

        box.append(Gtk.Button(label="HOLA"))

        self.entrada_texto = Gtk.Entry()
        box.append(self.entrada_texto)
