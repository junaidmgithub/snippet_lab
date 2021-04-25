class Template:
    def __init__(self, path):
        with open(path) as f:
            self.text = f.read()

    def render(self, **kwargs):
        return self.text.format(**kwargs)

# Usage
t = Template('sample.html')
template = t.render(first_name="hello", last_name="world")
print(template)
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
hello
world
</body>
</html>"""
