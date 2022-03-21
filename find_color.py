import numpy as np
import cv2
  
def find_color(url):
    imageFrame = cv2.imread(url)
  
    # Convert the imageFrame in 
    # BGR(RGB color space) to 
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    cv2.imwrite('./img/crop_hsv.jpg',hsvFrame)

    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    # 形态变换、每种颜色的膨胀以及 imageFrame 和蒙版之间的bitwise_and运算符确定仅检测该特定颜色
    kernal = np.ones((5, 5), "uint8")

    # # 1
    # # Set range for black color and 
    # # define mask
    # black_lower = np.array([0, 0, 0], np.uint8)
    # black_upper = np.array([180, 255, 46], np.uint8)
    # black_mask = cv2.inRange(hsvFrame, black_lower, black_upper)
    # # For black color
    # black_mask = cv2.dilate(black_mask, kernal)
    # # Creating contour to track black color
    # contours, hierarchy = cv2.findContours(black_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
      
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if(area > 550):
    #         print('color is black, HSV: [0,0,0], RGB: [0,0,0]')
    #         return
    
    # # 2
    # # Set range for white color and 
    # # define mask
    # white_lower = np.array([0, 0, 221], np.uint8)
    # white_upper = np.array([180, 30, 255], np.uint8)
    # white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)
    # # For white color
    # white_mask = cv2.dilate(white_mask, kernal)
    # # Creating contour to track white color
    # contours, hierarchy = cv2.findContours(white_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
      
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if(area > 550):
    #         print('color is white, HSV: [0,0,100], RGB: [255,255,255]')
    #         return
  
    # 3
    # Set range for red color and 
    # define mask
    red_lower = np.array([0, 43, 46], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 550):
            print('color is red, HSV: [0,100,100], RGB: [255,0,0]')
            return
    
    # 4
    # Set range for orange color and 
    # define mask
    orange_lower = np.array([11, 43, 46], np.uint8)
    orange_upper = np.array([25, 255, 255], np.uint8)
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)
    # For orange color
    orange_mask = cv2.dilate(orange_mask, kernal)
    # Creating contour to track orange color
    contours, hierarchy = cv2.findContours(orange_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 550):
            print('color is orange, HSV: [25,100,100], RGB: [255,106,0]')
            return
    
    # 5
    # Set range for yellow color and 
    # define mask
    yellow_lower = np.array([26, 43, 46], np.uint8)
    yellow_upper = np.array([34, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)
    # For yellow color
    yellow_mask = cv2.dilate(yellow_mask, kernal)
    # Creating contour to track yellow color
    contours, hierarchy = cv2.findContours(yellow_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 550):
            print('color is yellow, HSV: [60,100,100], RGB: [255,255,0]')
            return
    
    # 6
    # Set range for green color and 
    # define mask
    green_lower = np.array([35, 43, 46], np.uint8)
    green_upper = np.array([77, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    # For green color
    green_mask = cv2.dilate(green_mask, kernal)
    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 550):
            print('color is green, HSV: [120,100,100], RGB: [0,255,0]')
            return
    
    # 7
    # Set range for cyan color and 
    # define mask
    cyan_lower = np.array([78, 43, 46], np.uint8)
    cyan_upper = np.array([99, 255, 255], np.uint8)
    cyan_mask = cv2.inRange(hsvFrame, cyan_lower, cyan_upper)
    # For cyan color
    cyan_mask = cv2.dilate(cyan_mask, kernal)
    # Creating contour to track cyan color
    contours, hierarchy = cv2.findContours(cyan_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 550):
            print('color is cyan, HSV: [180,38,50], RGB: [80,128,128]')
            return
    

    # 8
    # Set range for blue color and
    # define mask
    blue_lower = np.array([100, 43, 46], np.uint8)
    blue_upper = np.array([124, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    # Creating contour to track blue color
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 550):
            print('color is blue, HSV: [240,100,100], RGB: [0,0,255]')
            return

    # 9
    # Set range for purple color and
    # define mask
    purple_lower = np.array([125, 43, 46], np.uint8)
    purple_upper = np.array([155, 255, 255], np.uint8)
    purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper) 
    # For purple color
    purple_mask = cv2.dilate(purple_mask, kernal)
    # Creating contour to track purple color
    contours, hierarchy = cv2.findContours(purple_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 550):
            print('color is purple, HSV: [300,100,100], RGB: [255,0,255]')
            return
    

    print('I dont know')