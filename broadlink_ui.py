import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import subprocess
import json

device_path = "/home/blu/broadlink/BEDROOM.device"
file_path = "/home/blu/broadlink/broadlink-devices.json"
button_frame = None
prev_selected_device = None

def update_window_size():
    if button_frame is None:
        return

    window.update_idletasks()
    content_width = button_frame.winfo_reqwidth()
    content_height = button_frame.winfo_reqheight()

    # Set a minimum width and height to prevent the window from being too small
    min_width = 200
    min_height = 200

    # Calculate the new window size by adding some padding
    window_width = content_width + 20
    window_height = content_height + 60

    # Ensure that the window width and height are not smaller than the minimum values
    window_width = max(window_width, min_width)
    window_height = max(window_height, min_height)

    # Get the current window position
    x = window.winfo_x()
    y = window.winfo_y()

    # Set the window size without changing the position
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def send_data(data_path):
    command = f"broadlink_cli --device @{device_path} --send @{data_path}"
    subprocess.run(command, shell=True)


def on_button_click(data_path):
    send_data(data_path)


def copy_command_line(data_path):
    window.clipboard_clear()
    command = f"broadlink_cli --device @{device_path} --send @{data_path}"
    window.clipboard_append(command)
    show_message_toast("Command copied to clipboard!")


def update_buttons(*args):
    global button_frame, prev_selected_device
    clear_buttons()

    selected_device = devices_dropdown.get()
    if selected_device == prev_selected_device:
        return

    prev_selected_device = selected_device
    data_paths = devices[selected_device]

    button_frame = ttk.Frame(window)
    button_frame.pack(padx=10, pady=10)

    row_counter = 0
    col_counter = 0
    max_columns = 3

    for category, entries in data_paths.items():
        if col_counter != 0:
            row_counter += 1
        col_counter = 0

        category_label = ttk.Label(button_frame, text=category)
        category_label.grid(row=row_counter, column=col_counter, sticky="w", padx=5, pady=5, columnspan=max_columns)
        row_counter += 1

        for label, path in entries.items():
            button = ttk.Button(
                button_frame,
                text=label,
                command=lambda path=path: on_button_click(path),
                width=20
            )
            button.grid(row=row_counter, column=col_counter, padx=5, pady=(0, 5), sticky="w")

            button.bind("<Button-3>", lambda event, path=path: show_context_menu(event, path))

            col_counter += 1
            if col_counter >= max_columns:
                col_counter = 0
                row_counter += 1

    window.after(100, update_window_size)  # Update the window size after 100 milliseconds


def show_context_menu(event, data_path):
    context_menu = tk.Menu(window, tearoff=0)
    context_menu.add_command(label="Copy Command Line", command=lambda: copy_command_line(data_path))
    context_menu.tk_popup(event.x_root, event.y_root)


def clear_buttons():
    global button_frame
    if button_frame is not None:
        button_frame.destroy()
        button_frame = None


with open(file_path) as file:
    devices = json.load(file)


def handle_keypress(event):
    if event.keysym == "Up":
        move_dropdown_selection(-1)
    elif event.keysym == "Down":
        move_dropdown_selection(1)
    elif event.keysym == "Tab":
        move_focus_forward()
    elif event.keysym == "ISO_Left_Tab":
        move_focus_backward()
    elif event.widget == devices_dropdown:
        return "break"  # Prevent other keys from changing the dropdown selection
    return None  # Allow other key events to be processed


def move_dropdown_selection(offset):
    current_index = devices_dropdown.current()
    new_index = (current_index + offset) % len(devices)
    devices_dropdown.current(new_index)
    update_buttons()


def move_focus_forward():
    focus_next = window.focus_get().tk_focusNext()
    if focus_next:
        focus_next.focus_set()


def move_focus_backward():
    focus_prev = window.focus_get().tk_focusPrev()
    if focus_prev:
        focus_prev.focus_set()


def show_message_toast(message):
    toast_label = ttk.Label(window, text=message)
    toast_label.place(relx=0.5, rely=0.9, anchor="center")
    window.after(2000, lambda: toast_label.destroy())


window = ThemedTk(theme="arc")  # Specify the desired theme ("arc" in this example)
window.title("Broadlink Device Control")
window.geometry("400x400")
window.bind("<KeyPress>", handle_keypress)
window.configure(bg="#36393F")  # Use the color code for Discord's dark gray

selected_device = tk.StringVar(window)
devices_dropdown = ttk.Combobox(window, textvariable=selected_device)
devices_dropdown.pack(pady=10)

devices_dropdown["values"] = tuple(devices.keys())
devices_dropdown.current(0)
devices_dropdown.bind("<<ComboboxSelected>>", update_buttons)

update_buttons()  # Update buttons on application start

window.after(100, update_window_size)  # Update the window size after 100 milliseconds
window.mainloop()
