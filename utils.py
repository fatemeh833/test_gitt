from PIL import Image , ImageEnhance
import matplotlib.pyplot as plt

def adjust_image(img_path, brightness_factor,
                 cotrast_factor, color_factor):
    
    image_in = Image.open(img_path)

    # Enhance Brightness
    brightness_enhancer = ImageEnhance.Brightness(image_in)
    image_b = brightness_enhancer.enhance(brightness_factor)

    # Enhance Contrast
    contrast_enhancer = ImageEnhance.Contrast(image_b)
    image_c = contrast_enhancer.enhance(cotrast_factor) 

    # Enhance Color (Saturation)
    color_enhancer = ImageEnhance.Color(image_c)
    image_out = color_enhancer.enhance(color_factor)

    return image_in, image_out
 
    
def show_images_side_by_side(img_before, img_after):
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img_before, cmap='gray')
    axes[0].set_axis_off()
    axes[0].set_title('before')
    axes[1].imshow(img_after, cmap='gray')
    axes[1].set_axis_off()
    axes[1].set_title('after')
    plt.tight_layout()