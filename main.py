from photo_display import Display
PATH ='42_octillion_quarks_in_love/'

PhotoFrame = Display()
images = PhotoFrame.get_photos(path=PATH)
PhotoFrame.display_slideshow(images=images, path=PATH)
