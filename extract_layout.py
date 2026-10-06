import re
import os

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Extract header
header_match = re.search(r'(<header.*?</header>)', content, re.DOTALL)
header_str = header_match.group(1)

# Extract footer
footer_match = re.search(r'(      {/\* Footer \*/}\n      <footer.*?</footer>)', content, re.DOTALL)
footer_str = footer_match.group(1)

# Create Header.tsx
os.makedirs('src/components', exist_ok=True)
with open('src/components/Header.tsx', 'w') as f:
    f.write('\'use client\';\nimport Link from "next/link";\nexport default function Header() {\n  return (\n')
    f.write(header_str)
    f.write('\n  );\n}\n')

# Create Footer.tsx
with open('src/components/Footer.tsx', 'w') as f:
    f.write('\'use client\';\nimport Link from "next/link";\nimport { FaInstagram } from "react-icons/fa";\nexport default function Footer() {\n  return (\n')
    f.write(footer_str)
    f.write('\n  );\n}\n')

# Remove from page.tsx and add components
content = content.replace(header_str, '<Header />')
content = content.replace(footer_str, '<Footer />')

# Fix imports in page.tsx
content = content.replace('import Reveal from "@/components/Reveal";', 'import Reveal from "@/components/Reveal";\nimport Header from "@/components/Header";\nimport Footer from "@/components/Footer";')

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

