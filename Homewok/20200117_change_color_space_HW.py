import cv2

img_path = 'data/lena.png'

# 以彩色圖片的方式載入
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 改變不同的 color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(img, cv2.COLOR_LBGR2Lab)
 

# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    cv2.imshow('bgr', img)
    cv2.imshow('hsv', img_hsv)
    cv2.imshow('hls', img_hls)
    cv2.imshow('lab', img_lab)
    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break