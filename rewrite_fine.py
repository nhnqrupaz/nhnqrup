import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Remove the section-level reveals
content = content.replace('        <Reveal direction="up" delay={0.2} className="w-full h-full">\n', '')
content = content.replace('        </Reveal>\n      </section>', '      </section>')

# Now wrap specific elements in Reveal

# 1. Hero text
content = content.replace(
    '<h1 className="text-5xl md:text-7xl font-bold leading-[1.1] mb-6">',
    '<Reveal direction="up" delay={0.1}>\n          <h1 className="text-5xl md:text-7xl font-bold leading-[1.1] mb-6">'
)
content = content.replace(
    'Solutions You Can Trust\n          </h1>',
    'Solutions You Can Trust\n          </h1>\n          </Reveal>'
)

content = content.replace(
    '<p className="text-lg md:text-xl text-white/90 mb-10 max-w-2xl leading-relaxed">',
    '<Reveal direction="up" delay={0.2}>\n          <p className="text-lg md:text-xl text-white/90 mb-10 max-w-2xl leading-relaxed">'
)
content = content.replace(
    'same-day service.\n          </p>',
    'same-day service.\n          </p>\n          </Reveal>'
)

# 2. Stats
# <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">
# Contains 4 <div>s
content = content.replace(
    '<div>\n            <div className="text-5xl font-bold mb-2">10+</div>',
    '<Reveal direction="up" delay={0.1}>\n          <div>\n            <div className="text-5xl font-bold mb-2">10+</div>'
)
content = content.replace(
    '<div>\n            <div className="text-5xl font-bold mb-2">2.5k+</div>',
    '<Reveal direction="up" delay={0.2}>\n          <div>\n            <div className="text-5xl font-bold mb-2">2.5k+</div>'
)
content = content.replace(
    '<div>\n            <div className="text-5xl font-bold mb-2">98%</div>',
    '<Reveal direction="up" delay={0.3}>\n          <div>\n            <div className="text-5xl font-bold mb-2">98%</div>'
)
content = content.replace(
    '<div>\n            <div className="text-5xl font-bold mb-2">24/7</div>',
    '<Reveal direction="up" delay={0.4}>\n          <div>\n            <div className="text-5xl font-bold mb-2">24/7</div>'
)

# Add closing </Reveal> for the 4 stat divs
content = re.sub(r'(<div className="text-white/90">[^<]+</div>\n          )</div>', r'\1</div>\n          </Reveal>', content)


# 3. Section Titles (Our Services, Why Choose Us, How it Works, Featured Projects)
content = content.replace(
    '<div className="mb-16 max-w-2xl">',
    '<Reveal direction="up" delay={0.1}>\n          <div className="mb-16 max-w-2xl">'
)
content = content.replace(
    '<div className="mb-16 max-w-3xl">',
    '<Reveal direction="up" delay={0.1}>\n          <div className="mb-16 max-w-3xl">'
)
content = content.replace(
    '<div className="mb-16">',
    '<Reveal direction="up" delay={0.1}>\n          <div className="mb-16">'
)

content = content.replace(
    'home or business.\n            </p>\n          </div>',
    'home or business.\n            </p>\n          </div>\n          </Reveal>'
)
content = content.replace(
    'services you can trust.\n            </p>\n          </div>',
    'services you can trust.\n            </p>\n          </div>\n          </Reveal>'
)
content = content.replace(
    'transparent, and hassle-free.\n            </p>\n          </div>',
    'transparent, and hassle-free.\n            </p>\n          </div>\n          </Reveal>'
)
content = content.replace(
    'delivered with care and precision.\n            </p>\n          </div>',
    'delivered with care and precision.\n            </p>\n          </div>\n          </Reveal>'
)

# 4. Service Cards
content = content.replace(
    '{/* Card 1 */}\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group">',
    '{/* Card 1 */}\n            <Reveal direction="up" delay={0.2} className="h-full">\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">'
)
content = content.replace(
    '{/* Card 2 */}\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group">',
    '{/* Card 2 */}\n            <Reveal direction="up" delay={0.3} className="h-full">\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">'
)
content = content.replace(
    '{/* Card 3 */}\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group">',
    '{/* Card 3 */}\n            <Reveal direction="up" delay={0.4} className="h-full">\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">'
)
content = content.replace(
    '{/* Card 4 */}\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group">',
    '{/* Card 4 */}\n            <Reveal direction="up" delay={0.2} className="h-full">\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">'
)
content = content.replace(
    '{/* Card 5 */}\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group">',
    '{/* Card 5 */}\n            <Reveal direction="up" delay={0.3} className="h-full">\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">'
)
content = content.replace(
    '{/* Card 6 */}\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group">',
    '{/* Card 6 */}\n            <Reveal direction="up" delay={0.4} className="h-full">\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">'
)

content = content.replace(
    '</span>\n              </a>\n            </div>',
    '</span>\n              </a>\n            </div>\n            </Reveal>'
)

# 5. Why Choose Us Grid
content = content.replace(
    '{/* Left Cards */}\n            <div className="flex flex-col gap-6">',
    '{/* Left Cards */}\n            <Reveal direction="left" delay={0.2}>\n            <div className="flex flex-col gap-6 h-full">'
)
content = content.replace(
    'delays or disruptions.\n                </p>\n              </div>\n            </div>',
    'delays or disruptions.\n                </p>\n              </div>\n            </div>\n            </Reveal>'
)
content = content.replace(
    '{/* Middle Image */}\n            <div className="rounded-3xl overflow-hidden h-[600px] lg:h-auto relative">',
    '{/* Middle Image */}\n            <Reveal direction="up" delay={0.3}>\n            <div className="rounded-3xl overflow-hidden h-[600px] lg:h-auto relative">'
)
content = content.replace(
    'className="w-full h-full object-cover"\n              />\n            </div>',
    'className="w-full h-full object-cover"\n              />\n            </div>\n            </Reveal>'
)
content = content.replace(
    '{/* Right Cards */}\n            <div className="flex flex-col gap-6">',
    '{/* Right Cards */}\n            <Reveal direction="right" delay={0.4}>\n            <div className="flex flex-col gap-6 h-full">'
)
content = content.replace(
    'assistance whenever needed.\n                </p>\n              </div>\n            </div>\n          </div>',
    'assistance whenever needed.\n                </p>\n              </div>\n            </div>\n            </Reveal>\n          </div>'
)

# 6. Video
content = content.replace(
    '<div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">',
    '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">'
)
content = content.replace(
    'className="text-[#ff4f14]" />\n            </div>\n          </div>\n        </div>',
    'className="text-[#ff4f14]" />\n            </div>\n          </div>\n        </div>\n        </Reveal>'
)

# 7. How it works Grid
content = content.replace(
    '{/* Step 1 */}\n            <div className="relative z-10 flex flex-col items-center">',
    '{/* Step 1 */}\n            <Reveal direction="up" delay={0.2}>\n            <div className="relative z-10 flex flex-col items-center">'
)
content = content.replace(
    '{/* Step 2 */}\n            <div className="relative z-10 flex flex-col items-center">',
    '{/* Step 2 */}\n            <Reveal direction="up" delay={0.3}>\n            <div className="relative z-10 flex flex-col items-center">'
)
content = content.replace(
    '{/* Step 3 */}\n            <div className="relative z-10 flex flex-col items-center">',
    '{/* Step 3 */}\n            <Reveal direction="up" delay={0.4}>\n            <div className="relative z-10 flex flex-col items-center">'
)
content = content.replace(
    '{/* Step 4 */}\n            <div className="relative z-10 flex flex-col items-center">',
    '{/* Step 4 */}\n            <Reveal direction="up" delay={0.5}>\n            <div className="relative z-10 flex flex-col items-center">'
)
content = content.replace(
    'give us a call.\n              </p>\n            </div>',
    'give us a call.\n              </p>\n            </div>\n            </Reveal>'
)
content = content.replace(
    'explains the solution.\n              </p>\n            </div>',
    'explains the solution.\n              </p>\n            </div>\n            </Reveal>'
)
content = content.replace(
    'proven techniques.\n              </p>\n            </div>',
    'proven techniques.\n              </p>\n            </div>\n            </Reveal>'
)
content = content.replace(
    'reliable service.\n              </p>\n            </div>',
    'reliable service.\n              </p>\n            </div>\n            </Reveal>'
)

# 8. Emergency CTA
content = content.replace(
    '<div className="max-w-2xl mb-8 md:mb-0">',
    '<Reveal direction="left" delay={0.2}>\n          <div className="max-w-2xl mb-8 md:mb-0">'
)
content = content.replace(
    'CALL NOW\n              <ArrowRight size={20} />\n            </button>\n          </div>',
    'CALL NOW\n              <ArrowRight size={20} />\n            </button>\n          </div>\n          </Reveal>'
)
content = content.replace(
    '<div className="relative w-72 h-72 hidden md:block">',
    '<Reveal direction="right" delay={0.4}>\n          <div className="relative w-72 h-72 hidden md:block">'
)
content = content.replace(
    'className="w-full h-full object-cover rounded-full border-8 border-[#ff4f14]"\n            />\n          </div>',
    'className="w-full h-full object-cover rounded-full border-8 border-[#ff4f14]"\n            />\n          </div>\n          </Reveal>'
)

# 9. Featured Projects grid
content = content.replace(
    '<div className="rounded-3xl overflow-hidden h-80 group relative">',
    '<Reveal direction="up" delay={0.2} className="h-full">\n            <div className="rounded-3xl overflow-hidden h-80 group relative">'
)
# Match closing of those 3 blocks.
content = re.sub(r'(<img src="[^"]+" alt="Project \d" className="[^"]+" />\n            )</div>', r'\1</div>\n            </Reveal>', content)


with open('src/app/page.tsx', 'w') as f:
    f.write(content)

