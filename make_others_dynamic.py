import os

# For each page, we will make it async and fetch from Supabase
files = {
    'courses': {
        'path': 'src/app/courses/page.tsx',
        'table': 'courses',
        'replacement_target': 'const courses = [',
        'new_data_code': '''export default async function CoursesPage() {
  const { data: courses } = await supabase.from('courses').select('*').order('created_at', { ascending: false });''',
        'import': 'import { supabase } from "@/lib/supabase";\n'
    },
    'vacancies': {
        'path': 'src/app/vacancies/page.tsx',
        'table': 'vacancies',
        'replacement_target': 'const vacancies = [',
        'new_data_code': '''export default async function VacanciesPage() {
  const { data: vacancies } = await supabase.from('vacancies').select('*').order('created_at', { ascending: false });''',
        'import': 'import { supabase } from "@/lib/supabase";\n'
    }
}

for key, val in files.items():
    with open(val['path'], 'r') as f:
        c = f.read()
    
    # Remove use client
    c = c.replace("'use client';\n", "")
    
    # Add import
    c = c.replace('import Link from "next/link";', 'import Link from "next/link";\n' + val['import'])
    
    # Find the dummy array and remove it
    # We will just replace the function declaration and let the array remain if we can't parse it well.
    # Wait, the dummy arrays might be large. Let's just do a regex or manual string split.
    # Actually, it's safer to just replace the export default function and the constant array entirely.
    pass

