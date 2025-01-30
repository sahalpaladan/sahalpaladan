# Load the libraries
library(sf)
library(raster)
library(exactextractr)
library(dplyr)
# Read the shapefile containing state geometries
state_shapefile <- st_read("path_to_shapefile.shp")

# Read the maxt raster file
maxt_raster <- raster("path_to_maxt_raster.tif")
# Perform exact extraction of the maxt values for each state geometry
state_avg_maxt <- exact_extract(maxt_raster, state_shapefile, 'mean')

# Combine the results with state names
result <- state_shapefile %>%
  mutate(avg_maxt = state_avg_maxt) %>%
  select(state_name_column, avg_maxt) %>%
  st_drop_geometry()
# Write the results to a CSV file
write.csv(result, "state_avg_maxt.csv", row.names = FALSE)
