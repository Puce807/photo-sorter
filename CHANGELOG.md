
# 📸 Photo Sorter Changelog

All commits will be recorded here. 

## [1.0.0] Initial Commit

- Created `main.py`, `CHANGELOG.md`, `README.md` and `requirements.txt`

---

## [1.0.1] `file_browser` and `read_source` functions in utils.py
``
- Added `file_browser` and `read_source` functions to utils.py

---
``
## [1.0.2] `metadata.py` functions including EXIF extraction

- Added functions which return EXIF data from a photo
- Added dms to decimal conversion to `utils.py`

## [1.0.3] gps to region function

- Added loading function
- Added gps to region function
- Converted slow and old `.shp` file to quicker `.gpkg` file
- Added `LAD_shaoefile.gpkg` to `.gitignore` due to be github's 100mb per file limit