with open('src/components/CVForm.tsx', 'r') as f:
    c = f.read()

# Remove the text
c = c.replace('<p className="text-xs text-center text-gray-400 mt-4">İlk müraciət zamanı email qutunuza "FormSubmit" tərəfindən aktivasiya mesajı gedə bilər.</p>', '')

# Change names to ASCII
c = c.replace('name="Ad_və_Soyad"', 'name="Ad_Soyad"')
c = c.replace('name="Müraciət_Edilən_Sahə"', 'name="Secilen_Vezife_ve_ya_Kurs"')

with open('src/components/CVForm.tsx', 'w') as f:
    f.write(c)

