with open('src/components/CVForm.tsx', 'r') as f:
    c = f.read()

c = c.replace(
    '<input type="hidden" name="_subject" value="YENİ CV MÜRACİƏTİ (Saytdan)" />',
    '<input type="hidden" name="_subject" value={job ? `Yeni Müraciət: ${job}` : "Yeni CV Müraciəti (Saytdan)"} />'
)

with open('src/components/CVForm.tsx', 'w') as f:
    f.write(c)
