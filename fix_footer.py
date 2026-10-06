with open('src/components/Footer.tsx', 'r') as f:
    c = f.read()

c = c.replace('href="#" className="hover:text-white transition-colors">İstifadə qaydaları', 'href="/terms" className="hover:text-white transition-colors">İstifadə qaydaları')
# Also add Məxfilik siyasəti
# Let's see the list:
# <li><Link href="/contact" className="hover:text-white transition-colors">Əlaqə</Link></li>
# <li><Link href="#" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>
# I will change it to:
old_links = '<li><Link href="/contact" className="hover:text-white transition-colors">Əlaqə</Link></li>\n            <li><Link href="#" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>'
new_links = '<li><Link href="/contact" className="hover:text-white transition-colors">Əlaqə</Link></li>\n            <li><Link href="/terms" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>\n            <li><Link href="/privacy" className="hover:text-white transition-colors">Məxfilik siyasəti</Link></li>'

if old_links in c:
    c = c.replace(old_links, new_links)
else:
    c = c.replace('href="/terms" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>', 'href="/terms" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>\n            <li><Link href="/privacy" className="hover:text-white transition-colors">Məxfilik siyasəti</Link></li>')

with open('src/components/Footer.tsx', 'w') as f:
    f.write(c)

