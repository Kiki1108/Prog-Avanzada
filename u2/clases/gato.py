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
        #(orientation VERTICAL|HORIZONTAL  , spacing in pixels)
        self.main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL,10)
        self.box1 = Gtk.Box.new(Gtk.Orientation.VERTICAL,10)
        self.box2 = Gtk.Box.new(Gtk.Orientation.VERTICAL,10)
        self.box3 = Gtk.Box.new(Gtk.Orientation.VERTICAL,10)
        self.box4 = Gtk.Box.new(Gtk.Orientation.VERTICAL,10)

        self.set_child(self.main_box)
        self.main_box.append(self.box1)
        self.main_box.append(self.box2)
        self.main_box.append(self.box3)
        self.main_box.append(self.box4)

        self.quit_button = Gtk.Button.new_with_label("Quit")
        self.quit_button.connect("clicked",self.on_quit_button_clicked)
        self.quit_button.props.vexpand = True
        self.quit_button.props.hexpand = True  

        self.button1 = Gtk.Button.new()
        self.button1.connect("clicked",self.x, self.button1)
        self.button1.props.vexpand = True 
        self.button1.props.hexpand = True

        self.button2 = Gtk.Button.new()
        self.button2.connect("clicked",self.x, self.button2)
        self.button2.props.vexpand = True 
        self.button2.props.hexpand = True

        self.button3 = Gtk.Button.new()
        self.button3.connect("clicked",self.x, self.button3)
        self.button3.props.vexpand = True 
        self.button3.props.hexpand = True

        self.button4 = Gtk.Button.new()
        self.button4.connect("clicked",self.x, self.button4)
        self.button4.props.vexpand = True 
        self.button4.props.hexpand = True

        self.button5 = Gtk.Button.new()
        self.button5.connect("clicked",self.x, self.button5)
        self.button5.props.vexpand = True 
        self.button5.props.hexpand = True

        self.button6 = Gtk.Button.new()
        self.button6.connect("clicked",self.x, self.button6)
        self.button6.props.vexpand = True 
        self.button6.props.hexpand = True

        self.button7 = Gtk.Button.new()
        self.button7.connect("clicked",self.x, self.button7)
        self.button7.props.vexpand = True 
        self.button7.props.hexpand = True

        self.button8 = Gtk.Button.new()
        self.button8.connect("clicked",self.x, self.button8)
        self.button8.props.vexpand = True 
        self.button8.props.hexpand = True

        self.button9 = Gtk.Button.new()
        self.button9.connect("clicked",self.x,self.button9)
        self.button9.props.vexpand = True 
        self.button9.props.hexpand = True

        self.box1.append(self.quit_button)
        self.box2.append(self.button1)
        self.box2.append(self.button2)
        self.box2.append(self.button3)
        self.box3.append(self.button4)
        self.box3.append(self.button5)
        self.box3.append(self.button6)
        self.box4.append(self.button7)
        self.box4.append(self.button8)
        self.box4.append(self.button9)

        self.connect("close-request", quit_)
        self.show()
        self.set_default_size(800,600)

    def x(self, x, button):
        button.set_label("X")

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
