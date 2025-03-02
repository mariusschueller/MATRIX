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
http://127.0.0.1:5000/fileOptions/TRUMPETSTENCIL.stl/--scale%200.5%20--layer-height%200.2

### All Parameters in configurations.md

## Auto Configurations
In the configurations folder
Using [material]_config.ini

Exported using DFL .ini file in Superslicer

### Calling

Base print (baseMaterialPrint function):

http://127.0.0.1:5000/materialPrint/pla/TRUMPETSTENCIL.stl

Overriding Settings (materialPrint function):
http://127.0.0.1:5000/materialPrint/pla/TRUMPETSTENCIL.stl/--scale%200.5%20--layer-height%200.2



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

# Add Orientation
The Tweaker library is used in this api to orient parts.

Using Tweaker Library which can be found here:
https://github.com/ChristophSchranz/Tweaker-3

Example usage:
```
python Tweaker.py -i demo_object.stl -vb
```


