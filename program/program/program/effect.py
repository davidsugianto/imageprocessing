from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
for i in range(100):
	camera.annotate_text="Contrast:%s"%i
	camera.contrast = i
	sleep(0.1)
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
	camera.image_effect = effect
	camera.annotate_text="Effect: %s"%effect
	sleep(1)	
camera.stop_preview()

