import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Remove from lucide-react
content = content.replace(',\n  Instagram,\n  Facebook,\n  Linkedin', '')
content = content.replace('  Instagram,\n  Facebook,\n  Linkedin\n} from "lucide-react";', '} from "lucide-react";')

# Add import for react-icons
content = content.replace('import Reveal from "@/components/Reveal";', 'import Reveal from "@/components/Reveal";\nimport { FaInstagram, FaFacebook, FaLinkedin } from "react-icons/fa";')

# Update tags in footer
content = content.replace('<Instagram size={24} />', '<FaInstagram size={24} />')
content = content.replace('<Facebook size={24} />', '<FaFacebook size={24} />')
content = content.replace('<Linkedin size={24} />', '<FaLinkedin size={24} />')

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

