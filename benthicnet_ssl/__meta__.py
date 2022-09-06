# `name` is the name of the package as used for `pip install package`
name = "benthicnet-ssl"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1.dev0"
author = "Shakhboz Abdulazizov"
author_email = "sh873370@dal.ca"
description = "Different SSL methods trained on BenthicNet data"  # One-liner
url = ""  # your project homepage
license = "MIT"  # See https://choosealicense.com
