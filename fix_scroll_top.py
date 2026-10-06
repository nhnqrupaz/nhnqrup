import re

with open('src/components/Header.tsx', 'r') as f:
    c = f.read()

# Change window.scrollTo to document.documentElement.scrollTo for safety, or just standard window.scrollTo(0,0)
# Lenis usually hijacks window.scrollTo. Let's just use window.scrollTo(0,0)
old_click = "window.scrollTo({ top: 0, behavior: 'smooth' });"
new_click = "window.scrollTo({ top: 0, behavior: 'smooth' }); document.body.scrollTop = 0; document.documentElement.scrollTop = 0;"

c = c.replace(old_click, new_click)

with open('src/components/Header.tsx', 'w') as f:
    f.write(c)
