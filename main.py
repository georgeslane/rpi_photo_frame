from photo_display import Display

PhotoFrame = Display()
images = PhotoFrame.get_photos(path='42_octillion_quarks_in_love/')
PhotoFrame.display(images=images)