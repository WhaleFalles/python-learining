#!python

import requests,os,bs4,sys

url='https://bing.ioliu.cn/?p=1'# url of Bing Wallpaper site
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140Safari/537.36 Edge/17.17134'}

## reserach for the first wallpaper's url
print('Downloading page %s'% url)
res=requests.get(url,headers=headers)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
elem=soup.select('div a')
if elem==[]:
    print('error')
    sys.exit(0)
else:
    #for i in range(10):
     #   pass
     #   print(elem[i],end='\n')
    url='https://bing.ioliu.cn'+elem[4].get('href')
#print(url)



## analysis response to reserach for the HD wallpaper'url
res=requests.get(url,headers=headers,timeout=3)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
elem=soup.select('img')
newimgurl=''
if elem==[]:
    print('error')
    sys.exit(0)
else:
    #for i in range(10):
     #   print(elem[i],end='\n\n\n')
    newimgurl=elem[0].get('data-progressive')



## save img file on your desktop
res=requests.get(newimgurl,headers=headers,timeout=3)
imagefile=open(os.path.basename(newimgurl),'wb')
for chunk in res.iter_content(100000):
    imagefile.write(chunk)
imagefile.close()
print('The new wallpaper on your desktop is \"%s."'%os.path.basename(newimgurl))



##set wallpaper 
import win32api,win32con,win32gui

def set_wallpaper(img_path):
    reg_key=win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
set_wallpaper('c:\\Users\\administrator\\desktop\\'+os.path.basename(newimgurl))
print('================task done==============')
