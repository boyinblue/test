import cv2

if __name__ == '__main__':
    img = cv2.imread('test.png')
    cv2.imshow('window_name', img)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#    cv2.destroyWindow('window_name')
    
    cv2.destroyAllWindows()
