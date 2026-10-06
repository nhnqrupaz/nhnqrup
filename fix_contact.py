with open('src/app/contact/page.tsx', 'r') as f:
    c = f.read()

c = c.replace('<p className="text-gray-600">+994 77 333 44 66</p>', '<a href="https://wa.me/994773334466" target="_blank" rel="noopener noreferrer" className="text-gray-600 hover:text-[#ff4f14] transition-colors font-medium">+994 77 333 44 66</a>')
c = c.replace('<p className="text-gray-600">info@nhnqrup.az</p>', '<a href="mailto:info@nhnqrup.az" className="text-gray-600 hover:text-[#ff4f14] transition-colors font-medium">info@nhnqrup.az</a>')

with open('src/app/contact/page.tsx', 'w') as f:
    f.write(c)
