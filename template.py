import os
from pathlib import Path
import logging

project_name = "portfolio"

list_of_files = [
    f"css/bootstrap/bootstrap-grid.css",
    f"css/bootstrap/bootstrap-reboot.css",
    f"css/css/mixins/_text-hide.css",
    f"css/css/bootstrap-reboot.css",
    f"css/animate.css",
    f"css/aos.css",
    f"css/bootstrap.min.css",
    f"css/flaticon.css",
    f"css/icomoon.css",
    f"css/ionicons.min.css",
    f"css/magnific-popup.css",
    f"css/open-iconic-bootstrap.min.css",
    f"css/owl.carousel.min.css",
    f"css/owl.theme.default.min.css",
    f"css/style.css",
    f"fonts/a.py",
    f"images/a.py",
    f"js/a.py",
    "index.html",
    f"documents/a.py"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

