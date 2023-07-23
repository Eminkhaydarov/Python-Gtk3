import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")
from csv_loader import CsvLoader


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Мое приложение")
        self.set_default_size(800, 600)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        button_api = Gtk.Button(label="Загрузить из API")
        vbox.pack_start(button_api, False, False, 0)

        button_file = Gtk.Button(label="Загрузить из файла")
        button_file.connect("clicked", self.on_button_file_clicked)
        vbox.pack_start(button_file, False, False, 0)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.EXTERNAL)
        vbox.pack_start(scrolled_window, True, True, 0)

        self.listbox = Gtk.ListBox()
        scrolled_window.add(self.listbox)

    def on_button_file_clicked(self, button):
        default_file_path = "snakes_count_1000.csv"

        loader = CsvLoader(default_file_path, self.update_listbox)
        loader.start()
        self.listbox.foreach(
            Gtk.Widget.destroy
        )  # Очищаем список перед загрузкой нового файла

    def update_listbox(self, rows):
        for row in rows:
            row_str = str(row)
            row_label = Gtk.Label(label=row_str, wrap=True)
            self.listbox.add(row_label)

            # Установка свойства expand для метки, чтобы переносить строки по ширине окна
            row_label.set_xalign(0)
            row_label.set_hexpand(True)

        self.listbox.show_all()
