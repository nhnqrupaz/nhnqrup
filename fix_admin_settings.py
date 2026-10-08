with open('src/app/admin/page.tsx', 'r') as f:
    c = f.read()

# Add states
c = c.replace(
    "const [ctaImage, setCtaImage] = useState('');",
    "const [ctaImage, setCtaImage] = useState('');\n  const [whyUsImage, setWhyUsImage] = useState('');\n  const [urgentImage, setUrgentImage] = useState('');"
)

# Fetch settings
c = c.replace(
    "setCtaImage(data.cta_image_url || '');",
    "setCtaImage(data.cta_image_url || '');\n        setWhyUsImage(data.why_us_image_url || '');\n        setUrgentImage(data.urgent_image_url || '');"
)

# Save settings
c = c.replace(
    ".upsert({ id: 1, hero_image_url: heroImage, cta_image_url: ctaImage, updated_at: new Date().toISOString() });",
    ".upsert({ id: 1, hero_image_url: heroImage, cta_image_url: ctaImage, why_us_image_url: whyUsImage, urgent_image_url: urgentImage, updated_at: new Date().toISOString() });"
)

# UI additions
ui_addition = """
        <hr className="border-gray-100" />

        {/* Why Us Image */}
        <div>
          <label className="block text-sm font-bold text-gray-700 mb-2">Niyə Bizi Seçməlisiniz (Orta Şəkil)</label>
          {whyUsImage && (
            <img src={whyUsImage} alt="Why Us" className="w-full h-48 object-cover rounded-xl mb-4" />
          )}
          <label className="flex items-center gap-2 bg-gray-50 border border-gray-200 px-4 py-3 rounded-xl cursor-pointer hover:bg-gray-100 transition-colors">
            <Upload size={20} className="text-gray-500" />
            <span className="text-gray-600 font-medium">Yeni şəkil seç və yüklə</span>
            <input type="file" className="hidden" accept="image/*" onChange={e => handleUpload(e, setWhyUsImage)} />
          </label>
        </div>

        <hr className="border-gray-100" />

        {/* Urgent Image */}
        <div>
          <label className="block text-sm font-bold text-gray-700 mb-2">Təcili Xidmət Şəkli (Dairəvi Şəkil)</label>
          {urgentImage && (
            <img src={urgentImage} alt="Urgent" className="w-48 h-48 object-cover rounded-full mx-auto border-8 border-gray-100 mb-4" />
          )}
          <label className="flex items-center gap-2 bg-gray-50 border border-gray-200 px-4 py-3 rounded-xl cursor-pointer hover:bg-gray-100 transition-colors">
            <Upload size={20} className="text-gray-500" />
            <span className="text-gray-600 font-medium">Yeni şəkil seç və yüklə</span>
            <input type="file" className="hidden" accept="image/*" onChange={e => handleUpload(e, setUrgentImage)} />
          </label>
        </div>
"""

c = c.replace(
    '        </div>\n\n      </div>',
    '        </div>\n' + ui_addition + '\n      </div>'
)

with open('src/app/admin/page.tsx', 'w') as f:
    f.write(c)

