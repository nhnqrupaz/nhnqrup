with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Remove use client
c = c.replace('"use client";\n', '')

# Add supabase import
if 'import { supabase }' not in c:
    c = c.replace('import Image from "next/image";', 'import Image from "next/image";\nimport { supabase } from "@/lib/supabase";')

# Make Home async and fetch data
c = c.replace('export default function Home() {', 'export default async function Home() {\n  const { data: settings } = await supabase.from(\'settings\').select(\'*\').eq(\'id\', 1).single();\n  const { data: partners } = await supabase.from(\'partners\').select(\'*\');\n\n  const heroImg = settings?.hero_image_url || "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=3270&auto=format&fit=crop";\n  const ctaImg = settings?.cta_image_url || "https://images.unsplash.com/photo-1542013936693-884638332954?q=80&w=1600&auto=format&fit=crop";\n')

# Replace Hero image url
old_hero_img = """<img 
            src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=3270&auto=format&fit=crop" 
            alt="Hero Background" 
            className="w-full h-full object-cover"
          />"""
new_hero_img = """<img 
            src={heroImg} 
            alt="Hero Background" 
            className="w-full h-full object-cover"
          />"""
c = c.replace(old_hero_img, new_hero_img)

# Replace CTA image url
old_cta_img = """<img 
            src="https://images.unsplash.com/photo-1542013936693-884638332954?q=80&w=1600&auto=format&fit=crop" 
            alt="Praktiki Dərslər" 
            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
          />"""
new_cta_img = """<img 
            src={ctaImg} 
            alt="Praktiki Dərslər" 
            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
          />"""
c = c.replace(old_cta_img, new_cta_img)

# Replace Partners map
old_partners = """          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map((i) => (
              <Reveal key={i} direction="up" delay={0.1 + (i * 0.1)}>
                <div className="bg-gray-50 border border-gray-100 h-32 rounded-2xl flex items-center justify-center hover:shadow-md transition-shadow grayscale hover:grayscale-0">
                  {/* Empty placeholder for partner logo */}
                  <span className="text-gray-400 font-medium">Partnyor Logo</span>
                </div>
                </Reveal>
            ))}
          </div>"""

new_partners = """          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-6">
            {(partners || []).map((p: any, i: number) => (
              <Reveal key={p.id} direction="up" delay={0.1 + (i * 0.1)}>
                <div className="bg-gray-50 border border-gray-100 h-32 rounded-2xl flex items-center justify-center hover:shadow-md transition-shadow grayscale hover:grayscale-0 p-4">
                  <img src={p.logo_url} alt={p.name} className="max-w-full max-h-full object-contain" />
                </div>
              </Reveal>
            ))}
            {(!partners || partners.length === 0) && (
              <div className="col-span-full text-center text-gray-500 py-8">Hələ partnyor əlavə edilməyib.</div>
            )}
          </div>"""
c = c.replace(old_partners, new_partners)

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

