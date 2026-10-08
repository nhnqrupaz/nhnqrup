import os

files_to_fix = [
    'src/app/page.tsx',
    'src/app/courses/page.tsx',
    'src/app/vacancies/page.tsx',
    'src/app/products/page.tsx',
    'src/app/products/[id]/page.tsx'
]

dynamic_statement = "export const dynamic = 'force-dynamic';\nexport const revalidate = 0;\n\n"

for path in files_to_fix:
    if not os.path.exists(path):
        continue
    with open(path, 'r') as f:
        content = f.read()
    
    if "export const dynamic = 'force-dynamic';" not in content:
        # We'll just prepend it right after imports, or at the very top.
        # Safest is at the very top, but sometimes it conflicts with "use client".
        # None of these should be "use client" now because I made them server components.
        content = dynamic_statement + content
        with open(path, 'w') as f:
            f.write(content)

