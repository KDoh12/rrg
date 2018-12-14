
# coding: utf-8

# Python Script developed by KDoh12
#GEO 409 Fall 2018 Semester
# University of Kentucky
# This script selects arches by elevation and state and creates a CSV file of that selection.
# Python 3.6 and ArcGIS Pro 2.2

#This imports the package for ArcGIS Pro
import arcpy

# This tells arcpy where our workspace is
arcpy.env.workspace = r"C:\DohnerGIS\DATA\geology.gdb"
arcpy.env.overwriteOutput = True

# This assigns variables that will be used in the creation of the .csv file
# input layer is the target layer you want the features to be selected from
# output path is where you want the .csv file to be saved to when completed
input_layer = "us_arches"
output_path = r"C:\DohnerGIS\DATA"

# This prompts the user for input for the desired elevation and the desired state
print("This program returns all arches as .csv file at or above the minimum elevation.")
elevation = input("Enter minimum elevation: ")
stateinput = input("Enter the desired State abbreviation in all caps: ")

# This adds apostrophes around the abbreviation so that the SQL statement will execute properly in ArcGIS
state = ("'" + stateinput + "'")

# Try converting to integer. Exit if not integer
# This prevents someone from inputing something other than a number
try:
    elevationNumber = int(elevation)
except:
    print("Whoops! Try using a number.")
    exit()

# This builds the SQL statement that selects the features
whereClause = "base_elevation_ft >= " + str(elevationNumber) + "AND state_alpha = " + state

# This prompts the user for input on what they want the .csv file to be named
saved_file = input("Enter the file name for your finished .csv: ")

# Use the TableToTable arcpy function extract by SQL query
# This extracts the features that is selected by the SQL statement and inputs them into a .csv file
arcpy.TableToTable_conversion (input_layer, output_path, saved_file + ".csv", whereClause)

