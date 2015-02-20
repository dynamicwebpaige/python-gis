#! /usr/bin/python

'''Note: Intended to be run as either a script from within the 
Python terminal in ArcGIS 10.1+, or line by line.'''

import arcpy
from arcpy import env

# either / or of the above statements
# have noticed significant time delays for both

# Set the path to directory where the raster is located. 
# mgisdata/Austin is located within the GIS_Python repo.
env.workspace = "C:/Users/ASUS/Desktop/GIS_Python/mgisdata/Austin"

# Create the polygons
# .png file is raster; then the output file; "NO_SIMPLIFY" gives better results than alternative
arcpy.RasterToPolygon_conversion("edwardsoverview.png","C:/Users/ASUS/Desktop/Edwards_polygons","NO_SIMPLIFY","VALUE")


# More info on raster-to-polygon, raster-to-polyline, and raster-to-point conversions 
# can be found on Esri's website: http://resources.arcgis.com/en/help/main/10.1/index.html#/Raster_to_Polygon/001200000008000000/

