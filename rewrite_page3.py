with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Add import
content = content.replace('import Link from "next/link";', 'import Link from "next/link";\nimport Reveal from "@/components/Reveal";')

# Wrap everything inside <section> tags with <Reveal direction="up" delay={0.1} className="w-full h-full"> ... </Reveal>
# Wait, this might break layout if not careful, but Reveal renders a motion.div which defaults to block display.
import re
def section_replacer(match):
    section_open = match.group(1)
    inner_html = match.group(2)
    section_close = match.group(3)
    
    # Don't double wrap if already wrapped
    if "<Reveal" in inner_html:
        return match.group(0)
        
    return f'{section_open}\n        <Reveal direction="up" delay={{0.1}} className="w-full h-full">\n{inner_html}\n        </Reveal>\n{section_close}'

# We need a regex to match sections. Since sections don't nest here:
pattern = re.compile(r'(<section[^>]*>)(.*?)(</section>)', re.DOTALL)
content = pattern.sub(section_replacer, content)

# Wrap hero content (which is not just the whole section, actually hero section is fine to wrap entirely)
# Wait, hero has an absolute background image! If we wrap the whole hero section inner content in a single relative Reveal div, the background image will be blurred and animated, and it will scroll in. This is exactly what "heavy animations" and "blur" means!

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

