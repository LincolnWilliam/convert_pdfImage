# import module
from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('doc00648320220401120903.pdf')

for i in range(len(images)):
# Save pages as images in the pdf

	images[i].save('doc00648320220401120903' + '.jpg', 'JPEG')


















































