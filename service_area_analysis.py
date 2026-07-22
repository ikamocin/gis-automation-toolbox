##  Facilities: Fire stations
##  Break values: 5, 10, 15 minutes
##  Network source: Local Network Dataset
##  Output: outputs/service_area_results.gdb
##  Polygon type: Rings
##  Facility overlap: No overlap
import sys
import arcpy


print("Python executable:", sys.executable)
print("ArcPy location:", arcpy.__file__)
print("ArcGIS Pro version:", arcpy.GetInstallInfo()["Version"])
print("License:", arcpy.ProductInfo())
print("Network Analyst:", arcpy.CheckExtension("network"))

network_dataset = "Dataset Path"
facilities = "String Data"
break_values = [5,10,15]
travel_mode = "Driving Time"
output_gdb = "Output GeoDatabase"
output_name = "Feature Class Name"

