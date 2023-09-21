# MapPointPlot
Python Map Plotter: A Python program that allows you to input latitude and longitude coordinates and plot multiple points on a map. Visualize geographic data with ease!



## Installation

Before running the application, make sure you have the required Python packages installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```
## Usage
Run the application by executing the main.py script.
You will see a window with latitude and longitude input fields.
Enter the latitude and longitude of the point you want to plot.
Click the "Plot" button to display the point on the map.
You can also change the country displayed on the map by modifying the code in main.py. By default, it displays a map of Pakistan. To change the country, locate the following line in the code:
```
axis = world_data[world_data.name == "Pakistan"].plot(ax=ax, color="lightblue", edgecolor="black")
```
Replace "Pakistan" with the name of the country you want to display.

![image](https://github.com/saithsays/MapPointPlot/assets/113043793/22e24bb3-3d0a-4025-9126-923bc6e10a75)  ![image](https://github.com/saithsays/MapPointPlot/assets/113043793/567a5675-c876-46da-8cd2-d85b3a7014d2)

## Example
Here's an example of how to use the application:

Run the application.
Enter latitude: 82.986944.52.5200 , longitude: 13.4050  .
Click the "Plot" button.
A red point will be displayed on the map at the specified coordinates.

![image](https://github.com/saithsays/MapPointPlot/assets/113043793/cbe8158b-d779-4811-b319-460423e83cbd)

Feel free to fork and modify this project to suit your needs!

This `README.md` file provides an overview of your project, installation instructions, basic usage guidelines, an example, and mentions the open-source license. You can further customize it to include additional information as needed.
