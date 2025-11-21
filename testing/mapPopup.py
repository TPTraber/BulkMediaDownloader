import tkinter as tk
from tkinter import ttk
import tkintermapview

root = tk.Tk()

root.minsize(width=400, height=600)

root.title("Map Test")

root.grid_columnconfigure(0, weight=1)

def mapPopup():
    win = tk.Toplevel(root)
    win.title("Choose Location")

    coords = tk.StringVar()

    textBox = ttk.Entry(win,width=50, textvariable=coords)
    textBox.grid(column=0,row=0)

    map_widget = tkintermapview.TkinterMapView(win, width=800, height=600, corner_radius=50)
    map_widget.grid(column=0,row=1)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
    address = tkintermapview.convert_address_to_coordinates("Williamsburg")
    map_widget.set_position(address[0],address[1])
    map_widget.set_zoom(15)


    marker = map_widget.set_marker(address[0],address[1])

    def on_string_var_update(*args):    
        try:
            x = float(coords.get().split(",")[0].split("(")[1])
            y = float(coords.get().split(",")[1].split(")")[0])
            marker.set_position(x,y)
            map_widget.set_position(x,y)
            map_widget.set_zoom(15)
        except Exception as e:
            print(e)
    
    coords.trace_add("write", on_string_var_update)

    def left_click_event(coordinates_tuple):
        marker.set_position(coordinates_tuple[0],coordinates_tuple[1])
        coords.set(str(coordinates_tuple))
        print("Left click event with coordinates:", coordinates_tuple)
    
    map_widget.add_left_click_map_command(left_click_event)

def areaMapPopup():
    win = tk.Toplevel(root)
    win.title("Choose Location")

    coords = tk.StringVar()

    textBox = ttk.Entry(win,width=50, textvariable=coords)
    textBox.grid(column=0,row=0)

    map_widget = tkintermapview.TkinterMapView(win, width=800, height=600, corner_radius=50)
    map_widget.grid(column=0,row=1)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
    address = tkintermapview.convert_address_to_coordinates("Williamsburg")
    map_widget.set_position(address[0],address[1])
    map_widget.set_zoom(15)

    markerList = list()
    polygon = map_widget.set_polygon([(0,0),(0,0),(0,0),(0,0)])

    def left_click_event(coordinates_tuple):
        newMarker = map_widget.set_marker(coordinates_tuple[0],coordinates_tuple[1])
        if len(markerList) < 4:
            markerList.append(newMarker)
            newMarker
        else:
            markerList.pop(0).delete()
            markerList.append(newMarker)
        
        if len(markerList) == 4:
            if polygon != None:
                polygon.delete()
            polygon = map_widget.set_polygon([marker.position for marker in markerList],
                                   # fill_color=None,
                                   # outline_color="red",
                                   # border_width=12,
                                   #command=polygon_click,
                                   name="user_area")
        
    map_widget.add_left_click_map_command(left_click_event)

label = ttk.Label(root, text="Coordnates: ")
label.grid(column=0,row=0)

button = ttk.Button(root,text="Choose Location",command=mapPopup)
button.grid(column=0,row=1)
button = ttk.Button(root,text="Choose Location Area",command=areaMapPopup)
button.grid(column=0,row=2)

tk.mainloop()
