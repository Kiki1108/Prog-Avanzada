import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GLib

QUIT = False

def quit_(window):
    global QUIT
    QUIT = True

class Ventana(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box1 = Gtk.Box.new( Gtk.Orientation.VERTICAL,10) #(orientation VERTICAL|HORIZONTAL  , spacing in pixels)
        self.set_child(self.box1)

        self.about_button = Gtk.Button.new()
        self.about_button.set_label("About") # Or Change "label Propertie" self.about_button.props.label = "About"
        self.about_button.connect("clicked",self.on_about_button_clicked,"My Example App")
        self.box1.append(self.about_button)

        self.quit_button = Gtk.Button.new_with_label("Quit")
        self.quit_button.connect("clicked",self.on_quit_button_clicked)
        self.quit_button.props.vexpand = True  # Whether to expand vertically
        # https://amolenaar.github.io/pgi-docgen/index.html#Gtk-4.0/classes/Widget.html#Gtk.Widget.props.vexpand
        self.box1.append(self.quit_button)

        self.resolution640x480_button = Gtk.Button.new()
        self.resolution640x480_button.set_label("640x480")
        self.resolution640x480_button.connect("clicked",self.change_resolution, 640, 480)
        self.box1.append(self.resolution640x480_button)

        self.resolution800x600_button = Gtk.Button.new()
        self.resolution800x600_button.set_label("800x600")
        self.resolution800x600_button.connect("clicked",self.change_resolution, 800, 600)
        self.box1.append(self.resolution800x600_button)

        self.resolution1024x768_button = Gtk.Button.new()
        self.resolution1024x768_button.set_label("1024x768")
        self.resolution1024x768_button.connect("clicked",self.change_resolution, 1024, 768)
        self.box1.append(self.resolution1024x768_button)

        self.connect("close-request", quit_)
        self.show()
        self.fullscreen()

    def change_resolution(self, change_resolution, a, b):
        self.unfullscreen()
        self.set_default_size(a,b)
        self.set_default_size(a,b)
        

    def on_quit_button_clicked(self,quit_clicked_button):
        quit_(self)

    def on_about_button_clicked(self,about_clicked_button,msg):
        print(msg)


if __name__ == "__main__":
    Ventana()
    loop = GLib.MainContext().default()
    while not QUIT:
        loop.iteration(True)
