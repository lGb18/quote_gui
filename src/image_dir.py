from pathlib import Path
BASE_DIR = Path(__file__).parent.parent
IMAGES_DIR = BASE_DIR / 'data' / 'images'


def get_image(file_name):
    return IMAGES_DIR / file_name

