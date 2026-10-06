with open('src/components/SmoothScroll.tsx', 'r') as f:
    c = f.read()

if 'window.lenis = lenis' not in c:
    c = c.replace('const lenis = new Lenis({', 'const lenis = new Lenis({')
    c = c.replace('requestAnimationFrame(raf);', 'requestAnimationFrame(raf);\n    // @ts-ignore\n    window.lenis = lenis;')

    # Also clean up on unmount
    c = c.replace('lenis.destroy();', 'lenis.destroy();\n      // @ts-ignore\n      window.lenis = undefined;')

with open('src/components/SmoothScroll.tsx', 'w') as f:
    f.write(c)

with open('src/components/Header.tsx', 'r') as f:
    ch = f.read()

old_click = "window.scrollTo({ top: 0, behavior: 'smooth' });"
new_click = """// @ts-ignore
      if (typeof window !== 'undefined' && window.lenis) {
        // @ts-ignore
        window.lenis.scrollTo(0, { duration: 1.5, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }"""

ch = ch.replace(old_click, new_click)

with open('src/components/Header.tsx', 'w') as f:
    f.write(ch)
