import sys
import gi
import pathlib
from rdkit import Chem
from os import remove
from rdkit.Chem import Draw

gi.require_version('Gtk', '4.0')

from gi.repository import Gio, GObject, Gtk, Gdk

class Widget(GObject.Object):
    __gtype_name__ = 'Widget'

    def __init__(self, name):
        super().__init__()
        self._name = name

    @GObject.Property
    def name(self):
        return self._name
    
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = self.get_application()
        self.path_mol = ""

        # Crear Header Bar
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Visualizador")

        # Crear el menu button
        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=Gio.Menu())
        menu_button.set_create_popup_func(self.clicked_menu_button)
        header_bar.pack_end(child=menu_button)

        # Crear el Button para el Filechooser
        self.button = Gtk.Button.new_with_label("Abrir")
        self.button.connect("clicked",self.on_button_clicked)

        # Crear la ventana que guarda
        self._native = self.dialogo_save()
        self._native.connect("response", self.on_file_save_response)

        # Crear el model del dropdown
        self.dropdown_model = Gio.ListStore(item_type=Widget)
        self.lista_dropdown = []
        self.add_data_to_model(self.lista_dropdown)

        # Crear el factory del dropdown
        self.dropdown_factory = Gtk.SignalListItemFactory()
        self.dropdown_factory.connect("setup", self.dropdown_factory_setup)
        self.dropdown_factory.connect("bind", self.dropdown_factory_bind)

        # Crear el dropdown
        self.dropdown = Gtk.DropDown(model=self.dropdown_model, factory=self.dropdown_factory)
        self.dropdown.connect("notify::selected-item", self.on_change_item_dropdown)

        # Crear el Gtk.image
        self.image = Gtk.Image.new()
        self.image.set_pixel_size(300)

        # Crear la ventana
        self.main_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 10)
        self.set_child(self.main_box)
        self.main_box.append(self.button)
        self.main_box.append(self.dropdown)
        self.main_box.append(self.image)
        

    def add_data_to_model(self, list):
        for i in self.lista_dropdown:
            self.dropdown_model.append(Widget(name=i))
        # Agrega 


    def dropdown_factory_setup(self, dropdown_factory, list_item):
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        box.append(label)
        list_item.set_child(box)


    def dropdown_factory_bind(self, dropdown_factory, list_item):
        box = list_item.get_child()
        label = box.get_first_child()
        widget = list_item.get_item()
        label.set_text(widget.name)

    def clicked_menu_button(self, button):
        # Crear el about Dialog
        about_header = Gtk.AboutDialog.new()
        about_header.set_authors(['Cristian Pavez'])
        about_header.set_program_name(self.get_title()) 
        about_header.show()
    

    def on_button_clicked(self, button):
        self._native.show()


    def dialogo_save(self):
        return Gtk.FileChooserNative(title="Seleccionar Carpeta",
                                     action=Gtk.FileChooserAction.SELECT_FOLDER,
                                     transient_for=self.get_root(),
                                     accept_label="_Seleccionar",
                                     cancel_label="_Cancelar",
                                    )


    def on_file_save_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            path = native.get_file().get_path()
            self.path_mol = path
            directorio = pathlib.Path(path)
            archivos_mol = [fichero.name[:-4] for fichero in directorio.iterdir() if directorio.glob(".mol")]
            self.lista_dropdown = archivos_mol
            self.dropdown_model.remove_all()
            self.add_data_to_model(self.lista_dropdown)


    def on_change_item_dropdown(self, dropdown, data):
        item_name = dropdown.get_selected_item()._name
        m = Chem.MolFromMolFile(f"{self.path_mol}/{item_name}.mol")
        img = Draw.MolToImage(m)
        img.save("temp.png")
        self.image.set_from_file("temp.png")
        remove("temp.png")


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()

app = MyApp(application_id="com.uwu",flags= Gio.ApplicationFlags.FLAGS_NONE)
app.run(sys.argv)