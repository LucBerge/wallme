import tkinter as tk
from PIL import ImageTk, Image
from .websites import WEBSITES
from .managers.managerfactory import ManagerFactory
import threading
import os
from . import utils


class WallmeCanvas(tk.Canvas):

    def create_text(self, x1, y1, x2, y2, **kwargs):
        text = super().create_text(
            int((x2 + x1) / 2),
            int((y2 + y1) / 2),
            **kwargs
        )
        return text

    def create_image(self, x1, y1, x2, y2, path):
        if (os.path.exists(path)):
            image = Image.open(path)
            image = image.resize((x2 - x1, y2 - y1))
            self.photo_image = ImageTk.PhotoImage(image)
        else:
            self.photo_image = None
        label = tk.Label(self, image=self.photo_image)
        label.place(x=0, y=0)
        return label

    def create_list_box(self, x1, y1, x2, y2):
        var = tk.Variable(value=tuple([key.replace('-', ' ').capitalize() for key in WEBSITES.keys()]))
        listbox = tk.Listbox(
            self,
            listvariable=var,
            selectmode=tk.SINGLE,
            width=int((x2 - x1) * 82 / 500),
            height=int((y2 - y1) * 13 / 220),
        )
        listbox.place(x=x1, y=y1)
        return listbox

    def create_button(self, x1, y1, x2, y2, **kwargs):
        button = tk.Button(
            self,
            **kwargs)
        button.place(x=x1, y=y1)
        return button

    def create_entry(self, x1, y1, x2, y2, callback, **kwargs):
        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
        entry = tk.Entry(self, textvariable=sv, **kwargs)
        entry.place(x=x1, y=y1)
        return sv


class Gui(tk.Tk):
    TITLE = "Wallme"

    COLOR_WHITE = "#FFFFFF"
    COLOR_LIGHT_GREY = "#D7D7D7"
    COLOR_GREY = "#7C7C7C"
    COLOR_LIGHT_BLUE = "#00A3FF"

    def __init__(self):
        super().__init__()

        # Get manager
        manager_factory = ManagerFactory()
        self.manager = manager_factory.get_manager()

        # configure the root window
        self.title(self.TITLE)
        self.geometry("1110x543")
        self.configure(bg=self.COLOR_LIGHT_GREY)

        # canvas
        canvas = WallmeCanvas(
            self,
            bg=self.COLOR_LIGHT_GREY,
            height=543,
            width=1110,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # IMAGE
        self.image = canvas.create_image(
            0,
            0,
            960,
            540,
            "")

        # LIST LABEL
        canvas.create_text(
            970,
            10,
            970,
            30,
            text="Website",
            anchor="w")

        # LIST
        self.listbox = canvas.create_list_box(
            970,
            30,
            1100,
            400)
        self.listbox.bind('<<ListboxSelect>>', self.list_items_selected)

        # SUBKEY LABEL
        canvas.create_text(
            970,
            370,
            970,
            390,
            text="Subkey",
            anchor="w")

        # SUBKEY ENTRY
        self.subkey_entry = canvas.create_entry(
            970,
            390,
            1100,
            410,
            self.entry_has_changed,
            width=20)

        # SET
        self.set_button = canvas.create_button(
            970,
            420,
            1100,
            440,
            text="SET",
            width=17,
            command=self.set)

        # INFO
        self.info_button = canvas.create_button(
            970,
            450,
            1100,
            470,
            text="INFO",
            width=17,
            command=self.info)

        # SET STARTUP
        self.set_startup_button = canvas.create_button(
            970,
            480,
            1100,
            500,
            text="SET STARTUP",
            width=17,
            command=self.set_startup)
        self.set_startup_button["state"] = tk.DISABLED

        # UNSET STARTUP
        self.unset_startup_button = canvas.create_button(
            970,
            510,
            1100,
            530,
            text="UNSET STARTUP",
            width=17,
            command=self.unset_startup)
        self.unset_startup_button["state"] = tk.DISABLED

        # Get current startup value
        fullkey = self.manager.get_startup()
        # If startup value exists
        if (fullkey is not None):
            # Get key and subkey
            key, subkey = utils.get_key_subkey_from_fullkey(fullkey)
            # Set subkey entry value
            if (subkey is not None):
                self.subkey_entry.set(subkey)
            # Get index
            index = list(WEBSITES).index(key)
            # Select item in list box
            self.listbox.select_set(index)
            # Create event
            self.list_items_selected(None)

    def update_image(self, key):
        try:
            # Download image
            image_path = self.manager.download(key, True)
            # Set image
            new_image = Image.open(image_path)
            new_image = new_image.resize((960, 540))
            photo_image = ImageTk.PhotoImage(new_image)
            self.image.configure(image=photo_image)
            self.image.image = photo_image
        except Exception:
            self.image.configure(image=None)
            self.image.image = None

    def get_selected_key(self):
        if (len(self.listbox.curselection()) == 0):
            return None
        # Get index
        index = self.listbox.curselection()[0]
        # Get key
        key = list(WEBSITES.keys())[index]
        # Get subkey
        subkey = self.subkey_entry.get()
        if (subkey == ""):
            return key
        else:
            return key + "." + subkey

    def list_items_selected(self, event):
        # Get key
        fullkey = self.get_selected_key()
        # If key is not None
        if (fullkey is not None):
            # Get current startup value
            current_startup = self.manager.get_startup()
            # If selected item is the startup value
            if ((current_startup is not None) and ((current_startup in fullkey) or (fullkey in current_startup))):
                # Disable set startup button
                self.set_startup_button["state"] = tk.DISABLED
                # Enable unset startup button
                self.unset_startup_button["state"] = tk.NORMAL
            else:
                # Enable set startup button
                self.set_startup_button["state"] = tk.NORMAL
                # Disable unset startup button
                self.unset_startup_button["state"] = tk.DISABLED

            # Enable set button
            self.set_button["state"] = tk.NORMAL
            # Enable info button
            self.info_button["state"] = tk.NORMAL

            # Set image
            thread = threading.Thread(target=self.update_image, args=(fullkey,))
            thread.start()

    def entry_has_changed(self, entry):
        # Clear listbox selection
        self.listbox.selection_clear(0, 'end')
        # Disable set button
        self.set_button["state"] = tk.DISABLED
        # Disable info button
        self.info_button["state"] = tk.DISABLED
        # Disable set startup button
        self.set_startup_button["state"] = tk.DISABLED
        # Disable unset startup button
        self.unset_startup_button["state"] = tk.DISABLED

    def set(self):
        # Get key
        fullkey = self.get_selected_key()
        # Set
        thread = threading.Thread(target=self.manager.set, args=(fullkey,))
        thread.start()

    def info(self):
        # Get index
        fullkey = self.get_selected_key()
        # Info
        self.manager.info(fullkey)

    def set_startup(self):
        # Get index
        fullkey = self.get_selected_key()
        # Disable set startup button
        self.set_startup_button["state"] = tk.DISABLED
        # Enable unset startup button
        self.unset_startup_button["state"] = tk.NORMAL
        # Set startup
        self.manager.set_startup(fullkey)

    def unset_startup(self):
        # Enable set startup button
        self.set_startup_button["state"] = tk.NORMAL
        # Disable unset startup button
        self.unset_startup_button["state"] = tk.DISABLED
        # Unset startup
        self.manager.unset_startup()
