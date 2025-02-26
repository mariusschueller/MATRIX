# Using Superslicer’s CLI Tool
Working G-code example with Superslicer:  
Run this command in the terminal:
```
./superslicer -g /home/marius/Downloads/TRUMPETSTENCIL.stl
```

Note: There are a lot of paramaters that can be added to the command

see here: https://subscription.packtpub.com/book/business-and-other/9781783284979/1/ch01lvl1sec14/running-slic3r-from-the-command-line-become-an-expert

https://manual.slic3r.org/advanced/command-line


## Flask API

Created api.py that can run in the background that uses a subprocess to call call superslicer's command line tool


ex:
1. run api.py
2. go to http://127.0.0.1:5000

The api will source from an example file TRUMPETSTENCIL.stl in test_files

The api will then call superslicer and download the gcode into the same file

ex 2:
1. run api.py
2. go to http://127.0.0.1:5000/file/TRUMPETSTENCIL.stl


### For Custom Prints
The way this API works:
```
[API_Address}/fileOptions/[File_Name]/[Parameters]
```

### Parameters
Put in the desired parameter and instead of spaces put %20
Add in as many parameters as you'd like

Ex with scale at 0.5 and layer-height at 0.2:
```
http://127.0.0.1:5000/fileOptions/TRUMPETSTENCIL.stl/--scale%200.5%20--layer-height%200.2
```

### All Parameters Below

| Filament options                        | Description                                                                                      | Default Value |
|--------------------------------|------------------------------------------------------------------------------------------------|--------------|
| `--filament-diameter`         | Diameter in mm of your raw filament                                                            | 3            |
| `--extrusion-multiplier`      | Alters the amount of plastic extruded; mainly for compensating filament packing               | 1            |
| `--temperature`               | Extrusion temperature in °C; set to 0 to disable                                              | 200          |
| `--first-layer-temperature`   | Extrusion temperature for the first layer in °C; set to 0 to disable                          | Same as `--temperature` |
| `--bed-temperature`           | Heated bed temperature in °C; set to 0 to disable                                             | 0            |
| `--first-layer-bed-temperature` | Heated bed temperature for the first layer in °C; set to 0 to disable                        | Same as `--bed-temperature` |



| Speed options                        | Description                                                                                 | Default Value |
|--------------------------------|---------------------------------------------------------------------------------------------|--------------|
| `--travel-speed`              | Speed of non-print moves in mm/s                                                             | 130          |
| `--perimeter-speed`           | Speed of print moves for perimeters in mm/s                                                 | 30           |
| `--small-perimeter-speed`     | Speed of print moves for small perimeters in mm/s or % over perimeter speed                 | 30           |
| `--external-perimeter-speed`  | Speed of print moves for the external perimeter in mm/s or % over perimeter speed           | 70           |
| `--infill-speed`              | Speed of print moves in mm/s                                                                 | 60           |
| `--solid-infill-speed`        | Speed of print moves for solid surfaces in mm/s or % over infill speed                      | 60           |
| `--top-solid-infill-speed`    | Speed of print moves for top surfaces in mm/s or % over solid infill speed                  | 50           |
| `--support-material-speed`    | Speed of support material print moves in mm/s                                               | 60           |
| `--bridge-speed`              | Speed of bridge print moves in mm/s                                                          | 60           |
| `--gap-fill-speed`            | Speed of gap fill print moves in mm/s                                                        | 20           |
| `--first-layer-speed`         | Speed of print moves for bottom layer (absolute value or % over normal speeds)              | 30%          |


| Acceleration options                      | Description                                                                 | Default Value |
|-----------------------------|-----------------------------------------------------------------------------|--------------|
| `--perimeter-acceleration`  | Overrides firmware's default acceleration for perimeters (mm/s², set 0 to disable) | 0            |
| `--infill-acceleration`     | Overrides firmware's default acceleration for infill (mm/s², set 0 to disable)     | 0            |
| `--default-acceleration`    | Acceleration will be reset to this value after specific settings are applied (mm/s², set 0 to disable) | 130          |



| Accuracy options                        | Description                                         | Default Value |
|--------------------------------|-----------------------------------------------------|--------------|
| `--layer-height`              | Layer height in mm                                  | 0.4          |
| `--first-layer-height`        | Layer height for the first layer (mm or %)         | 0.35         |
| `--infill-every-layers`       | Infill every N layers                              | 1            |
| `--solid-infill-every-layers` | Force a solid layer every N layers                 | 0            |



| Print options                                      | Description                                                                                     | Default Value  |
|---------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|
| `--perimeters`                              | Number of perimeters/horizontal skins (range: 0+)                                              | 3             |
| `--top-solid-layers`                        | Number of solid layers for top surfaces (range: 0+)                                            | 3             |
| `--bottom-solid-layers`                     | Number of solid layers for bottom surfaces (range: 0+)                                         | 3             |
| `--solid-layers`                            | Shortcut for setting `--top-solid-layers` and `--bottom-solid-layers`                          | -             |
| `--fill-density`                            | Infill density (range: 0-1)                                                                    | 0.4           |
| `--fill-angle`                              | Infill angle in degrees (range: 0-90)                                                          | 45            |
| `--fill-pattern`                            | Pattern used to fill non-solid layers                                                          | honeycomb     |
| `--solid-fill-pattern`                      | Pattern used to fill solid layers                                                              | rectilinear   |
| `--start-gcode`                             | Load initial G-code from the supplied file (overwrites default G28 home command)              | -             |
| `--end-gcode`                               | Load final G-code from the supplied file (overwrites default M104 S0, G28 X, M84 commands)    | -             |
| `--layer-gcode`                             | Load layer-change G-code from the supplied file                                                | nothing       |
| `--toolchange-gcode`                        | Load tool-change G-code from the supplied file                                                 | nothing       |
| `--extra-perimeters`                        | Add more perimeters when needed                                                                | yes           |
| `--randomize-start`                         | Randomize the starting point across layers                                                     | yes           |
| `--only-retract-when-crossing-perimeters`   | Disable retraction when traveling between infill paths inside the same island                 | no            |
| `--solid-infill-below-area`                 | Force solid infill when a region has a smaller area than the threshold (mm²)                  | 70            |



| Support material options                          | Description                                                         | Default Value  |
|---------------------------------|---------------------------------------------------------------------|---------------|
| `--support-material`            | Generate support material for overhangs                            | -             |
| `--support-material-threshold`  | Overhang threshold angle (range: 0-90, set 0 for automatic)        | 0             |
| `--support-material-pattern`    | Pattern to use for support material                               | rectilinear   |
| `--support-material-spacing`    | Spacing between pattern lines (mm)                                | 2.5           |
| `--support-material-angle`      | Support material angle in degrees (range: 0-90)                   | 0             |



| Retraction options                      | Description                                                         | Default Value |
|-----------------------------|---------------------------------------------------------------------|--------------|
| `--retract-length`         | Length of retraction in mm when pausing extrusion                 | 1            |
| `--retract-speed`          | Speed for retraction in mm/s                                      | 30           |
| `--retract-restart-extra`  | Additional filament in mm to push after compensating retraction   | 0            |
| `--retract-before-travel`  | Only retract before travel moves of this length in mm            | 2            |
| `--retract-lift`           | Lift Z by the given distance in mm when retracting               | 0            |



| Cooling options                        | Description                                                       | Default Value |
|-------------------------------|-------------------------------------------------------------------|--------------|
| `--cooling`                    | Enable fan and cooling control                                    | -            |
| `--min-fan-speed`              | Minimum fan speed                                                 | 35%          |
| `--max-fan-speed`              | Maximum fan speed                                                 | 100%         |
| `--bridge-fan-speed`           | Fan speed to use when bridging                                    | 100%         |
| `--fan-below-layer-time`       | Enable fan if layer print time is below this number of seconds   | 60           |
| `--slowdown-below-layer-time`  | Slow down if layer print time is below this number of seconds    | 30           |
| `--min-print-speed`            | Minimum print speed in mm/s                                       | 10           |
| `--disable-fan-first-layers`   | Disable fan for the first N layers                               | 1            |
| `--fan-always-on`              | Keep fan always on at min speed, even for layers that don't need cooling | -         |



| Skirt options                        | Description                                                            | Default Value |
|-------------------------------|------------------------------------------------------------------------|--------------|
| `--skirts`                     | Number of skirts to draw (0+)                                          | 1            |
| `--skirt-distance`             | Distance in mm between the innermost skirt and the object              | 6            |
| `--skirt-height`               | Height of skirts to draw (expressed in layers, 0+)                    | 1            |
| `--min-skirt-length`           | Generate no less than the number of loops required to consume this length of filament on the first layer, for each extruder (mm, 0+) | 0            |
| `--brim-width`                 | Width of the brim added to each object to help adhesion (mm)          | 0            |


| Transform options                     | Description                                                          | Default Value |
|----------------------------|----------------------------------------------------------------------|--------------|
| `--scale`                   | Factor for scaling input object                                      | 1            |
| `--rotate`                  | Rotation angle in degrees (0-360)                                    | 0            |
| `--duplicate`               | Number of items with auto-arrange (1+)                                | 1            |
| `--bed-size`                | Bed size, only used for auto-arrange (mm)                            | 200,200      |
| `--duplicate-grid`          | Number of items with grid arrangement                                | 1,1          |
| `--duplicate-distance`      | Distance in mm between copies                                        | 6            |



| Flow options                              | Description                                                              | Default Value |
|-------------------------------------|--------------------------------------------------------------------------|--------------|
| `--extrusion-width`                 | Set the extrusion width manually (absolute value in mm or percentage over layer height) | -            |
| `--first-layer-extrusion-width`     | Set a different extrusion width for the first layer                      | -            |
| `--perimeter-extrusion-width`      | Set a different extrusion width for perimeters                           | -            |
| `--infill-extrusion-width`         | Set a different extrusion width for infill                               | -            |
| `--support-material-extrusion-width`| Set a different extrusion width for support material                    | -            |
| `--bridge-flow-ratio`              | Multiplier for extrusion when bridging (> 0)                             | 1            |



| Speed options                        | Description                                                                                 | Default Value |
|--------------------------------|---------------------------------------------------------------------------------------------|--------------|
| `--travel-speed`              | Speed of non-print moves in mm/s                                                             | 130          |
| `--perimeter-speed`           | Speed of print moves for perimeters in mm/s                                                 | 30           |
| `--small-perimeter-speed`     | Speed of print moves for small perimeters in mm/s or % over perimeter speed                 | 30           |
| `--external-perimeter-speed`  | Speed of print moves for the external perimeter in mm/s or % over perimeter speed           | 70           |
| `--infill-speed`              | Speed of print moves in mm/s                                                                 | 60           |
| `--solid-infill-speed`        | Speed of print moves for solid surfaces in mm/s or % over infill speed                      | 60           |
| `--top-solid-infill-speed`    | Speed of print moves for top surfaces in mm/s or % over solid infill speed                  | 50           |
| `--support-material-speed`    | Speed of support material print moves in mm/s                                               | 60           |
| `--bridge-speed`              | Speed of bridge print moves in mm/s                                                          | 60           |
| `--gap-fill-speed`            | Speed of gap fill print moves in mm/s                                                        | 20           |
| `--first-layer-speed`         | Speed of print moves for bottom layer (absolute value or % over normal speeds)              | 30%          |



| Acceleration options                      | Description                                                                 | Default Value |
|-----------------------------|-----------------------------------------------------------------------------|--------------|
| `--perimeter-acceleration`  | Overrides firmware's default acceleration for perimeters (mm/s², set 0 to disable) | 0            |
| `--infill-acceleration`     | Overrides firmware's default acceleration for infill (mm/s², set 0 to disable)     | 0            |
| `--default-acceleration`    | Acceleration will be reset to this value after specific settings are applied (mm/s², set 0 to disable) | 130          |



| Accuracy options                        | Description                                         | Default Value |
|--------------------------------|-----------------------------------------------------|--------------|
| `--layer-height`              | Layer height in mm                                  | 0.4          |
| `--first-layer-height`        | Layer height for the first layer (mm or %)         | 0.35         |
| `--infill-every-layers`       | Infill every N layers                              | 1            |
| `--solid-infill-every-layers` | Force a solid layer every N layers                 | 0            |



| Multiple extruder options                          | Description                                                                   | Default Value |
|---------------------------------|-------------------------------------------------------------------------------|--------------|
| `--extruder-offset`             | Offset of each extruder if firmware doesn't handle displacement (multiple allowed) | 0x0          |
| `--perimeter-extruder`          | Extruder to use for perimeters (1+)                                          | 1            |
| `--infill-extruder`             | Extruder to use for infill (1+)                                              | 1            |
| `--support-material-extruder`   | Extruder to use for support material (1+)                                    | 1            |






### Getting Dimensions
Now we can use a new call.
http://localhost:5000/size/TRUMPETSTENCIL.stl

We could then add scaling based on what occured
scale by 0.5
```
http://127.0.0.1:5000/fileOptions/TRUMPETSTENCIL.stl/--scale%200.5
```

Note: we should use the tweaked file from then on after getting the size

```
<iframe src="http://localhost:8000" width="100%" height="600px"></iframe>
```

https://github.com/tonyb486/stlviewer?tab=readme-ov-file

### Future work
- Add error handling
- Testing with more parameters
- Does it work with df configuration or do we need to set them ourselves? 

<br>

# Add Orientation
Using Tweaker Library which can be found here:
https://github.com/ChristophSchranz/Tweaker-3


```
python Tweaker.py -i demo_object.stl -vb
```


