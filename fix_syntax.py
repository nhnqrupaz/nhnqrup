with open('src/app/page.tsx', 'r') as f:
    c = f.read()

c = c.replace('          />\n          </div>\n        </div>\n        </Reveal>', '          />\n        </div>\n        </Reveal>')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

