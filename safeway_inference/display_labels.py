import cv2
im = cv2.imread("segnet_labels.jpg")
cv2.imshow("labels", im)
#print(im.shape)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
    
