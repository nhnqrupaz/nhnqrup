with open('src/app/cv/page.tsx', 'r') as f:
    c = f.read()

new_logic = """  const { data: coursesData } = await supabase.from('courses').select('id, title').order('created_at', { ascending: false });
  const { data: vacanciesData } = await supabase.from('vacancies').select('id, title').order('created_at', { ascending: false });
  
  const fallbackCourses = [{id: 'f1', title: 'Elektrik Kursu'}, {id: 'f2', title: 'Ağıllı Ev (Smart Home)'}, {id: 'f3', title: 'Zəif Axın Sistemləri'}, {id: 'f4', title: 'PLC Proqramlaşdırma'}];
  const fallbackVacancies = [{id: 'v1', title: 'Elektrik'}, {id: 'v2', title: 'Elektrik köməkçisi'}, {id: 'v3', title: 'Elektromexanik'}];

  const courses = coursesData && coursesData.length > 0 ? coursesData : fallbackCourses;
  const vacancies = vacanciesData && vacanciesData.length > 0 ? vacanciesData : fallbackVacancies;
"""

old_logic = """  const { data: coursesData } = await supabase.from('courses').select('id, title').order('created_at', { ascending: false });
  const { data: vacanciesData } = await supabase.from('vacancies').select('id, title').order('created_at', { ascending: false });
  
  const courses = coursesData || [];
  const vacancies = vacanciesData || [];"""

c = c.replace(old_logic, new_logic)

with open('src/app/cv/page.tsx', 'w') as f:
    f.write(c)
