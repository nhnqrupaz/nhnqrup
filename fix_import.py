import re
with open('src/app/page.tsx', 'r') as f:
    c = f.read()

c = re.sub(r'(import {.*?)(, \n  Phone,)', r'\1, Briefcase\2', c, flags=re.DOTALL)
if 'Briefcase' not in c: # fallback
    c = c.replace('Lightbulb,', 'Lightbulb, Briefcase,')
with open('src/app/page.tsx', 'w') as f:
    f.write(c)

