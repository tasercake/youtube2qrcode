import qrcode
import numpy as np
import pandas as pd
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

IMAGE_WIDTH = 1000
MARGIN = 0.15

URL_FONT = ImageFont.truetype('FiraSans-Light.otf', 20)
SONG_FONT = ImageFont.truetype('FiraSans-LightItalic.otf', 32)
SONGS = pd.read_csv('songs.csv')


def make_image(row):
    url = row['url']
    artist = row['artist']
    title = row['title']
    margin_height = int(MARGIN * IMAGE_WIDTH)
    song_string = f"{artist} - {title}"

    # Create Image
    image = np.full((IMAGE_WIDTH + margin_height, IMAGE_WIDTH, 3), 255, dtype=np.uint8)
    code = np.array(qrcode.make(url).resize((IMAGE_WIDTH, IMAGE_WIDTH)))[..., None].astype(np.uint8) * 255
    image[:IMAGE_WIDTH, :IMAGE_WIDTH] = code
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)

    # Write Artist and Title
    song_size = draw.textsize(song_string, font=SONG_FONT)
    song_x = (IMAGE_WIDTH - song_size[0]) // 2
    song_y = IMAGE_WIDTH
    draw.text((song_x, song_y), song_string, fill=0, font=SONG_FONT)

    # Write YouTube URL
    url_size = draw.textsize(url, font=URL_FONT)
    url_x = (IMAGE_WIDTH - url_size[0]) // 2
    url_y = song_y + 20 + song_size[1]
    draw.text((url_x, url_y), url, fill=0, font=URL_FONT)

    # Draw rectangle border around image
    draw.rectangle([(0, 0), (image.width - 1, image.height - 1)], outline=0)

    # Save image
    path = Path(f"output/{song_string}.png")
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)

    return image


if __name__ == '__main__':
    SONGS['images'] = SONGS.apply(make_image, axis=1)
