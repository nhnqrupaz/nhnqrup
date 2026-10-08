with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Fix partners
old_partners_block = """          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map((i) => (
              <Reveal key={i} direction="up" delay={0.2 + (i * 0.1)} className="h-full">
                <div className="rounded-2xl overflow-hidden h-40 bg-gray-100 flex items-center justify-center border border-gray-200 hover:shadow-md transition-shadow">
                  {/* Empty placeholder for partner logo */}
                  <span className="text-gray-400 font-medium">Partnyor Logo</span>
                </div>
              </Reveal>
            ))}
          </div>"""

new_partners_block = """          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-6">
            {(partners || []).map((p: any, i: number) => (
              <Reveal key={p.id} direction="up" delay={0.2 + (i * 0.1)} className="h-full">
                <div className="rounded-2xl overflow-hidden h-40 bg-white flex items-center justify-center border border-gray-100 hover:shadow-md transition-shadow grayscale hover:grayscale-0 p-4">
                  <img src={p.logo_url} alt={p.name} loading="lazy" className="max-w-full max-h-full object-contain" />
                </div>
              </Reveal>
            ))}
            {(!partners || partners.length === 0) && (
              <div className="col-span-full text-center text-gray-500 py-8 border-2 border-dashed border-gray-200 rounded-2xl">
                Hələ partnyor əlavə edilməyib.
              </div>
            )}
          </div>"""

c = c.replace(old_partners_block, new_partners_block)

# Fast loading for Hero
c = c.replace(
    'alt="Hero Background" \n            className="w-full h-full object-cover"',
    'alt="Hero Background" \n            className="w-full h-full object-cover"\n            loading="eager"\n            fetchPriority="high"'
)

# Fast loading for CTA
c = c.replace(
    'alt="Praktiki Dərslər" \n            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"',
    'alt="Praktiki Dərslər" \n            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"\n            loading="lazy"'
)

with open('src/app/page.tsx', 'w') as f:
    f.write(c)
