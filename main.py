import cv2

from attractor_network import AttractorNetwork 
from configuration import Configuration

# 1. Recuperar imagem a ser memorizada
image = cv2.imread('examples/myself.jpg', cv2.IMREAD_GRAYSCALE)
resized_image = cv2.resize(image, (64, 64), interpolation=cv2.INTER_NEAREST)
_, binarized_image_pattern = cv2.threshold(resized_image, 128, 1, cv2.THRESH_BINARY)
#_, binary_inv_image = cv2.threshold(resized_image, 128, 1, cv2.THRESH_BINARY_INV) # inversão de cores

cp_binarized_image = binarized_image_pattern.copy() # this is copying only the header, not the data itself (get it) 
cp_binarized_image.tobytes()

configuration = Configuration(cp_binarized_image, "foto_rosto_tiago").flat() # binarized image COPY

attractor_net = AttractorNetwork()
attractor_net.add_configuration(configuration)

# Last. Criar versão da com distúrbios na imagem 
disturbed_binary_image = binarized_image_pattern.copy() # this is copying only the header, not the data itself 
disturbed_binary_image.sort()
disturbed_binary_image.tobytes()
print(f"disturbed_bin_img: {disturbed_binary_image}")

attractor_net.converge(disturbed_binary_image)





