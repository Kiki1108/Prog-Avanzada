import sys
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GObject


class Exito(Gtk.MessageDialog):
    def __init__(self, parent):
        super().__init__(transient_for=parent)

        self.set_default_size(200, 40)

        self.add_buttons(
            "_OK",
            Gtk.ResponseType.OK,
        )

        box = self.get_content_area()
        box.append(Gtk.Label(label="Se ha guardado con éxito"))
