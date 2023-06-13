import sys
import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gio, GObject, Gtk

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
        self.app_ = self.get_application()

        # Crear el model
        self.model = Gio.ListStore(item_type=Widget)
        list = ["First", "Second", "third"]
        self.add_data_to_model(list)

        # Crear el factory
        self.factory = Gtk.SignalListItemFactory()
        self.factory.connect("setup", self.factory_setup)
        self.factory.connect("bind", self.factory_bind)

        # Crear el dropdown
        self.dropdown = Gtk.DropDown(model=self.model, factory=self.factory)

        # Crear la ventana
        self.main_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 10)
        self.set_child(self.main_box)
        self.main_box.append(self.dropdown)

    
    def add_data_to_model(self, list):
        for i in list:
            self.model.append(Widget(name=i))


    def factory_setup(self, factory, list_item):
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        box.append(label)
        list_item.set_child(box)


    def factory_bind(self, factory, list_item):
        box = list_item.get_child()
        label = box.get_first_child()
        widget = list_item.get_item()
        label.set_text(widget.name)


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