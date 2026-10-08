with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Replace hardcoded Unsplash why_us with setting
c = c.replace(
    'src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=800&auto=format&fit=crop"',
    'src={settings?.why_us_image_url || "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=800&auto=format&fit=crop"}'
)

# Replace hardcoded Unsplash urgent with setting
c = c.replace(
    'src="https://images.unsplash.com/photo-1574739782594-db4ead022697?q=80&w=600&auto=format&fit=crop"',
    'src={settings?.urgent_image_url || "https://images.unsplash.com/photo-1574739782594-db4ead022697?q=80&w=600&auto=format&fit=crop"}'
)

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

