#!/usr/bin/env python
# coding: utf-8

# ## Black Theme

# Add custom CSS under the same name with .ipynb file in the same directory.

# https://rise.readthedocs.io/en/latest/customize.html#adding-custom-css

# 
# The approach that works is to add custom CSS alongside the notebook file.

# ### Code cell examples

# In[1]:


# this is where you press Shift-Enter
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

"Hello world"


# In[2]:


# of course you can show figures

def polynom(x):
    return 2 * x**2 - 20 * x + 2

X = np.linspace(-10, 10)
Y = polynom(X)
plt.plot(X, Y);


# ## Set Black Theme in Notebook Metadata

#         "rise": {
#             ...
#             "theme": "black"
#         }

# The default theme is simple, and there are 11 themes you can choose from black, white, league, sky, beige, simple, serif, blood, night, moon, and solarized.
# 

# |    |   Name |   Effect | 
# |---:|-----------:|---------------:|
# |  1 |     simple |        White background, black text, blue links (default) | 
# |  2 |      black |        Black background, white text, blue links |
# |  3 |      white |        White background, black text, blue links | 
# |  4 |     league |        Gray background, white text, blue links | 
# |  5 |      beige |        Beige background, dark text, brown links |
# |  6 |        sky |        Blue background, thin dark text, blue links| 
# |  7 |      night |        Black background, thick white text, orange links | 
# |  8 |       serif|        Cappuccino background, gray text, brown links |
# |  9 |   solarized|        Cream-colored background, dark green text, blue links|
# | 10 |       blood|         Dark background, thick white text, red links   |
# | 11 |        moon|         Dark blue background, thick grey text, blue links|

# ## Add custom CSS named the same with .ipynb file in the same directory.

# You can copy the rise.css file in this folder to your target notebook file to set up the black theme.
# 
# [demo/rise.css](https://github.com/YiqinZhang/OPE-RISE/blob/47efc63ae2556eff1d1cc5bc21b3150a75172d63/demo/rise.css)

# Alternatively, you can add these modifications in the custom CSS file as listed below:

# - Set markdown cells background black

#     /* ---------- slides background black----------*/
#     body.rise-enabled.theme-black
#       div.jp-RenderedHTMLCommon
#       tbody
#       tr:nth-child(even), 
#       body.rise-enabled.theme-black div.jp-RenderedHTMLCommon thead th, 
#       body.rise-enabled.theme-black div.jp-RenderedText > pre, 
#       body.rise-enabled.theme-black div.jp-RenderedHTMLCommon, 
#       body.rise-enabled.theme-black div.jp-MarkdownCell.jp-mod-rendered {
#         color: white;
#         background-color: #191919;
#     }

# - Set slides margin black

#     /* ---------- background of code block in markdown black----------*/
#     body.rise-enabled.theme-black div.jp-RenderedHTMLCommon pre, 
#     body.rise-enabled.theme-black div.jp-RenderedHTMLCommon code {
#         color: white;
#         background-color: #191919;
#     }

# - Set code cell background black

#     /* ---------- slides margin background black----------*/
#     body.rise-enabled.theme-black div.slide-background, 
#     body.rise-enabled.theme-black div.slide-backgournd-content, 
#     body.rise-enabled.theme-black div.jp-Notebook{
#         background-color: #191919;
#     }

# #  Hide the Code input

# Add custom CSS in the same directory with .ipynb file.

# - Hide input cell number

#     /* ---------- hide input cell number----------*/
#     div.jp-InputPrompt, div.jp-InputArea-editor{
#         display: none;
#     }
#     div.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
#         display: none;
#     }

# - Hide output cell number

#     /* ---------- hide output cell number ----------*/
#     div.jp-OutputPrompt, div.jp-OutputArea-prompt{
#         color: rgba(0, 0, 0, 0);
#     }
#     div.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
#         color: rgba(0, 0, 0, 0);
#     }

# - Hide three dots when folding the cell

#     /* ---------- hide the three dots after folding the cells-----*/
#     div.f1m36mmi svg{
#         display: none;
#     }

# In[3]:


print('All Set')


# In[ ]:




