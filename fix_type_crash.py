with open('src/app/courses/page.tsx', 'r') as f:
    cc = f.read()

# Fix features map
old_features = """                  <div className="space-y-3 mb-8">
                    {course.features ? course.features.map((f: string, i: number) => (
                      <div key={i} className="flex items-center gap-3 text-gray-700">
                        <CheckIcon />
                        <span className="font-medium">{f}</span>
                      </div>
                    )) : ("""

new_features = """                  <div className="space-y-3 mb-8">
                    {course.features ? (Array.isArray(course.features) ? course.features : String(course.features).split(',')).map((f: string, i: number) => (
                      <div key={i} className="flex items-center gap-3 text-gray-700">
                        <CheckIcon />
                        <span className="font-medium">{f.trim()}</span>
                      </div>
                    )) : ("""

cc = cc.replace(old_features, new_features)

with open('src/app/courses/page.tsx', 'w') as f:
    f.write(cc)
