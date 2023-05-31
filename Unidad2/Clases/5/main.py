import sys
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GObject
from dialog import ExampleDialog

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(600, 250)
        self.set_title("Ejemplo")

        # Main layout containers
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now

        self.grid1 = Gtk.GridView()
        self.box3.append(self.grid1)


        self.label = Gtk.Label()
        self.label1 = Gtk.Label()
        self.label2= Gtk.Label()
        self.box3.append(self.label)
        self.box3.append(self.label1)

        # Add a button
        self.button = Gtk.Button(label="Hola")
        self.button.connect('clicked', self.hello)
        self.box2.append(self.button)  # But button in the first of
        # the two vertical boxes

        # Save Button
        self.button_save = Gtk.Button(label="Guardar")
        self.button_save.connect('clicked', self.save)
        self.box2.append(self.button_save)

        # Read Button
        self.open_button = Gtk.Button(label="Abrir")
        self.open_button.connect('clicked', self.open)
        self.box2.append(self.open_button)

        self.button_open_dialog = Gtk.Button(label="Abrir Dialogo")
        self.button_open_dialog.connect('clicked', self.open_dialog)
        self.box2.append(self.button_open_dialog)

        # Add a check button
        self.check = Gtk.CheckButton(label="Chao")
        self.box2.append(self.check)

        self._native = self.dialog_save()
        self._native.connect("response", self.on_file_save_response)

        self._native2 = self.dialog_open()
        self._native2.connect("response", self.on_file_open_response)

        # Atributo de clase Dialgo
        self.entrada_texto = None


    def on_dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            print("Presionó OK")
            self.entrada_texto = dialog.entrada_texto.get_text()
            self.label1.set_text(dialog.entrada_texto.get_text())

        elif response == Gtk.ResponseType.CANCEL:
            print("Presionó Cancelar")

        dialog.close()

    def open_dialog(self, button):
        dialog = ExampleDialog(parent=self.get_root())
        dialog.connect("response", self.on_dialog_response)
        dialog.set_visible(True)


    def on_file_save_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            _path = native.get_file().get_path()
            print(_path)

            with open(_path, "w") as _file:
                _file.write(f'{self.entrada_texto} - {self.label.get_text()}\n')

        self._native = None

    
    def on_file_open_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            _path = native.get_file().get_path()
            print(_path)

            with open(_path, "r") as _file:
                self.label.set_text(_file.read())

        self._native2 = None


    def dialog_save(self):
        return Gtk.FileChooserNative(title="Save File",
                                     # "self.main_window" is defined elsewhere as a Gtk.Window
                                     #transient_for=self.main_window,
                                     action=Gtk.FileChooserAction.SAVE,
                                     accept_label="_Save",
                                     cancel_label="_Cancel",
                                     )

    def dialog_open(self):
        return Gtk.FileChooserNative(title="Save File",
                                     # "self.main_window" is defined elsewhere as a Gtk.Window
                                     #transient_for=self.main_window,
                                     action=Gtk.FileChooserAction.OPEN,
                                     accept_label="_Open",
                                     cancel_label="_Cancel",
                                     )
    
    def save(self, button):
        self._native.show()

    def open(self, button):
        self._native2.show()

    def hello(self, button):
        print("Hola Mundo")
        self.label.set_text("Hola Mundo")
        if self.check.get_active():
            print("Chao Mundo!")
            self.close()


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
