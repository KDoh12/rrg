# Python Script developed by KDoh12
#GEO 409 Fall 2018 Semester
# University of Kentucky
# This script creates hillshades using while loops
# Python 3.6 and ArcGIS Pro 2.2

# Import site package for ArcGIS
import arcpy

# This defines the geodatabase
geodatabase = input("Full pathname to geodatabase: ") + "\\"

# This sets the workspace and shows the raster files in the database
try:
    arcpy.env.workspace = geodatabase
    rasterList = arcpy.ListRasters()
    print ("Raster: ", rasterList)
except:
    print("Not a valid database")
arcpy.env.overwriteOutput = True

# This asks the user to choose what layer they want to use to create the hillshade
in_raster = input("Please choose what Raster Layer you want to use: ")

# This defines the variables that will be used to create the hillshade
out_dir = geodatabase
i = 90
azimuth = 90
altitude = 55

# This creates a while loop that will create the 3 hillshades
# The loop will run as long as azimuth is less that 271
while azimuth < 271:
    # This determines what the hillshade output will be called
    out_raster = "hillshade" + str(i)
    print("Creating hillshade from " + in_raster + " ...")
    # This runs the arcpy hillshade function
    arcpy.HillShade_3d(in_raster, out_raster, azimuth, altitude, "SHADOWS", 1)
    # This adds 90 to the variabke azimuth
    azimuth += 90
    # This adds 90 to the variable i
    i += 90