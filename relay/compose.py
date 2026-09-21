import base64, io
from PIL import Image, ImageDraw
B22="iVBORw0KGgoAAAANSUhEUgAAAO0AAABACAYAAAD2z/C/AAAEQUlEQVR4nO2cQW7mIAyF09Hsq0q9/wkrVT1BZxVNSgkxYOxn875llf4Y2y+AgRwHIYQQQgghhBASkxdvAzLw/vb6LX324/OLPidTMIEm6BHrExQzkcJEGUBTrE9QzKSECdGBpVglUNB7wqALQRNsC4o5NwyugEiCvYNCzgMD2SCDWFtQyDFh0CpkF2sNdAH3xgS9PzOk7dgoOwq2hlXSsxLfT4pOzEKh3qOR6Gj+jS7e0MZrgJZQSFyT+/3t9btM9ui+iyrekEbPEj3ZSlrJN9rX7IK9Ek28oYzVIEuylaJa9fulYLP4rySScP96G2BFlmS7iilyG2icfY0g3vSizZR4H59fL9b92WGUvVJbCqDxy7hrYNCNb7FDgp1orjfLUdZz1LV8Sd21haiB5kgb4a1TklmstVi8v71+r+rzLtPk1ssBUQOP02NEo2tkTiwr8SCJ1CrnJKM5mgbCr2kRE0zbJq+pqXWbJQixPUEqVP0p/3A3BbMxR87KaWEPNX99fH69IARXAwQfr2JkzYzgj1+ivQPB2OPAEuuTMM9nIgkYxbdebUja9vZR1/TYc27v7aiT0f4/rRe9z/he20d4yVjEe6YN6f+24j7q56Hjb5ZBjS7WHjT6OrqvWjsB5eV7j/3ole1L/NmTX0OFKIsRF0Gsmn206g+C30gdra2l4erxqmoaQtJ5T1WJPx6jvVRT4kLUU0Mav+M9JdIoGnn3YxaE9aw33lt2T8/firYneLMLes+1k2Z1N6pYvdew0enJIY1cUztc0TNd9hTpit9lsu/NNfc1Z553+dpMYs9qpgYzIt1JiEiV49MeBP+P2NH6nxEt1HK4OdJqOC/Ch7sQEoT853x5MC51HqfHyM4bESlqX3YHOc+kWPVBtKbtMWal4RTpT6yKhRaU9mUfbaV9q61t1W/5aK6LekWaNcDHEecihyaj6z7UC/tah5LEou1568189SDT6KGJRxEP1b9PIrW+f2zR1pWl92lr20B3Dpb+FtmTHoFobrtYtNOLyxpxx6keOmgx8Z7yWtVmJG0sX9NKoEBJibdIayDsWdfoFi3yWofMY3lnGlGox/Hbrp6rdTBbPoRo4XlCTsLsAZ1Vd3Gv8JjfZnhso6EL9eTJN1pnFXr8oSpaSYPEHoQvbKBOe1toCba3PYrWEavqa5T7rpFyw2PbUTLa3tk1tabdsSjVI5rWs6P71ahEzANkn7dsM738HenTNMgBXUHNlz0vnWh43Qg7B7qnkXa5aGsN75b0UYguthm8B43rzHTmlCCFtQEU6lqkp5quz9VEK7WVok3OXaLcPZMBr1neqosxJRRtYiRTsSzstBzbpqM787TRH1HIO4m0hMcYE5OlOBjV7lXQGUl5Knp4QyGOQ8dtgOSonFURhcxD5ydHMkX2OhxDxmAQNoSjamwYkM2QXhkjuLB6vDEUKSGEEEIIIYQQQiz5B0xue9nGfKd5AAAAAElFTkSuQmCC"
base=Image.open('assets/img_001.png').convert('RGBA')
body=Image.open(io.BytesIO(base64.b64decode(B22))).convert('RGBA').resize((249,67),Image.LANCZOS)
# rotate 4deg clockwise around left-middle (css rotate(4deg) is clockwise)
big=Image.new('RGBA',(249*2,67*4),(0,0,0,0)); big.paste(body,(249,67*2-33),body)
rot=big.rotate(-4,resample=Image.BICUBIC,center=(249,67*2))
base.alpha_composite(rot,(876-249,566+33-67*2))
d=ImageDraw.Draw(base)
def bez(p0,p1,p2,p3,n=40):
    return [tuple((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t**2*c+t**3*e for a,b,c,e in zip(p0,p1,p2,p3)) for t in [i/n for i in range(n+1)]]
d.line(bez((852,582),(864,588),(876,594),(890,600)),fill=(20,17,15,255),width=4)
base.convert('RGB').save('relay_out/img_001_body.png')
print('ok')
