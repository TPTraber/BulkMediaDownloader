import tkinter
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
address = tkintermapview.convert_address_to_coordinates("Williamsburg")
map_widget.set_position(address[0],address[1])
map_widget.set_zoom(15)


marker = map_widget.set_marker(address[0],address[1])

def left_click_event(coordinates_tuple):
    marker.set_position(coordinates_tuple[0],coordinates_tuple[1])
    print("Left click event with coordinates:", coordinates_tuple)
    
map_widget.add_left_click_map_command(left_click_event)

root_tk.mainloop()