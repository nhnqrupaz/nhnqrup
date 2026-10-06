with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Add import
content = content.replace('import Link from "next/link";', 'import Link from "next/link";\nimport Reveal from "@/components/Reveal";')

# Hero
old_hero = '<div className="relative z-10 max-w-3xl text-white">'
new_hero = '<Reveal delay={0.2} direction="up">\n        <div className="relative z-10 max-w-3xl text-white">'
content = content.replace(old_hero, new_hero)
content = content.replace('</div>\n      </section>\n\n      {/* Stats Section */}', '</div>\n        </Reveal>\n      </section>\n\n      {/* Stats Section */}')

# Stats
old_stats = '<div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">'
new_stats = '<Reveal delay={0.1} direction="up" className="w-full">\n        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">'
content = content.replace(old_stats, new_stats)
content = content.replace('</div>\n      </section>\n\n      {/* Services Section */}', '</div>\n        </Reveal>\n      </section>\n\n      {/* Services Section */}')

# Services Intro
old_srv_intro = '<div className="mb-16 max-w-2xl">'
new_srv_intro = '<Reveal direction="up" delay={0.1}>\n          <div className="mb-16 max-w-2xl">'
content = content.replace(old_srv_intro, new_srv_intro, 1)

old_srv_intro_close = '</p>\n          </div>\n\n          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">'
new_srv_intro_close = '</p>\n          </div>\n          </Reveal>\n\n          <Reveal direction="up" delay={0.2}>\n          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">'
content = content.replace(old_srv_intro_close, new_srv_intro_close, 1)

old_srv_close = '</a>\n            </div>\n          </div>\n        </div>\n      </section>\n      {/* Why Choose Us Section */}'
new_srv_close = '</a>\n            </div>\n          </div>\n          </Reveal>\n        </div>\n      </section>\n      {/* Why Choose Us Section */}'
content = content.replace(old_srv_close, new_srv_close, 1)

# Why choose us
old_why_intro = '<div className="mb-16 max-w-3xl">'
new_why_intro = '<Reveal direction="up">\n          <div className="mb-16 max-w-3xl">'
content = content.replace(old_why_intro, new_why_intro)

old_why_intro_close = '</p>\n          </div>\n\n          <div className="grid lg:grid-cols-3 gap-6 w-full">'
new_why_intro_close = '</p>\n          </div>\n          </Reveal>\n\n          <Reveal direction="up" delay={0.2}>\n          <div className="grid lg:grid-cols-3 gap-6 w-full">'
content = content.replace(old_why_intro_close, new_why_intro_close)

old_why_close = '</div>\n          </div>\n        </div>\n      </section>\n\n      {/* Video Block */}'
new_why_close = '</div>\n          </div>\n          </Reveal>\n        </div>\n      </section>\n\n      {/* Video Block */}'
content = content.replace(old_why_close, new_why_close)

# Video Block
old_video = '<div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">'
new_video = '<Reveal direction="up" delay={0.1} className="w-full">\n        <div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">'
content = content.replace(old_video, new_video)

old_video_close = '</div>\n      </section>\n\n      {/* How It Works Section */}'
new_video_close = '</div>\n        </Reveal>\n      </section>\n\n      {/* How It Works Section */}'
content = content.replace(old_video_close, new_video_close)

# How it works
old_hw_intro = '<div className="mb-16">'
new_hw_intro = '<Reveal direction="up">\n          <div className="mb-16">'
content = content.replace(old_hw_intro, new_hw_intro, 1)

old_hw_intro_close = '</p>\n          </div>\n\n          <div className="grid md:grid-cols-4 gap-8 relative">'
new_hw_intro_close = '</p>\n          </div>\n          </Reveal>\n\n          <Reveal direction="up" delay={0.2}>\n          <div className="grid md:grid-cols-4 gap-8 relative">'
content = content.replace(old_hw_intro_close, new_hw_intro_close, 1)

old_hw_close = '</div>\n          </div>\n        </div>\n      </section>\n\n      {/* Emergency CTA */}'
new_hw_close = '</div>\n          </div>\n          </Reveal>\n        </div>\n      </section>\n\n      {/* Emergency CTA */}'
content = content.replace(old_hw_close, new_hw_close, 1)

# Emergency CTA
old_cta = '<div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">'
new_cta = '<Reveal direction="up" className="w-full">\n        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">'
content = content.replace(old_cta, new_cta)

old_cta_close = '</div>\n      </section>\n\n      {/* Featured Projects Section */}'
new_cta_close = '</div>\n        </Reveal>\n      </section>\n\n      {/* Featured Projects Section */}'
content = content.replace(old_cta_close, new_cta_close)

# Featured Projects
old_feat_intro = '<div className="mb-16 max-w-2xl">'
new_feat_intro = '<Reveal direction="up">\n          <div className="mb-16 max-w-2xl">'
content = content.replace(old_feat_intro, new_feat_intro)

old_feat_intro_close = '</p>\n          </div>\n          \n          <div className="grid md:grid-cols-3 gap-6">'
new_feat_intro_close = '</p>\n          </div>\n          </Reveal>\n          \n          <Reveal direction="up" delay={0.2}>\n          <div className="grid md:grid-cols-3 gap-6">'
content = content.replace(old_feat_intro_close, new_feat_intro_close)

old_feat_close = '</div>\n        </div>\n      </section>\n\n      {/* Footer */}'
new_feat_close = '</div>\n          </Reveal>\n        </div>\n      </section>\n\n      {/* Footer */}'
content = content.replace(old_feat_close, new_feat_close)


with open('src/app/page.tsx', 'w') as f:
    f.write(content)

