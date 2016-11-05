# vfr-fixes-converter
A simple python script to convert Finnish VFR reporting points file to earth_fix.dat and waypoints.txt supported by **X-Plane 10**.
Check the URL of the latest VFR reporting points file from [Finavia Downloads](https://ais.fi/C-en/services_en/downloads)

## How to use

```
usage: python generate.py <URL_OF_THE_FILE>
````

That will generate two files: earth_fix.dat and waypoints.txt. You can the copy-paste the contents to the end of files in X-Plane 10 `Custom Data` directory:
```
<X-Plane Install Path>\Custom Data\earth_fix.dat
<X-Plane Install Path>\Custom Data\GNS430\navdata\Waypoints.txt
```

If you don't have the files, you can copy the originals from the following directories:
```
<X-Plane Install Path>\Resources\default data\earth_fix.dat
<X-Plane Install Path>\Resources\GNS430\navdata\Waypoints.txt
```

**DO NOT** overwrite the original files since you will loose your changes after X-Plane update. Always use Custom Data directory.




