#!/usr/bin/env python
# coding: utf-8

# # Toggle RISE Buttons

# ### Press ```m```  or ```,``` to toggle rise buttons

# <table>
# <tr>
#    <td width="40%">
#       <img  src="../images/buttons_show.png">
#     </td>
#    <td> 
#    <td width="100%">
#       <img  src="../images/buttons_hide.png">
#     </td>

# We can set show buttons when starting.

# ```css
# "show_buttons_on_startup": true
# ```

# ### fix the toggle RISE buttons function

# In line 847 in
# 
#     RISE/packages/application/src/plugins/rise.ts

# ```javascript
#    element.style.visibility === 'true' ? 'false' : 'true';
# ```

# Change to

# ```javascript
# function toggleAllRiseButtons() {
#    for (const selector of ['#help_b', '#toggle-chalkboard', '#toggle-notes']) {
#      const element = document.querySelector(selector) as HTMLElement | null;
#      if (element) {
#        element.style.visibility =
#          element.style.visibility === 'hidden' ? 'visible' : 'hidden';
#      }
#    }
#  }
# ```

# ### Add keyboard ```m``` to toggle rise buttons

# If you want to bind shortcuts like `m` to hide/show buttons, you should add the key binding in line 959 in
# 
#     RISE/packages/application/src/plugins/rise.ts

# ```javascript
#     77: toggleAllRiseButtons,
# ```

# ### Modify keyboard instructions in shortcuts help page

# In line 1111
# 
#     RISE/packages/application/src/plugins/rise.ts

# ```html
#     <li><kbd>${CommandRegistry.formatKeystroke('m')} or ${CommandRegistry.formatKeystroke(',')}</kbd>: ${
#         helpStrings[CommandIDs.riseToggleAllButtons]}
#     </li>
# ```
