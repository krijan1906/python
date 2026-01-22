from cv2pencil import get_pencil_drawing

# Allowed image formats: url/path/buffer/base64/PIL/np

# save_diff / save_norm are optional

a, b = get_pencil_drawing(

    r"https://imgs.search.brave.com/mT14LiHutpQX2cSzrA3tcN-bQIdRnPcS00yy3j4O-HU/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wNTMv/MTkzLzU4OS9zbWFs/bC9hLXdvbWFuLXRh/a2luZy1hLXBpY3R1/cmUtd2l0aC1hLWNh/bWVyYS1mcmVlLXBo/b3RvLmpwZw",

    dilate=(9, 9),

    blur=7,

    save_diff="diff.png",

    save_norm="norm.png",

)