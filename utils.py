import numpy as np
import cv2

def linear_mapping(img):
    return (img - img.min()) / (img.max() - img.min())


def pre_process(img):

    #görüntüden yükseklik ve genişlik değerleri alınır.
    height, width = img.shape
    
    #Logaritma işlemi yapılır. Log işlevi, ışık efektlerini azaltmak ve kontrastı artırmak için uygulanır.
    img = np.log(img + 1)

    #Görüntü standardize edilir.
    img = (img - np.mean(img)) / (np.std(img) + 1e-5)

    # Hanning pencere fonksiyonu kullanılır
    window = window_func_2d(height, width)
    
    #Bu çerçeve görüntü üzerine uygulanır.
    img = img * window
    
    return img

def window_func_2d(height, width):

    #Bu fonksiyon cosinus penceresini oluşturmak için kullanılır.

    #Hanning fonksiyonu ile pencere için gerekli değerler oluşturulur.
    win_col = np.hanning(width)
    win_row = np.hanning(height)

    #Satır ve sütun değerleri hanning den gelen değerler kullanılarak maskelenir.
    mask_col, mask_row = np.meshgrid(win_col, win_row)

    #Pencere oluşturulur. 
    win = mask_col * mask_row

    return win


