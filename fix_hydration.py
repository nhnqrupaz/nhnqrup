with open('src/components/CVForm.tsx', 'r') as f:
    c = f.read()

c = c.replace(
    """{typeof window !== 'undefined' && (
        <input type="hidden" name="_next" value={`${window.location.origin}/cv?success=true`} />
      )}""",
    """<input type="hidden" name="_next" value="https://nhnqrup.az/cv?success=true" />"""
)

with open('src/components/CVForm.tsx', 'w') as f:
    f.write(c)

