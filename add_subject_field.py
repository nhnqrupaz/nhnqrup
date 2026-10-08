with open('src/components/CVForm.tsx', 'r') as f:
    c = f.read()

# Add the 'Mövzu' field right after Email
new_field = """      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">E-poçt (istəyə bağlı)</label>
        <input type="email" name="Email" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="E-poçt ünvanınız" />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Mövzu</label>
        <input required type="text" name="Movzu" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="Müraciətinizin mövzusu (məs: İşə qəbul, Təcrübə proqramı və s.)" />
      </div>"""

c = c.replace("""      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">E-poçt (istəyə bağlı)</label>
        <input type="email" name="Email" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="E-poçt ünvanınız" />
      </div>""", new_field)

with open('src/components/CVForm.tsx', 'w') as f:
    f.write(c)

