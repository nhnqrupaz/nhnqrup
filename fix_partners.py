with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Fix heading text size
c = c.replace(
    '<h2 className="text-3xl md:text-5xl font-bold mb-4 md:mb-6 text-[#131312]">',
    '<h2 className="text-2xl md:text-4xl font-bold mb-3 md:mb-4 text-[#131312]">'
)

c = c.replace(
    '<p className="text-lg text-gray-600 leading-relaxed">',
    '<p className="text-base text-gray-600 leading-relaxed">'
)

# Fix partner boxes: remove grayscale, increase height (h-40 to h-48)
c = c.replace(
    'className="rounded-2xl overflow-hidden h-40 bg-white flex items-center justify-center border border-gray-100 hover:shadow-md transition-shadow grayscale hover:grayscale-0 p-4"',
    'className="rounded-2xl overflow-hidden h-48 bg-white flex items-center justify-center border border-gray-100 hover:shadow-md transition-shadow p-6"'
)

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

with open('src/app/admin/partners/page.tsx', 'r') as f:
    admin_c = f.read()

# Remove the 'name' input field
admin_c = admin_c.replace(
    '<div>\n            <label className="block text-sm font-medium mb-1">Şirkət Adı</label>\n            <input required type="text" value={form.name || \'\'} onChange={e => setForm({...form, name: e.target.value})} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-2" />\n          </div>',
    ''
)

# Ensure payload has a default name
admin_c = admin_c.replace(
    'const payload = { ...form };',
    'const payload = { ...form, name: form.name || \'Partnyor\' };'
)

with open('src/app/admin/partners/page.tsx', 'w') as f:
    f.write(admin_c)
