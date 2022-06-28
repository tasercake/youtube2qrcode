
# youtube2qrcode

Generate Pretty, Printable QR Codes From YouTube URLs.

**I threw this together to quickly generate QR codes for a bunch of music videos** - this may not work for your use case out of the box, but it's simple enough to change as you wish

QR code generation requires the following as input:

- YouTube URL (or any other URL)
- Artist's name (video creator's name)
- Song name (video title)

# Usage

1. Clone this repo
2. Modify `songs.csv` to include any information you want
  - Generated QR codes will include the artist name & song title in the format `{artist} - {title}` and the video's URL
3. Run this command:

    ```shell
    python generate.py
    ```

# Examples

|[![TheFatRat - Unity](output/TheFatRat%20-%20Unity.png)](https://www.youtube.com/watch?v=n8X9_MgEdCg)| [![Caravan Palace - Lone Digger](output/Caravan%20Palace%20-%20Lone%20Digger.png)](https://www.youtube.com/watch?v=UbQgXeY_zi4) |
|--|--|
|[![Avicii - Addicted to You](output/Avicii%20-%20Addicted%20to%20You.png)](https://www.youtube.com/watch?v=Qc9c12q3mrc)|[![Daft Punk ft. Julian Casablancas - Instant Crush](output/Daft%20Punk%20ft.%20Julian%20Casablancas%20-%20Instant%20Crush.png)](https://www.youtube.com/watch?v=a5uQMwRMHcs)|
