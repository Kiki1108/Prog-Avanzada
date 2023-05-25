import sys
import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk
from ventana_exito import Exito

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(800, 600)
        self.set_title("Guía 2")

        # Se incia una box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(self.box)

        # En la box se pone un label arriba, que indica que escriba
        self.label = Gtk.Label()
        self.label.set_text("Escriba")
        self.label.props.vexpand = True
        self.label.props.hexpand = True
        self.box.append(self.label)

        # En la mitad de la box se pone una entrada de texto
        self.entrada_texto = Gtk.Entry()
        self.entrada_texto.props.hexpand = True
        self.box.append(self.entrada_texto)

        # Se crea un botón para guardar
        self.button = Gtk.Button(label="Guardar")
        self.button.props.vexpand = True
        self.button.props.hexpand = True
        self.button.connect('clicked', self.save)
        self.box.append(self.button)

        # Se crea la ventana que guarda
        self._native = self.dialogo_save()
        self._native.connect("response", self.on_file_save_response)

    # Toma lo escrito en la entrada de texto, luego muestra la ventana que guarda
    def save(self, button):
        texto = self.entrada_texto.get_text()
        print(texto)
        self._native.show()

    # Ventana de guardado
    def dialogo_save(self):
        return Gtk.FileChooserNative(title="Save File",
                                     action=Gtk.FileChooserAction.SAVE,
                                     transient_for=self.get_root(),
                                     accept_label="_Save",
                                     cancel_label="_Cancel",
                                    )


    # Evalua si se presionó aceptar en el guardado, para así guardar el archivo
    # Con lo escrito en la entrada de texto
    def on_file_save_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            _path = native.get_file().get_path()
            print(_path)
            self.open_dialogo_exito()

            with open(_path, "w") as _file:
                _file.write(f"{self.entrada_texto.get_text()}\n")

    # Abre la ventana de éxito
    def open_dialogo_exito(self):
        dialog = Exito(parent=self.get_root())
        dialog.connect("response", self.on_dialog_response)
        dialog.set_visible(True)


    # Evaluá si se presionó ok en la ventana de éxito
    def on_dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            print("Presionó OK")
        dialog.close()
        # Tambien se puede cerrar la aplicación al momento de guardar
        #self.get_application().quit()


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)


    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


def main():
    app = MyApp(application_id="com.guia2.GtkApplication")
    app.run(sys.argv)

if __name__ == "__main__":
    main()
