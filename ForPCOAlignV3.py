import h5py
import cv2
import os
from os import listdir
from os.path import isfile, join
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import ion
from scipy.signal.signaltools import wiener

from scipy import math
from math import atan
            
def findContour(nxsfileName,dataFolder, minColumn=0,maxColumn=4000,minCrop=0,maxCrop=2000, thresh=400):
    print nxsfileName
    
    mypath=h5py.File(nxsfileName,'r') 
    print 'looking for "',dataFolder, '" in the tree...'
    contLoop=True
    pathTot=''
    contLoop, pathToData, pathTot=myRec(mypath,contLoop,pathTot,dataFolder)
    print pathTot
    if not contLoop:
        print 'database "',dataFolder,'" found in  ', pathTot
        data=mypath[str(pathTot)]
        npdata=np.array(data)
        a,b,c=npdata.shape
        print a,b,c, ' file images to analyse' 
        #sizeA=int(math.sqrt(a))
        #print 'size', sizeA
        #s=(sizeA,sizeA)
        #image=np.zeros((b,c))
        imageorig=data[0,:,:]
        #plt.imshow(imageorig,clim=[100,150])
        #plt.show()
        
        #minColumn,maxColumn,minRow,maxRow, thresh
        colmin=minColumn
        colmax=maxColumn
        #rowmin=minRow
        #rowmax=maxRow
        threshold=thresh
        
        aa=minCrop#1475
        bb=maxCrop#1810
        #aa=810
        #bb=920
        #print np.shape()
        rows,cols = np.shape(imageorig)

        #M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        #image2 = cv2.warpAffine(imageorig,M,(cols,rows))
        
        image2=np.transpose(imageorig)
        image2=np.flipud(image2)
        #plt.figure(101)
        #plt.imshow(image2,clim=[100,150])
        #plt.show()
        image=np.squeeze(image2)[aa:bb,:]
        print np.shape(image)
        #plt.figure(100)
        #plt.imshow(image,clim=[100,150])
        #plt.show()
        maximg=np.max(np.max(image))
        minimg=np.min(np.min(image))
        print 'maxvalue', maximg, minimg
        
        d,e=np.shape(image)     
        print d,e,'size'
        #plt.figure(2)
        #plt.imshow(image,clim=[100,150])
        #plt.show()
        print 'this is d',d
        #position=np.zeros((1,2))
        '''
        colmin=1000
        colmax=3000
        rowmin=1450
        rowmax=1550
        threshold=350
        '''
        
        
        count=0
        for i in range(d):
            for j in range(e):#colmin,colmax):
                if image[i,j]>threshold:
                    #position[count][0]=i
                    #position[count][1]=j
                    count=count+1
        '''
        for i in range(d):
            for j in range(2701,e-500):
                if image[i][j]>threshold:
                    #position[count][0]=i
                    #position[count][1]=j
                    count=count+1
        '''
        positionX=np.zeros(count)
        positionY=np.zeros(count)
        count=0
        for i in range(d):
            for j in range(e):#colmin,colmax):
                if image[i,j]>threshold:
                    positionX[count]=j
                    positionY[count]=d-i
                    print j,i
                    count=count+1
        '''
        for i in range(d):
            for j in range(2701,e-500):
                if image[i][j]>500:
                    positionX[count]=j
                    positionY[count]=i
                    count=count+1
        '''
        print positionX,positionY
        figure=plt.figure(10)
        plt.plot(positionX,positionY,'ro')
            
        #plt.show()
        #plt.figure(200)
        [m,q]=np.polyfit(positionX, positionY, 1)
        
        xrange=np.linspace(0, b, b)
        yrange=np.zeros(b)
        for i in range(b):
            yrange[i]=m*xrange[i]+q
        print np.shape(xrange)
        plt.plot(xrange,yrange,'r',linewidth=2.0)
        #plt.imshow(image)
        plt.text(1000, 500, r'angle = '+str(math.degrees(atan(m)))+' degrees')
        #plt.imshow(image)
        plt.show()
        print'I am here!!!'
        
        #positionyCalc=
        
        print math.degrees(atan(m)),m,q
        return math.degrees(atan(m))
       

      
def myRec(obj,continueLoop,pathTot,dataFolder):  
    ### recursive function to look for the data database
    temp=None
    i=1
    tempPath=''
    for name, value in obj.items():
        if continueLoop:
            #check if the object is a group
            if isinstance(obj[name], h5py.Group):
                tempPath='/'+name
                if len(obj[name])>0:
                    continueLoop,temp,tempPath= myRec(obj[name],continueLoop,tempPath,dataFolder)
                else:
                    continue
            else:
                test=obj[name]
                temp1='/'+dataFolder
                if temp1 in test.name:
                    continueLoop=False
                    tempPath=pathTot+'/'+name
                    return continueLoop,test.name,tempPath
            i=i+1
        if (i-1)>len(obj.items()):
            tempPath=''
    pathTot=pathTot+tempPath
    return continueLoop,temp, pathTot

    
   
#########For testing function
if __name__ == "__main__":
    pathToNexus='/dls/i13-1/data/2017/mt17254-1/raw/pco1-123847.hdf'
    #name='C:\\Users\\xfz42935\\Documents\\Alignement\\pco1-63429.hdf'
    
    #colmin=200
    #    colmax=1750
    #    rowmin=810
    #    rowmax=910
    #    threshold=220
    
    minColumn= 2500 
    maxColumn= 2672
    
    minCrop= 500
    maxCrop= 1200
    thresh=400
    findContour(pathToNexus,'data', 0,4000,0,2000, thresh)
    #findContour(pathToNexus,'data', minColumn,maxColumn,minCrop,maxCrop, thresh)
