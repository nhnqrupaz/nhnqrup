with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Extract just the stats section
start_marker = "{/* Stats Section */}"
end_marker = "{/* Niyə Bizi Seçməlisiniz Section */}"

start_idx = c.find(start_marker)
end_idx = c.find(end_marker)

stats_html = c[start_idx:end_idx]

# Clean up Reveal in stats_html ONLY
stats_html = stats_html.replace('<Reveal direction="up" delay={0.1}>\n          <div>', '<div>')
stats_html = stats_html.replace('</div>\n          </Reveal>', '</div>')

stats_html = stats_html.replace('<Reveal direction="up" delay={0.2}>\n          <div>', '<div>')
stats_html = stats_html.replace('<Reveal direction="up" delay={0.3}>\n          <div>', '<div>')
stats_html = stats_html.replace('<Reveal direction="up" delay={0.4}>\n          <div>', '<div>')

c = c[:start_idx] + stats_html + c[end_idx:]

with open('src/app/page.tsx', 'w') as f:
    f.write(c)
