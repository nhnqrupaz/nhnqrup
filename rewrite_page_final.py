with open('src/app/page.tsx', 'r') as f:
    lines = f.readlines()

# Add import
for i, line in enumerate(lines):
    if 'import Link from "next/link";' in line:
        lines.insert(i + 1, 'import Reveal from "@/components/Reveal";\n')
        break

# We know exactly where the main inner divs for sections are, but the easiest way is:
# When we see `<section ...>`, we insert `<Reveal direction="up" delay={0.2} className="w-full">` AFTER the section opening tag.
# When we see `</section>`, we insert `</Reveal>` BEFORE it.

import re

out_lines = []
for line in lines:
    if '<section ' in line:
        out_lines.append(line)
        # Hero and Emergency CTA have specific classes that we might not want to wrap if it breaks them,
        # but w-full h-full is safe.
        out_lines.append('        <Reveal direction="up" delay={0.2} className="w-full h-full">\n')
    elif '</section>' in line:
        out_lines.append('        </Reveal>\n')
        out_lines.append(line)
    else:
        out_lines.append(line)

with open('src/app/page.tsx', 'w') as f:
    f.writelines(out_lines)

