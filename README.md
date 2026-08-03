# Photo intelligence

A tool for triaging and understanding photo shoots — built to solve a real problem
(sorting through hundreds of shots from church and freelance bookings) while going
deep on computer vision and applied ML.

## Status

Phase 1 in progress: metadata extraction and basic shoot stats.

## Setup

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Also requires [exiftool](https://exiftool.org) available on PATH.

## Usage

Extract metadata from a shoot folder:

```
python extract_metadata.py "C:\path\to\shoot\folder" --output photo_dataset.csv
```

View the stats dashboard:

```
streamlit run dashboard.py
```

## Roadmap

- [x] Phase 1 — metadata extraction and basic stats
- [ ] Phase 2 — computer vision: sharpness detection, duplicate clustering, face detection
- [ ] Phase 3 — train a "keeper" classifier on rated photos
- [ ] Phase 4 — polished dashboard and shoot summaries
