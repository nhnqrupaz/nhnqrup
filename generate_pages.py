pages = {
    'products': 'Məhsullar',
    'services': 'Xidmətlər',
    'courses': 'Kurslar',
    'vacancies': 'Vakansiyalar',
    'cv': 'CV Göndər',
    'contact': 'Əlaqə',
    'about': 'Haqqımızda'
}

template = """export default function Page() {
  return (
    <div className="flex flex-col min-h-[70vh] bg-[#f8f9f8] pt-40 px-6 lg:px-20 items-center justify-center">
      <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-[#131312] mb-6">
        {title}
      </h1>
      <p className="text-lg text-gray-600">Bu səhifə tezliklə məlumatlarla doldurulacaq.</p>
    </div>
  );
}
"""

for path, title in pages.items():
    with open(f'src/app/{path}/page.tsx', 'w') as f:
        f.write(template.replace('{title}', title))

