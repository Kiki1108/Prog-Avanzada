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
        self.search_text_method = ''

        self.app_ = self.get_application()

        self.main_vertical_box = Gtk.Box.new( Gtk.Orientation.VERTICAL,10) #(orientation VERTICAL|HORIZONTAL  , spacing in pixels)
        self.set_child(self.main_vertical_box)

        data_to_show = ["",
                        "Male",
                        "Female",
                        "uwu"]

        # Se crea el model 1
        self.dropdown1_model = Gio.ListStore(item_type=DropDown)
        for names in range(1,4):
            self.dropdown1_model.append(DropDown(name=data_to_show[names]))

        # Se crea el factory 1
        dropdown1_factory = Gtk.SignalListItemFactory()
        dropdown1_factory.connect("setup", self._on_dropdown_factory_setup)
        dropdown1_factory.connect("bind", self._on_dropdown_factory_bind)

        # Se crea el Dropdown 1
        self.dropdown1 = Gtk.DropDown(model=self.dropdown1_model, factory=dropdown1_factory)
        self.main_vertical_box.append(self.dropdown1)

        # Se crea el botón del Dropdown 1
        print_button1 = Gtk.Button.new()
        print_button1.props.label = "Print actived text From DropboxText1 "
        print_button1.connect("clicked",self.on_print_button_clicked,self.dropdown1)
        self.main_vertical_box.append(print_button1)

        # Se crea el model 2
        self.dropdown2_model = Gio.ListStore(item_type=DropDown)
        self.sort_model_method  = Gtk.SortListModel(model=self.dropdown2_model) # FIXME: Gtk.Sorter?
        self.filter_model_method = Gtk.FilterListModel(model=self.sort_model_method)
        self.filter_method = Gtk.CustomFilter.new(self._do_filter_method_view, self.filter_model_method)
        self.filter_model_method.set_filter(self.filter_method)
        
        for names in data_to_show:
            self.dropdown2_model.append(DropDown(name=names))       

        # Se crea el factory 2
        dropdown2_factory = Gtk.SignalListItemFactory()
        dropdown2_factory.connect("setup", self._on_dropdown_factory_setup)
        dropdown2_factory.connect("bind", self._on_dropdown_factory_bind)

        # Crear entry
        self.entry = Gtk.Entry()
        self.main_vertical_box.append(self.entry)
        sumbit_button = Gtk.Button.new()
        sumbit_button.props.label = "Sumbit"
        sumbit_button.connect("clicked",self.on_sumbit_button_cliked,dropdown2_factory)
        self.main_vertical_box.append(sumbit_button) 

        # Se crea el Dropdown 2
        self.dropdown2 = Gtk.DropDown(model=self.filter_model_method, factory=dropdown2_factory)
        self.dropdown2.set_enable_search(True)
        self.dropdown2.connect("notify::selected-item", self._on_selected_widget, data_to_show)
        self.main_vertical_box.append(self.dropdown2)

        # Se implementa el search
        search_entry = self._get_search_entry()
        search_entry.connect('search-changed', self._on_search_changed)

        # Se crea el botón del Dropdown 2
        print_button2 = Gtk.Button.new()
        print_button2.props.label = "Print actived text From DropboxText2 "
        print_button2.connect("clicked",self.on_print_button_clicked,self.dropdown2)
        self.main_vertical_box.append(print_button2)

    def _get_search_entry(self):
        popover = self.dropdown2.get_last_child()
        box = popover.get_child()
        box2 = box.get_first_child()
        search_entry = box2.get_first_child()
        return search_entry
    
    def _on_search_changed(self, search_entry):
        self.search_text = search_entry.get_text()
        self.filter_method.changed(Gtk.FilterChange.DIFFERENT)

    def _do_filter_method_view(self, item, filter_list_model):
        return self.search_text_method.upper() in item.name.upper()

    def _on_dropdown_factory_setup(self, factory, list_item):
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        box.append(label)
        list_item.set_child(box)

    def _on_selected_widget(self, dropdown, data, data_to_show):
        pass

    def _on_dropdown_factory_bind(self, factory, list_item):
        box = list_item.get_child()
        label = box.get_first_child()
        method = list_item.get_item()
        label.set_text(method.name)

    def on_print_button_clicked(self,p_button, dropdown):
        print(dropdown.get_selected_item()._name)

    def on_sumbit_button_cliked(self, button, factory):
        entry = self.entry.get_text()
        models = self.dropdown2.get_model()
        lista = [entry]
        # Forma de crear nuevas opciones
        """
        for i in models:
            lista.append(i._name)
        """
        # Forma de reemplazar la opción
        for i in range(1,4):
            lista.append(models.get_item(i)._name)
        
        self.dropdown2_model.remove_all()

        for item in lista:
            self.dropdown2_model.append(DropDown(name=item))


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
