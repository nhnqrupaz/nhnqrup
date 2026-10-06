import re

with open('src/app/layout.tsx', 'r') as f:
    content = f.read()

# Add imports for Header and Footer
content = content.replace('import SmoothScroll from "@/components/SmoothScroll";', 'import SmoothScroll from "@/components/SmoothScroll";\nimport Header from "@/components/Header";\nimport Footer from "@/components/Footer";')

# Wrap children with Header and Footer
content = content.replace(
    '<SmoothScroll>{children}</SmoothScroll>',
    '<SmoothScroll>\n          <Header />\n          {children}\n          <Footer />\n        </SmoothScroll>'
)

with open('src/app/layout.tsx', 'w') as f:
    f.write(content)

# Now remove Header, Footer, and the global motion wrapper from page.tsx
with open('src/app/page.tsx', 'r') as f:
    page_content = f.read()

page_content = page_content.replace('import Header from "@/components/Header";\nimport Footer from "@/components/Footer";\n', '')
page_content = page_content.replace('<Header />\n', '')
page_content = page_content.replace('<Footer />\n', '')

# Remove the motion wrapper I added earlier in page.tsx
page_content = page_content.replace(
    '<motion.div \n      initial={{ opacity: 0 }}\n      animate={{ opacity: 1 }}\n      transition={{ duration: 1.2 }}\n      className="flex flex-col min-h-screen bg-[#f8f9f8]"\n    >',
    '<div className="flex flex-col min-h-screen bg-[#f8f9f8]">'
)
page_content = page_content.replace(
    '    </motion.div>\n  );\n}',
    '    </div>\n  );\n}'
)

with open('src/app/page.tsx', 'w') as f:
    f.write(page_content)

