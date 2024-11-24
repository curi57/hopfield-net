import matplotlib.pyplot as plt


# 'Imagem pixelada e Binarizada (disturbed)'
class Plotter:
    
    def plot(self, image, description):
        plt.imshow(image, cmap='gray')
        plt.title(description)
        plt.axis('off')
        plt.show()
    
    def plot_all(self, image, description):
        plt.imshow(image, cmap='gray')
        plt.title(description)
        plt.axis('off')
        plt.show()
