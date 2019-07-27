# 假设感觉有困难，可查看步骤中的提示（鼠标移到步骤小标题上点击出现的问号）。
local_path = r"py\Data""\\"
scores_file = "photo1.png"

with open("{}{}".format(local_path,scores_file), "rb") as image :
    im1 = image.read()

with open("{}{}".format(local_path,"photo2.png"), "wb") as image2 :
    image2.write(im1)

