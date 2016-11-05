# VFR-ilmoittautumispaikat
# https://ais.fi/C/palvelut/Ladattavat_tuotteet

import sys
import requests
import xml.etree.ElementTree as ET


MAP_FILENAME = "earth_fix.dat"
GPS_FILENAME = "waypoints.txt"


def main(xml_url):
    waypoints = parse_waypoints(xml_url)
    generate_map_data(waypoints)
    generate_gps_data(waypoints)


def parse_waypoints(xml_url):
    response = requests.get(xml_url)

    if response.status_code <> 200:
        print "Invalid URL {0}".format(xml_url)
        print "Check the correct url from https://ais.fi/C/palvelut/Ladattavat_tuotteet"
        exit(1)

    root = ET.fromstring(response.content)

    namespaces = {"gpx": "http://www.topografix.com/GPX/1/1"}
    waypoints = []

    for wpt in root.findall("gpx:wpt", namespaces):
        waypoints.append({
            "lat": wpt.attrib["lat"],
            "lon": wpt.attrib["lon"],
            "name": wpt.find("gpx:name", namespaces).text
        })

    return waypoints


def generate_map_data(waypoints):
    with open(MAP_FILENAME, "w") as file_handle:
        for wpt in waypoints:
            lat = format(float(wpt["lat"]), ".8f")
            lon = format(float(wpt["lon"]), ".8f").zfill(12)
            file_handle.write(" {0}  {1} {2}\n".format(lat, lon, wpt["name"]))


def generate_gps_data(waypoints):
    with open(GPS_FILENAME, "w") as file_handle:
        for wpt in waypoints:
            lat = format(float(wpt["lat"]), ".6f")
            lon = format(float(wpt["lon"]), ".6f")
            file_handle.write("{2},{0},{1},EF\n".format(lat, lon, wpt["name"]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: python generate.py <URL_OF_THE_XML>"
        exit(1)

    main(sys.argv[1])
