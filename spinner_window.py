import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")


class SpinnerWindow(Gtk.Dialog):
    def __init__(self, parent_window):
        Gtk.Dialog.__init__(self, title="Загрузка...", parent=parent_window)
        self.set_default_size(200, 100)
        box = self.get_content_area()
        self.spinner = Gtk.Spinner()
        box.pack_start(self.spinner, True, True, 0)
        self.spinner.start()

    def destroy(self):
        self.spinner.stop()
        Gtk.Dialog.destroy(self)
