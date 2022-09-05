import os
from PIL import Image

exclude_list = [
"mcmeta",
"fire",
"sea_lantern"
]

def get_dominant(file):
    image = Image.open(file)
    colors = image.getcolors()
    print(colors)
    if max(colors)[1][0..2] == 0:
        rem_index = colors.index(max(colors))
        print(rem_index)
        colors.pop(rem_index)
    return max(image.getcolors())

asset_list = [texture for texture in os.listdir("jar\\assets\\minecraft\\textures\\block\\") if not any(x in texture for x in exclude_list)]
for item in asset_list:
    print(item)
dominant_list = [get_dominant("jar\\assets\\minecraft\\textures\\block\\" + asset) for asset in asset_list]
print(dominant_list)