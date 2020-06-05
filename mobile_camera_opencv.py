# necessary python module for this script
# pip3 install numpy opencv-python requests
import requests
import numpy as np
import cv2 as cv

#chnage this url according yours 
url = "http://192.168.43.23:8080/shot.jpg"

while True:
    # Getting Raw data
    RawData = requests.get(url, verify=False)

    # Convertting it to serilized one deminsion array
    One_D_Arry = np.array(bytearray(RawData.content),dtype = np.uint8)
    
    # converting One deminsion Array into opencv image matrxi, format using "imdecode" function 
    frame = cv.imdecode(One_D_Arry, -1)

    # show image on the screen, using imshow function of opencv
    cv.imshow("window", frame)

    # break out of loop when/if "q" key press on the keyborad by using waitKey fuction of opencv
    if cv.waitKey(1)==ord('q'):
        break

