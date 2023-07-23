import asyncio

import threading


import httpx

import gi
from gi.repository import GLib

gi.require_version("Gtk", "3.0")


class ApiLoader(threading.Thread):
    def __init__(self, urls, callback, spinner_window):
        threading.Thread.__init__(self)
        self.urls = urls
        self.callback = callback
        self.spinner_window = spinner_window

    def run(self):
        rows = []

        async def fetch_data(url):
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                if response.status_code == 200:
                    data = response.json()
                    for item in data:
                        rows.append(item)

        async def fetch_all():
            await asyncio.gather(*[fetch_data(url) for url in self.urls])

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(fetch_all())

        GLib.idle_add(self.callback, rows)
        GLib.idle_add(self.spinner_window.destroy)