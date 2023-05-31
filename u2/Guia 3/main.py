import sys
import gi

gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')
from gi.repository import Adw, Gio, GObject, Gtk

# Conversión del ejemplo con "combobox" a "drop down"

class DropDown(GObject.Object):
    __gtype_name__ = 'DropDown'

    def __init__(self, name):
        super().__init__()
        self._name = name

    @GObject.Property
    def name(self):
        return self._name

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_ = self.get_application()
        self.set_default_size(300, 150)

        data_to_show = ["Male",
                        "Female",
                        "uwu"]

        # Se crea el model
        self.dropdown_model = Gio.ListStore(item_type=DropDown)
        for item in data_to_show:
            self.dropdown_model.append(DropDown(name=item))

        # Se crea el factory
        dropdown_factory = Gtk.SignalListItemFactory()
        dropdown_factory.connect("setup", self._on_dropdown_factory_setup)
        dropdown_factory.connect("bind", self._on_dropdown_factory_bind)

        # Se crea el Dropdown
        self.dropdown = Gtk.DropDown(model=self.dropdown_model, factory=dropdown_factory)
        self.dropdown.connect("notify::selected-item", self._on_selected)

        # Se crea el botón para seleccionar
        button = Gtk.Button.new()
        button.props.label = "    ----Seleccionar----    "
        button.connect("clicked",self.on_print_button_clicked)

        # Se Crear y adjuntan al box
        self.main_vertical_box = Gtk.Box.new( Gtk.Orientation.VERTICAL,10)
        self.set_child(self.main_vertical_box)
        self.main_vertical_box.append(self.dropdown)
        self.main_vertical_box.append(button)


    def _on_dropdown_factory_setup(self, factory, list_item):
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        box.append(label)
        list_item.set_child(box)


    def _on_dropdown_factory_bind(self, factory, list_item):
        box = list_item.get_child()
        label = box.get_first_child()
        method = list_item.get_item()
        label.set_text(method.name)


    def on_print_button_clicked(self,p_button):
        print(f"Seleccionó: {self.dropdown.get_selected_item()._name}")

    
    def _on_selected(self, dropdown, data):
        print(f"Cambió la selección a: {self.dropdown.get_selected_item()._name}")



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

app = MyApp(application_id="com.drop_down",flags= Gio.ApplicationFlags.FLAGS_NONE)
app.run(sys.argv)
