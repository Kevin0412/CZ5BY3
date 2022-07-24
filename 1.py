from PIL import Image
import numpy as np
height=[379,388]#空间站轨道高度
latitude=19.63742#发射场纬度
radius=6378.137#地球赤道半径
e_1=298.257223563#地球偏心率
name='0724_1.png'#读入图片
img1=Image.open(name)
img=np.asarray(img1)
a=[]
for x in range(799,801):#图片转角度
    for y in range(2,1599):
         if img[x][y][0]==img[x][y][1] and img[x][y][1]==img[x][y][2] and img[x][y][0]!=255 and img[x][y][0]!=0:
            a.append(y)
            img1.putpixel((y,x),(255,0,0,255))
b=0
for c in a:
    b+=c
b=b/len(a)
if b>799:
    c=-1
    b=(1599-b)/799.5*90
else:
    c=1
    b=b/799.5*90

r=radius*((1-1/e_1**2)/(1-1/e_1**2+np.tan(np.radians(latitude))**2))**0.5/np.cos(np.radians(latitude))#计算发射场到地心距离
ans1=0
for h in height:
    ans=np.arcsin((-r+(r**2+h**2+h**2/np.tan(np.radians(b))**2+2*r*h+2*r*h/np.tan(np.radians(b))**2)**0.5)/(1+1/np.tan(np.radians(b))**2)/np.tan(np.radians(b))/(r+h))#解三角形，计算角度
    ans=np.arcsin(np.sin(ans/2)/np.cos(np.radians(latitude)))/np.pi*(23*3600+56*60+4)#角度投影并转为时间
    ans1+=ans
print(str(c*int(ans1/120))+"'"+str((ans1/2)%60)+'"'+' ±'+str(abs(ans1/2-ans))+'"')#输出结果
img1.save(name.split('.')[0]+'_1.png')#导出图片，估读红点时间，红点位置位于正东或正西方向，为经过发射场同纬度的时间
