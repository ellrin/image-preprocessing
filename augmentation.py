import cv2
import numpy as np
import matplotlib.pyplot as plt
import os, shutil


print('enter image input path:')
img_path = str(input()) 
print('enter image output path:')
output_path = str(input()) 




print('Check if all files are image')

for file in os.listdir(img_path):
    if ((file[-3:]) != ('png')) and ((file[-3:]) != ('jpg')):
        print(file+' is not an image file')
        assert False
        
    
print('All files in input folder are images')




if os.listdir(output_path)!= []:
    print('The output folder is not empty, continue? Type "yes" or "no"')
    
    false_count = 0
    for i in range(4):
        conti_or_not = str(input())
    
        if conti_or_not == 'yes':
            break

        if conti_or_not == 'no':
            assert False

        if (conti_or_not!='yes' and conti_or_not != 'no'):
            
            false_count += 1
            if false_count > 3:
                assert False
                
            print('press "yes" or "no" %d/3'%false_count)




def img_resize(img, desired_size):
    
    assert len(img.shape) ==3
        
    init_size = img.shape[:2]  # arr.shape = (12,24,36), arr.shape[:2] = (12,24)
    ratio = float(desired_size) / max(init_size)
    new_size = tuple([int(x*ratio) for x in init_size])  # tuple is a python way to save the string
    img = cv2.resize(img, (new_size[1], new_size[0]))
    
    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h - (delta_h//2)
    left, right = delta_w//2, delta_w - (delta_w//2)
        
    color = [0,0,0]
    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    
    return new_img



def img_rotate(image, angle, center=None, scale=1.0):
    
    (h, w) = image.shape[:2]
 
    if center is None:
        center = (w / 2, h / 2)
 
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(image, M, (w, h))
 
    return rotated_img





# resize or not 
print('Resize? Type "yes" or "no"')

for try_time in range(4):
    resize_or_not = str(input())
    
    if resize_or_not == 'yes':
        resize = True
        
        print('Enter an integer:')
        
        # check if the input is an integer
        for int_try_time in range(4):
            resize_size = (input())
            
            try:
                resize_size = int(resize_size)
            except:
                pass
            
            if type(resize_size) !='int':
                if int_try_time == 3:
                    assert False
                    print('Enter an integer: %d/3'%(int_try_time+1))
        
            break
        break

    if resize_or_not == 'no':
        resize = False
        break

    if (resize_or_not!='yes' and resize_or_not != 'no'):
        if try_time == 3:
            assert False
                
        print('press "yes" or "no" %d/3'%false_count)

        


# rotate or not 
print('Rotate? Type "yes" or "no"')

for try_time in range(4):
    rotate_or_not = str(input())
    
    if rotate_or_not == 'yes':
        rotate = True
        
        print('Enter an integer:')
        
        # check if the input is an integer
        for int_try_time in range(4):
            rotate_angle = (input())
            
            try:
                rotate_angle = int(rotate_angle)
            except:
                pass
            
            if type(rotate_angle) !='int':
                if int_try_time == 3:
                    assert False
                    print('Enter an integer: %d/3'%(int_try_time+1))
        
            break
        break

    if rotate_or_not == 'no':
        rotate = False
        break

    if (rotate_or_not!='yes' and rotate_or_not != 'no'):
        if try_time == 3:
            assert False
                
        print('press "yes" or "no" %d/3'%(try_time+1))



        
# flip or not
print('Flip? Type "yes" or "no"')
false_count = 0
for try_time in range(4):
    flip_or_not = str(input())
    
    if flip_or_not == 'yes':
        flip = True
        break

    if flip_or_not == 'no':
        flip = False
        break

    if (flip_or_not != 'yes' and flip_or_not != 'no'):
        if try_time == 3:
            assert False
                
        print('press "yes" or "no" %d/3'%(try_time+1))

        

# START 
for idx, file in enumerate(os.listdir(img_path)):
    
    img = cv2.imread(img_path+file)
    img_name = file[:-4]
    
    ### resize
    if resize:
        img = img_resize(img, resize_size)
        img_name = img_name+'_resize'
    
    ### flip
    if flip:
        img = cv2.flip(img, 1)
        img_name = img_name+'_flip'
    
    
    
    ### rotate
    if rotate:
        img_rotate(img, rotate_angle)
        img_name = img_name+'_rotate%d'%rotate_angle
    
    
    cv2.imwrite((output_path+img_name+'.png'), img)
    print('%4d '%(idx+1), (img_name+'.png \t saved'))

