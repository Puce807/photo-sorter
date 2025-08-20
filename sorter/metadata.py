import datetime
import piexif
from PIL import Image

from utils import dms_to_decimal

GPS_TAGS = {
    1: "GPSLatitudeRef",
    2: "GPSLatitude",
    3: "GPSLongitudeRef",
    4: "GPSLongitude",
    5: "GPSAltitudeRef",
    6: "GPSAltitude",
    7: "GPSTimeStamp",
    17: "GPSDateStamp"
}


def get_EXIF(path):
    img = Image.open(path)
    exif_dict = piexif.load(img.info['exif'])

    # Basic info
    result = {
        "filename": img.filename,
        "datetime": exif_dict["0th"].get(piexif.ImageIFD.DateTime, b"").decode(),
        "camera_make": exif_dict["0th"].get(piexif.ImageIFD.Make, b"").decode(),
        "camera_model": exif_dict["0th"].get(piexif.ImageIFD.Model, b"").decode(),
        "gps": None
    }

    gps_ifd = exif_dict.get("GPS", {})
    if gps_ifd:
        gps_data = {}
        for tag in gps_ifd:
            tag_name = GPS_TAGS.get(tag, str(tag))
            gps_data[tag_name] = gps_ifd[tag]
        result["gps"] = gps_data

        # Convert to decimal if possible
        if "GPSLatitude" in gps_data and "GPSLongitude" in gps_data:
            lat_ref = gps_data.get("GPSLatitudeRef", "N").decode() if isinstance(gps_data.get("GPSLatitudeRef"),
                                                                                 bytes) else gps_data.get(
                "GPSLatitudeRef", "N")
            lon_ref = gps_data.get("GPSLongitudeRef", "E").decode() if isinstance(gps_data.get("GPSLongitudeRef"),
                                                                                  bytes) else gps_data.get(
                "GPSLongitudeRef", "E")
            result["latitude"] = dms_to_decimal(gps_data["GPSLatitude"], lat_ref)
            result["longitude"] = dms_to_decimal(gps_data["GPSLongitude"], lon_ref)

    return result



