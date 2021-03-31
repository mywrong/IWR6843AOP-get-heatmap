import time
from radar import TI
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
MAGIC_WORD = b'\x02\x01\x04\x03\x06\x05\x08\x07'



def normalize(data):
    data=(data-np.min(data))/(np.max(data)-np.min(data))
    return data


##初始化mmwave
ti=TI()
def capture(total_frames):
    nerror=0
    nframe=0
    interval=0.1
    data=b''
    warn=0
    rawimg=np.zeros((total_frames,12,256,2))
    plt.ion()
    start=time.time()
    while nframe<total_frames:
        print(nframe)
        time.sleep(interval)
        byte_buffer=ti._read_buffer()
        if(len(byte_buffer)==0):
            warn+=1
        else:
            warn=0
        if(warn>2):
            print("Wrong")
            break

        data+=byte_buffer
  
        try:
            idx1 = data.index(MAGIC_WORD)
     
            idx2=data.index(MAGIC_WORD,idx1+1)

        except:
            continue

        datatmp=data[idx1:idx2]
        data=data[idx2:]
        try:
            cube=doneRawfft(datatmp)#结束采集后可以将cube保存为.npy文件
            draw_heatmap(cube)#成像
            rawimg[nframe]=cube
            nframe+=1
        except:
            continue
        
    ti.close()
    print("rate=",total_frames/(time.time()-start))

def draw_heatmap(cube,HorV='V'):
    '''HorV=H显示水平热图，为V显示垂直热图'''
    plt.ion()  
    fft_data=cube[:,:,1]+cube[:,:,0]*1j
    img=np.zeros((fft_data.shape[1],fft_data.shape[1]),dtype=complex)
    if HorV=='H':
        data=fft_data[[10,8,6,4]]
    elif HorV=='V':
        data=fft_data[[1,0,6,5]]
    img[:,0:4]=data.T
    img=np.abs(np.fft.fft(img,axis=1))
    last_img=np.fft.fftshift(img,axes=1)
    last_img=normalize(last_img)
    plt.clf()
    plt.imshow(last_img,cmap=plt.get_cmap('seismic'))#last_img为热图矩阵
    plt.pause(0.01)


def doneRawfft(byte_buffer):

    cube=ti._process(byte_buffer)   
    return cube


capture(30)