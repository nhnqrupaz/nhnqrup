import re

# In vacancies
with open('src/app/vacancies/page.tsx', 'r') as f:
    c = f.read()

c = c.replace('<Link href="/cv"', '<Link href={`/cv?job=${job.title}`}')

with open('src/app/vacancies/page.tsx', 'w') as f:
    f.write(c)

# In cv page
with open('src/app/cv/page.tsx', 'r') as f:
    c = f.read()

if 'useSearchParams' not in c:
    c = c.replace('import { Upload } from "lucide-react";', 'import { Upload } from "lucide-react";\nimport { useSearchParams } from "next/navigation";\nimport { Suspense } from "react";')

    form_replacement = """
function CVForm() {
  const searchParams = useSearchParams();
  const job = searchParams.get('job') || '';

  return (
    <form className="space-y-6">
      <div className="grid md:grid-cols-2 gap-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Ad və Soyad</label>
          <input type="text" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="Adınızı daxil edin" />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Telefon</label>
          <input type="text" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="+994 -- --- -- --" />
        </div>
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">E-poçt (istəyə bağlı)</label>
        <input type="email" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="E-poçt ünvanınız" />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Müraciət etdiyiniz vəzifə</label>
        <select defaultValue={job} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]">
          <option value="">Seçin</option>
          <option value="Elektrik">Elektrik</option>
          <option value="Elektrik köməkçisi">Elektrik köməkçisi</option>
          <option value="Elektromexanik">Elektromexanik</option>
          <option value="Digər">Digər</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">CV Yüklə (PDF, DOCX)</label>
        <div className="border-2 border-dashed border-gray-300 rounded-xl p-8 flex flex-col items-center justify-center bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer group">
          <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm mb-3 group-hover:scale-110 transition-transform">
            <Upload size={20} className="text-[#ff4f14]" />
          </div>
          <span className="text-gray-500 font-medium">Faylı seçmək üçün bura vurun</span>
        </div>
      </div>
      
      <button type="button" className="w-full bg-[#131312] text-white py-4 rounded-xl font-bold hover:bg-[#ff4f14] transition-colors">
        Müraciəti Tamamla
      </button>
    </form>
  );
}
"""
    c = re.sub(r'<form className="space-y-6">.*?</form>', '<Suspense fallback={<p>Yüklənir...</p>}><CVForm /></Suspense>', c, flags=re.DOTALL)
    c += form_replacement

    with open('src/app/cv/page.tsx', 'w') as f:
        f.write(c)

