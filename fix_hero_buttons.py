with open('src/app/page.tsx', 'r') as f:
    c = f.read()

c = c.replace('Get Your Free Quote', 'Kurslara Yazıl')
c = c.replace('Call Now', 'Bizə Zəng Edin')
c = c.replace('From Your Call to <span className="text-[#ff4f14]">Problem Solved</span>', 'Peşəkar <span className="text-[#ff4f14]">Həll Yolları</span>')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

