import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            title="Ventana simple")
        self.set_default_size(800, 600)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    v = Ventana()
    print(isinstance(v, Gtk.Window))
    Gtk.main()
