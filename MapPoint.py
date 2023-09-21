import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Create a GeoDataFrame with a single point
def create_point_df(lat, lon):
    geometry = [Point(lon, lat)]
    return gpd.GeoDataFrame(geometry=geometry, crs="EPSG:4326")

# Create the function to plot the map
def create_map():
    world_data = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    axis = world_data[world_data.name == "Pakistan"].plot(ax=ax, color="lightblue", edgecolor="black")
    ax.set_title("Map of Pakistan")
    return fig, ax

# Function to handle the "Plot" button click
def plot_button_click():
    lat_str = entry1.get()
    lon_str = entry2.get()
    if lat_str and lon_str:
        lat = float(lat_str)
        lon = float(lon_str)
        df_geo = create_point_df(lat, lon)
        df_geo.plot(ax=ax, color="red", markersize=100)  # Show the point in red
        canvas.draw()

# Create the main application window
root = tk.Tk()
root.title("Map Display")

# Create two input bars
input_frame = tk.Frame(root)
input_frame.pack(side="top", pady=10)
label1 = tk.Label(input_frame, text="Latitude:")
label1.pack(side="left")
entry1 = tk.Entry(input_frame)
entry1.pack(side="left", padx=10)
label2 = tk.Label(input_frame, text="Longitude:")
label2.pack(side="left")
entry2 = tk.Entry(input_frame)
entry2.pack(side="left")

# Create a button to trigger the map plot
plot_button = tk.Button(root, text="Plot", command=plot_button_click)
plot_button.pack()

# Create the initial map
fig, ax = create_map()

# Embed the Matplotlib plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Start the GUI main loop
root.mainloop()
