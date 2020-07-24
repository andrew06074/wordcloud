import multidict as multidict
import numpy as np
import os
import re
import collections
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
from os import path
from wordcloud import WordCloud


def getFrequency(sentence):
    #text frequency dict
    tfDict = multidict.MultiDict()
    #temp dict
    tempDict = {}

    # make dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
            continue
        val = tempDict.get(text, 0)
        tempDict[text.lower()] = val + 1
    for key in tempDict:
        tfDict.add(key, tempDict[key])
    return tfDict


def makeImage(text_counts):
    # load image
    image_color = np.array(Image.open(os.path.join(d, "original_image.jpg")))
    # subsample by factor of 3
    image_color = image_color[::3, ::3]

    # create mask  white is "masked out"
    image_mask = image_color.copy()
    image_mask[image_mask.sum(axis=2) == 0] = 255

    #enforce boundaries between colors
    edges = np.mean([gaussian_gradient_magnitude(image_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
    image_mask[edges > .08] = 255

    # create wordcloud
    wc = WordCloud(max_words=2000, mask=image_mask, max_font_size=75, random_state=42)

    # generate word cloud
    wc.generate_from_frequencies(text_counts)
    plt.imshow(wc)

    #change current dir so new file is saved in folder
    os.chdir(r"C:\Users\andre\Desktop\wordcloud-master\wordcloud-master")
    

    # create coloring from image
    image_colors = ImageColorGenerator(image_color)
    image_colors.default_color = [0.6,0.6,0.6]
    wc.recolor(None,image_colors)
    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation="bilinear")
    wc.to_file("wc_image.jpg")


# get data directory)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

#open text file and read
text = open(path.join(d, "use_text.txt"), encoding='utf-8')
text = text.read()

#get text frequencies
text_counts = getFrequency(text)
#create wordcloud based off of text frequencies
makeImage(text_counts)

