def resize_rectangle_img(from_dir,to_dir,size=None):
    import glob
    import cv2
    files = glob.glob("from_dir/*.jpg") # .jpgのみ列挙

    for file in files:
        img = cv2.imread(file)

        # 読み込んだ画像の高さと幅を取得
        height = img.shape[0]
        width = img.shape[1]
        x1 = y1 = 0
        x2 = width
        y2 = height
        diff = abs(height - width)
        if height > width:
            y1 = int(diff/2)
            y2 = height - y1
        elif width>height:
            x1 = int(diff/2)
            x2 = width - x1
        img = img[y1:y2,x1:x2]

        if size!=None:
            img = cv2.resize(img,(size,size))

        cv2.imwrite(to_dir+file, img)
    
if __name__ == '__main__':
    resize_rectangle_img('/Users/sk/code/images/original/','/Users/sk/code/images/resized/')