import os
from glob import glob
from utils import adjust_image
from utils import show_images_side_by_side

image_path = glob('images/*.*g')

out_dir = 'results'

i = 0
for img_path in image_paths:
    img_before, img_after = adjust_image(img_path, 1.47, 1.22, 1.19)
    show_images_side_by_side(img_before, img_after)
    # create output dir
    os.makedirs(out_dir)
    # save results inside output dir
    output = out_dir + '/' + str(i) + '.jpg'
    img_after.save(output, format="JPEG" , quality=85, optimize=True)
    i = i+1

# image_d.save('result.png')
# image_d.save('result_2.jpg', format="JPEG" , quality=85, optimize=True)
