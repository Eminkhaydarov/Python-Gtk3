import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")



class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Мое приложение")
        self.set_default_size(800, 600)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        button_api = Gtk.Button(label="Загрузить из API")
        vbox.pack_start(button_api, False, False, 0)

        button_file = Gtk.Button(label="Загрузить из файла")
        vbox.pack_start(button_file, False, False, 0)

