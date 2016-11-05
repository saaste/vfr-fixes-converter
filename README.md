# vfr-fixes-converter
A simple python script to convert Finnish VFR reporting points file to earth_fix.dat and waypoints.txt supported by **X-Plane 10**.
Check the URL of the latest VFR reporting points file from [Finavia Downloads](https://ais.fi/C-en/services_en/downloads)

## How to use

```
$ python generate.py <URL_OF_THE_VFR_FIX_FILE>
````

Example
```
$ python generate.py https://ais.fi/files/finavia2/gpx-tiedosto/EF_VFRREP_15SEP2016.gpx
```

## Documentation

The script generates two files: `earth_fix.dat` and `waypoints.txt`. You can add the contents to the **end** of files with
similar names in X-Plane 10 `Custom Data` directory:
```
<X-Plane Install Path>\Custom Data\earth_fix.dat
<X-Plane Install Path>\Custom Data\GNS430\navdata\Waypoints.txt
```

If you don't have the files, you can copy the originals from the following directories:
```
<X-Plane Install Path>\Resources\default data\earth_fix.dat
<X-Plane Install Path>\Resources\GNS430\navdata\Waypoints.txt
```

**DO NOT** edit the original files since you will loose your changes after X-Plane update. Always use `Custom Data` directory.

If you want up-to-date list of all fixes (excluding VFR reporting points), you can download X-Plane
compatible files from [Navigraph](https://www.navigraph.com) (not free). Just remember to add
VFR reporting points to these files.s

