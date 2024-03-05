# importing NetCDF data
import xarray as xr

# path to files 
files_path = 'c:/Users/Gunther/Copernicus/GenCli/AirTemperature/*.nc'

#load & combine dataset
ds = xr.open_mfdataset(files_path, combine='by_coords')

# save concatenated dataset
ds.to_netcdf('c:/Users/Gunther/Copernicus/GenCli/AirTemperature/combinedAT.nc')

# print dataset to understand its structure
print(ds)

#plotting a single time slice
ds['tas'].isel(time=0).plot()