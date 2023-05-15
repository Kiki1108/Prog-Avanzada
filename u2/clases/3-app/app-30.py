import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gio

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_ = self.get_application()

        self.button = Gtk.Button.new_with_label("Quit")
        self.button.connect("clicked",self.on_quit_button_clicked)

        self.add(self.button)
        self.button.show()

    def on_quit_button_clicked(self,clicked_button):
        self.app_.quit()

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

app = MyApp(application_id="cl.bioinfo.myapplicationexample",flags= Gio.ApplicationFlags.FLAGS_NONE)
app.run(sys.argv)
