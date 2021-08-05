from detect_mnist import run_model
from cell_segmentation.p1 import cell
import os

if __name__ =='__main__':
    path = os.path.join(os.getcwd(),"digit_cells")
    images = os.listdir(path)
    
    for img in images:
        run_model(os.path.join(path,img))

