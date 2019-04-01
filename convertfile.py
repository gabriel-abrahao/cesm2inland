import os
# import Nio
import xarray as xr
import matplotlib.pyplot as plt

def main():
    inpfname = "input/rcp8.5_weg_008.cam2.h1.2050-01-01-00000.nc"
    outfname = "output/prec_rcp8.5_weg_008.cam2.h1.2050-01-01-00000.nc"

    inpvarname = "PRECT"
    outvarname = "prec"

    finp = xr.open_dataset(inpfname, decode_times=False)

    finp.to_netcdf(outfname, mode = "w", format = "NETCDF3_64BIT")
    finp[inpvarname].to_netcdf(outfname, mode = "w", format = "NETCDF3_64BIT")




    # arq = Nio.open_file(infname)
    #
    # arqout = Nio.open_file("poi.nc","c")
    # var = arq.variables[invarname]
    # arqout.variables['lala'][:] = var
    #
    # arq.close()
    # arqout.close()
    #
    # print(var[:,-90:0,:])

    # dir(nio)

if __name__ == "__main__":
    main()
