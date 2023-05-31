import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GObject


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(600, 250)
        self.set_title("Ejemplo")

        # Main layout containers
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)

        self.grid1 = Gtk.GridView()
        self.box3.append(self.grid1)


        self.label = Gtk.Label()
        self.label1 = Gtk.Label()
        self.label2= Gtk.Label()
        self.box3.append(self.label)

        # Add a button
        self.button = Gtk.Button(label="Hola")
        self.button.connect('clicked', self.hello)
        self.box2.append(self.button)

        # Save Button
        self.button_save = Gtk.Button(label="Guardar")
        self.button_save.connect('clicked', self.save)
        self.box2.append(self.button_save)

        #Entry Text
        self.name = Gtk.Entry()
        self.name.props.placeholder_text = "Hola"
        self.box3.append(self.name)

        # Add a check button
        self.check = Gtk.CheckButton(label="Chao")
        self.check2 = Gtk.CheckButton(label="Otro")
        self.check3 = Gtk.CheckButton(label="Otro mas")
        self.box2.append(self.check)
        self.box2.append(self.check2)
        self.box2.append(self.check3)

        self._native = Gtk.FileChooserNative(title="Save File",
                                             # "self.main_window" is defined elsewhere as a Gtk.Window
                                             #transient_for=self.main_window,
                                             action=Gtk.FileChooserAction.SAVE,
                                             accept_label="_Save",
                                             cancel_label="_Cancel",
                                             )

        self._native.connect("response", self.on_file_save_response)

    def on_file_save_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            print("Presionó el botón aceptar")
            self.save_file(native.get_file())
        self._native = None


    def save(self, button):
        self._native = Gtk.FileChooserNative(title="Save File",
                                             # "self.main_window" is defined elsewhere as a Gtk.Window
                                             transient_for=self.get_root(),
                                             action=Gtk.FileChooserAction.SAVE,
                                             accept_label="_Save",
                                             cancel_label="_Cancel",
                                             )
        
        self._native.show()


    def hello(self, button):
        print("Hola Mundo")
        valor = self.name.get_text()
        self.label.set_text(valor)

        if self.check.get_active():
            print("Chao Mundo!")
            self.close()



class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
