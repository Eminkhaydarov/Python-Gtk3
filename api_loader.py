import concurrent.futures
import requests
import gi
from gi.repository import GLib

gi.require_version("Gtk", "3.0")


def load_data(urls, callback):
    rows = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {
            executor.submit(requests.get, url): url for url in urls
        }

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                response = future.result()
                if response.status_code == 200:
                    data = response.json()
                    for item in data:
                        rows.append(item)
            except Exception as e:
                print(f"Error fetching data from {url}: {str(e)}")

    GLib.idle_add(callback, rows)