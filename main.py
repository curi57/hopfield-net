import cv2

from attractor_network import AttractorNetwork 
from configuration import Configuration

# 1. Recuperar imagem a ser memorizada
image_pattern = cv2.imread('examples/myself.jpg', cv2.IMREAD_GRAYSCALE)
resized_image = cv2.resize(image_pattern, (64, 64), interpolation=cv2.INTER_NEAREST)
_, binarized_image_pattern = cv2.threshold(resized_image, 128, 1, cv2.THRESH_BINARY)
#_, binary_inv_image = cv2.threshold(resized_image, 128, 1, cv2.THRESH_BINARY_INV)

cp_binarized_image = binarized_image_pattern.copy() # this is copying only the header, not the data itself 
cp_binarized_image.tobytes()

pattern_configuration = Configuration(cp_binarized_image)
attractor_net = AttractorNetwork(pattern_configuration)

# Last. Criar versão da com distúrbios na imagem 
disturbed_binary_image = binarized_image_pattern.copy() # this is copying only the header, not the data itself 
disturbed_binary_image.sort()
disturbed_binary_image.tobytes()
print(f"disturbed_bin_img: {disturbed_binary_image}")

attractor_net.converge(disturbed_binary_image)





