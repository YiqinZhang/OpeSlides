#!/usr/bin/env python
# coding: utf-8

# # Quick start

# ## Turn your notebooks into slideshows

# ```sh
# Alt + r
# ``` 

# ### Press ```Space``` to keep on 
# You can write a regular Jupyter notebook, with the usual mix of markdown and code cells 

# If you press 
# ```sh
# Shift + Space 
# ``` 
# you will go backwards.

# In code cells, you press 
# ```sh
# Shift + Enter
# ```
# as usual to evaluate your code.

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


# ### Zoom in | Zoom out

# <table>
# <tr>
#    <td width="50%">
#        <p>zoom in</p>
#        </td>
#    <td> 
#        <p>zoom out </p>
#        </td>
#     </tr>
#    <tr>
#        <td width="60%">
#             <p>Alt + </p>
#            </td>
#       <td> 
#           <p>  Alt - </p>  
#           </td>
#    <tr>
#     <tr>
#        <td width="60%">
#             <p>Ctrl + </p>
#        </td>
#        <td> 
#           <p>  Ctrl - </p>   
#     </td>
#     </tr>
# </table>    

# You're in a browser, so you can always use smaller / larger fonts deponding on your platform.

# ### Toggle overview

# Press `w` to see the overview of all slides

# Navigate with `Left arrow` and `Right arrow` 

# ## Edit cells

# - `A` insert a new cell above active cell
# - `B` insert a new cell below
# - `M` set to a Markdown cell
# - `Y` set to a Code cell

# - `X` cut selected cell
# - `C` copy selected cell
# - `V` paste cell copied/cut
# - `D` + `D` (D twice) delete active cell.
# - `Z` undo cell deletion

# ### Run code from a different kernel

# Use IPython Magics with the name of your kernel at the start of each cell
# 
#     %%bash
#     %%HTML
#     %%python3
# 

# ## Add slide tag to each cell

# * `shift-i` : toggle slide
# * `shift-b` : toggle subslide
# * `shift-g` : toggle fragment

# ### RISE notebook extension
# 
# See full documentation at http://rise.readthedocs.io/.

# # Speaker notes

# ### Press `t`,  presenter view window will pop out.
# 

# The presenter view shows *Notes* cells, which won't appear in the main slides.

# 
# This is an example of a 'Notes' cell. Put an `Enter` at the front of the Notes cell to avoid the repetitive display of the first paragraph.Put an `Enter` at the front of the Notes cell to avoid the repetitive display of the first paragraph.
# 
# 
# Use two 'Enter' to make one blank line to form a separate paragraph. Use two 'Enter' to make one blank line to form a separate paragraph. 

# * Put all notes in one cell per slide
# * Put an `Enter` at the front of the Notes cell
# * Use two `Enter` to seperate paragraphs

# 
# Put all notes in one cell per slide. Don't make consecutive Notes cells, showing only the first note cell among them.
# 
# 
# We can also write Code blocks in the notes
# 
#     1. Use ` 
#     2. Use Tap
#     3. Two Enter + Tap to make a Code block.
# 

# This is an example of a *Skip* cell.

# # Metadata Setting

# Edit tags under the **“Property Inspector”** menu with the gears icon at the top-right corner. 
# 
# Tags UI in JupyterLab looks like:

# ![](../images/setting.png)

# ### Two levels of metadata

# + <font color='orange'>For cell level</font> 
# 
# Edit Cell Metadata, and click the checkmark right below the metadata tag to save the changes. 

# ![](../images/cell-metadata.png)

# + <font color='orange'>For notebook level</font> 
# 
# Edit Notebook Metadata, and click the checkmark below the metadata tag to save the changes. 

# ![](../images/nb-metadata.png)

# #  Custom RISE

# Source: [RISE documentation](https://rise.readthedocs.io/en/latest/customize.html#customizing-rise)

# Here is the rise 
# configuration for this demo file.

# ```javascript
#     "rise": {
#         "enable_chalkboard": true,
#         "footer": "Hello World",
#         "header": "Quick Start",
#         "rise": {
#             "height": "90%",
#             "width": "90%"
#         },
#         "scroll": true,
#         "start_slideshow_at": "selected",
#         "transition": "none"
#     }   
# ```

# Plus, all parameters we can use.

# ```javascript
#     "rise": {
#         "autolaunch": false,
#         "enable_chalkboard": false,
#         "start_slideshow_at": "beginning",
#         "auto_select": "code",
#         "show_buttons_on_startup": false,
#         "header": "",
#         "footer": "",
#         "backimage": false,
#         "overlay": "",
#         "theme": "simple",
#         "transition": "cube",
#         "slideNumber": "h/v",
#         "width": "100%",
#         "height": "100%",
#         "controls": true,
#         "progress": true,
#         "history": true,
#         "scroll": true,
#         "center": true,
#         "auto_select_timeout": 450,
#         "restore_timeout": 500,
#         "async_timeout": 250
#     }
# ```

# # CSS

# 2 files are loaded without the need for configuring
# 
# * `rise.css` in the current directory
# * `quickstart.css` for this notebook because it is called `quickstart.ipynb`

# ## Custom CSS 

# You can copy the rise.css file in this folder to your target notebook file to set up the slideshow effect.
# 
# [demo/rise.css](https://github.com/YiqinZhang/OPE-RISE/blob/47efc63ae2556eff1d1cc5bc21b3150a75172d63/demo/rise.css)

# Alternatively, you can add custom CSS named the same with .ipynb file in the same directory.

# # Chalkboard

# You can turn on the *chalkboard* in the notebook metadata with:
# 
# ```css
#     ...
#     "rise": {
#       "enable_chalkboard": true
#     }
#     ...
# ```

# Chalkboard displays itself with two extra buttons in the lower left area

# ![](chalkboard.png)

# ## Keyboard commands

# It also reacts to the following additional keyboard commands:
# 
# - `[` to turn the whole space into an empty chalkboard
# 
# - `]` to start adding free drawings to the current slide
# - `\` to download chalkboard drawing
# - `=` to reset chalkboard drawing on the current slide
# - `-` to clear the chalkboard
# 

# ## Eraser

# Long press the right mouse button can turn on the eraser

# ## Change chalk color

# After clicking the chalkboard button, press the keyboard `s` to switch to the next color and `q` to switch to the previous color.

# The default chalk color is <font color='grey'>grey</font>. And other color choices are <font color='blue'>blue,</font> <font color='red'>red, </font>
# <font color='green'>green, </font>
# <font color='orange'>orange, </font>
# <font color='purple'>purple, </font> and
# <font color='yellow'>yellow.</font>

# If you started writing and want to change to another color, double-click the chalkboard button and then press the keyboard `s` or `q` to choose the color.

# ![](../images/chalk.png)
