#!/usr/bin/env python
# coding: utf-8

# - - - 

# # Image display

# - - - 

# **1)Image Only**

# **BODY**

# ### Double-clicking the image will change the display. 

# Problem1:
# 
# Right now, a double-click will show the source code since we wrote HTML code to display the images.

# Makeup:
# 
# ```sh
# Shift + Enter
# ```
# to run the code in the current cell.

# <img src="../images/default.png" width = "100%">

# - - - 

# Probleme2:
# 
# If it were markdown, it would disappear because we set the input code cell to be hidden.

# <img src="../images/default.png" width = "100%">

# - - - 

# Problem3:
# insert an image in the Python cell

# In[1]:


from IPython import display
display.Image("../images/default.png")


# **NOTE**

# - Using % of slide to scale the image

# - - - 

# **2)Left Bullets and image**

# # Title

# **BODY**

# <table>
#   <tr>
# 
#    <td width=“100%“>
#          
# Here is a **left column**: 
# - Something about figure
# - Something else about it
# - a long description
#           
#     </td>
#       <td>
# <img align="right" src="../images/default.png">
#     </td>
#     </tr>
# </table>

# **NOTE**

# - A simple example that has bullets on left of figure while using markdown
# 

# - - - 

# **2)Two Column Bullets**

# # Two Column texts display 

# <table>
# <tr>
#    <td>   
#        
#        
# **Left Column:** 
# - Use two `Enter` to add two empty lines in front of the text to make a paragraph
#        
#     </td>
#    <td> 
# 
#        
# **Right Column:** 
# - If you also use ```<p>``` and ```</p>``` tags to make a paragraph.
#      
#        
#     </td>
#     </tr>
# </table> 

# **NOTE**

# - Using a table to control % of slide for both parts

# - - - 

# **6)Two Column Bullets**

# #  ``` </p> ```  tag

# <table>
#     <tr>
#     <td>  
#         
#         
# If you add ``` <p> ```  and ```</p>``` tags to make a paragraph, make sure ```</p>``` close tag following closely by the texts, instead of in a seperate line.
#         
#         
#     </td> 
#     <td>
#         <p>       
# If you add  ```</p>``` tag in a seperate line if will display in the slides.
#         </p>     
#        
#     </td>
# </table> 

# **NOTE**

# - Using a table to control % of slide for both parts

# - - - 

# **3) Right Bullets and image**

# # Title

# **BODY**

# <table>
# <tr>
#    <td width="40%">
#       <img  src="../images/default.png">
#     </td>
#    <td> 
# 
# Here is a **right column**: 
# - Something about figure
# - Something else about it
# - a long description
#        
#     </td>
# </table> 

# **NOTE**

# - An example with an image on the left and bullets on the right using a two-column HTML table

# - - - 

# **3) Right Bullets and image**

# # Title

# **BODY**

# 
# <img src="../images/default.png" width="40%" style="margin:2em 1em 0em 0em" align="left" >
# 
# ### Texts on the right wrapping image on the left
# 
# **Bullet 1:** Something about figure,Something else about it, and a long description
# 
# **Bullet 2:** Something about figure,Something else about it, and a long description
# 
# **Bullet 3:** Something about figure,Something else about it, and a long description
# 
# **Bullet 4:** Something about figure,Something else about it, and a long description

# **NOTE**

# - A simple example that has texts on the right wrapping image on the left while using markdown

# - - - 

# **4)Two Column image**

# # Title

# <table>
# <tr>
#    <td width="40%">
#       <img  src="../images/default.png">
#     </td>
#    <td width="40%">
#       <img  src="../images/default.png">
#     </td>
# <tr>
#    <td>
# 
#        
# - Something about figure,or a long description
#     </td>
#    <td> 
#       <p>
# - Something about figure,or a long description with p tag.         
#                            </p>
#     </td>
#     </tr>
# </table>    
# 

# **NOTE**

# - Using a table to control % of slide for both parts with larger image

# - - - 

# **5)Bullets**

# # Title

# - **Bullet 1:** Something keypoints, and a long description
# 
# - **Bullet 2:** Something keypoints, and a long description
# 
# - **Bullet 3:** Something keypoints, and a long description
# 
# - **Bullet 4:** Something keypoints, and a long description

# **NOTE**

# - a Note that will display in the notes view

# - - - 

# **6)Two Column Bullets**

# # Title

# <table>
# <tr>
#    <td>
#        
#        
# **Left Column:** 
# - Bullet 1: Something keypoints, and a long description
# - Bullet 2: Something keypoints, and a long description
# - a long description, a long description,a long description, a long description, a long description, a long description, a long description, a long description, a long description, a long description, a long description
#     </td>
#    <td> 
# 
#        
# **Right Column:** 
# - Bullet 1: Something keypoints, and a long description
# - Bullet 2: Something keypoints, and a long description
# - a long description, a long description, a long description, a long description, a long description, a long description, a long description, a long description, a long description, a long description, a long description
#      
#        
#     </td>
#     </tr>
# </table> 

# **NOTE**

# - Using a table to control % of slide for both parts

# - - - 
