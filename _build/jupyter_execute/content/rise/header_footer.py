#!/usr/bin/env python
# coding: utf-8

# # Header & footer

# ```css   
#     {
#      ...
#      "rise": {
#          "header": "<h2>Hello</h2>",
#          "footer": "<h3>World!</h3>"
#      }
#     }
# ```

# Configure the header and footer in the notebook metadata.

# If the slide contents are so large that they cover the header and footer, you should set the "z-index" of the header and footer to a bigger value than the present slide section. 

# ```css
# div#rise-overlay, div#rise-header, div#rise-footer{
#     z-index: 20;
# }
# ```

# In our case, set ["z-index"](./rise.css#L138) of the header and footer to 20, since "z-index" of "stack present" is 11 and chalkboard buttons' value is 30.

# ## Simple approach
# 
# Copy the [rise.css](./rise.css) to the target notebook file. 

# ## Alternatively
# 
# Copy the module to the custom CSS with the same name as the target notebook file. 

# ```css
# div#rise-overlay, div#rise-header, div#rise-footer{
#     z-index: 20;
# }
# ```

# # Slide 1

# Here we have defined `header`, `footer` and `backimage` - [see also the customization doc](https://rise.readthedocs.io/en/latest/customize.html#header-footer-and-backimage).

# # Slide 2

# See [config option overlay](https://rise.readthedocs.io/en/latest/customize.html#overlay) for a short description of how to use `overlay` instead. 
