SOURCE = picmaker
IMAGE_NAME = color

run:
	python $(SOURCE).py
convert:
	convert $(IMAGE_NAME).ppm $(IMAGE_NAME).png
display:
	display $(IMAGE_NAME).png
clean:
	rm -f *.png *.ppm
	rm -f *~
