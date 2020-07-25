import numpy as np
from PIL import Image, ImageEnhance
import pytesseract


# Morphology Dilate(膨胀)
def morphology_dilate(img, Dil_time=1):
    img = np.asarray(img)
    H, W = img.shape

    # kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(Dil_time):
        tmp = np.pad(out, (1, 1), 'edge')
        for y in range(1, H):
            for x in range(1, W):
                if np.sum(MF * tmp[y - 1:y + 2, x - 1:x + 2]) >= 255:
                    out[y, x] = 255

    return out


# Morphology Erode(腐蚀)
def morphology_erode(img, Erode_time=1):
    H, W = img.shape
    out = img.copy()

    # kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each erode
    for i in range(Erode_time):
        tmp = np.pad(out, (1, 1), 'edge')
        # erode
        for y in range(1, H):
            for x in range(1, W):
                if np.sum(MF * tmp[y - 1:y + 2, x - 1:x + 2]) < 255 * 4:
                    out[y, x] = 0

    return out


# Morphology Closing（形态学闭操作）
def morphology_closing(img, time=1):
    out = morphology_dilate(img, Dil_time=time)
    out = morphology_erode(out, Erode_time=time)
    return out


# Opening morphology（形态学开操作）
def morphology_opening(img, time=1):
    out = morphology_erode(img, Erode_time=time)
    out = morphology_dilate(out, Dil_time=time)
    return out


def identify_vc(img):
    """
     将图片转化为字符串，切割之后，转化为数字进行计算
     """
    text = pytesseract.image_to_string(img, lang='eng').strip().replace(' ', '')
    # if len(text) == 0:
    #     text = '1'
    return text


def noise_reduction(img, rangle):
    """
     截取下来验证码图片，并且进行灰度转化，二值化处理
     """
    # 截取验证码图片
    rangle = eval(rangle)
    img = img.crop(rangle)

    # convert()方法传入参数L，将图片转化为灰度图像
    img = img.convert("L")
    # img = np.asarray(img)
    # img = (img > 180) * 255
    # img = morphology_opening(img, 1)
    # print(img)
    # img = Image.fromarray(img).convert('L')
    # print('g')
    sharpness = ImageEnhance.Contrast(img)
    img = sharpness.enhance(3.0)
    img = img.resize((300, 100))
    # img.show()
    return identify_vc(img)


