# modules is a containing code return by somebody

# Type of modules
# 1 - Flask - use to build web apps
# 2 - Django - It is also a __package

# We can install this modules using PIP
# ex - pip install module_name

import pyjokes

joke = pyjokes.get_joke()
print(joke)

