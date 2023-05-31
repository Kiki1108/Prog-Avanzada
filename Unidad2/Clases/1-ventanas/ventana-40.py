import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib

QUIT = False

def quit_(window):
    global QUIT
    QUIT = True

class Ventana(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ventana simple")
        self.connect("close-request", quit_)
        self.show()

if __name__ == "__main__":
    Ventana()
    loop = GLib.MainContext().default()
    while not QUIT:
        loop.iteration(True)
