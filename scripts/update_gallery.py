import os

imgs = sorted(os.listdir("images"))
with open("gallery.html", "r", encoding="utf-8") as f:
    html = f.read()

start = html.index('<div class="gallery">') + len('<div class="gallery">')
end = html.index('</div>', start)
before = html[:start]
after = html[end:]

img_html = "\n".join([f'    <img src="images/{img}" alt="{img}" loading="lazy">' for img in imgs])

with open("gallery.html", "w", encoding="utf-8") as f:
    f.write(before + "\n" + img_html + "\n" + after)
