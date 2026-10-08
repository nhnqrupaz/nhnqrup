with open('src/app/products/[id]/page.tsx', 'r') as f:
    c = f.read()

c = c.replace(
    'export default async function ProductDetailPage({ params }: { params: { id: string } }) {',
    'export default async function ProductDetailPage({ params }: { params: Promise<{ id: string }> }) {\n  const resolvedParams = await params;'
)

c = c.replace(
    ".eq('id', params.id).single();",
    ".eq('id', resolvedParams.id).single();"
)

with open('src/app/products/[id]/page.tsx', 'w') as f:
    f.write(c)

