import os

courses_code = """import Link from "next/link";
import Reveal from "@/components/Reveal";
import { ArrowRight } from "lucide-react";
import { supabase } from "@/lib/supabase";

const fallbackCourses = [
  {
    title: "Elektrik Kursu",
    price: "160 ₼",
    image: "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=800&auto=format&fit=crop",
    desc: "Elektrik sahəsinin əsasları, avadanlıqlar və peşəkar quraşdırma qaydaları.",
    features: ["Real avadanlıqlar", "Sertifikat", "İşə yönləndirmə"]
  },
  {
    title: "Ağıllı Ev (Smart Home)",
    price: "250 ₼",
    image: "https://images.unsplash.com/photo-1558002038-1055907df827?q=80&w=800&auto=format&fit=crop",
    desc: "Müasir texnologiyalarla evlərin avtomatlaşdırılması və idarəetmə sistemləri.",
    features: ["Simsiz texnologiyalar", "Sertifikat", "İşə yönləndirmə"]
  }
];

export default async function CoursesPage() {
  const { data } = await supabase.from('courses').select('*').order('created_at', { ascending: false });
  const courses = data && data.length > 0 ? data : fallbackCourses;

  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Təlimlərimiz</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Gələcəyinizi <span className="text-[#ff4f14]">Peşəkar Biliklə</span> Qurun
          </h1>
          <p className="text-lg text-gray-600">
            NHN QRUP olaraq sizə ən çox tələb olunan sahələr üzrə həm nəzəri, həm də praktiki biliklər təqdim edirik.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-7xl mx-auto w-full">
        <div className="grid md:grid-cols-2 lg:grid-cols-2 gap-8">
          {courses.map((course: any, idx: number) => (
            <Reveal key={idx} direction="up" delay={0.2 + (idx * 0.1)} className="h-full">
              <div className="bg-white rounded-[2rem] overflow-hidden shadow-sm hover:shadow-xl transition-shadow duration-300 flex flex-col h-full group">
                <div className="h-64 overflow-hidden relative">
                  <div className="absolute top-4 right-4 bg-[#ff4f14] text-white px-4 py-1 rounded-full font-bold z-10 shadow-lg">
                    {course.price || 'Məlumat yoxdur'}
                  </div>
                  <img src={course.image_url || course.image} alt={course.title} className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
                </div>
                <div className="p-8 flex flex-col flex-grow">
                  <h3 className="text-2xl font-bold mb-3">{course.title}</h3>
                  <p className="text-gray-600 mb-6 flex-grow">{course.description || course.desc}</p>
                  
                  <div className="space-y-3 mb-8">
                    {course.features ? course.features.map((f: string, i: number) => (
                      <div key={i} className="flex items-center gap-3 text-gray-700">
                        <CheckIcon />
                        <span className="font-medium">{f}</span>
                      </div>
                    )) : (
                      <div className="flex items-center gap-3 text-gray-700">
                        <CheckIcon />
                        <span className="font-medium">Praktiki dərslər</span>
                      </div>
                    )}
                  </div>

                  <Link href={`/cv?job=${encodeURIComponent(course.title)}`} className="w-full bg-[#131312] text-white py-4 rounded-full font-bold hover:bg-[#ff4f14] transition-colors flex items-center justify-center gap-2">
                    Müraciət Et
                    <ArrowRight size={20} />
                  </Link>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>
    </div>
  );
}

function CheckIcon() {
  return (
    <div className="w-6 h-6 rounded-full bg-green-100 flex items-center justify-center shrink-0">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#16a34a" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
        <polyline points="20 6 9 17 4 12"></polyline>
      </svg>
    </div>
  );
}
"""

vacancies_code = """import Link from "next/link";
import Reveal from "@/components/Reveal";
import { ArrowRight, Briefcase, MapPin, DollarSign } from "lucide-react";
import { supabase } from "@/lib/supabase";

const fallbackVacancies = [
  {
    title: "Elektrik köməkçisi",
    salary: "800 ₼",
    type: "Tam iş günü",
    location: "Bakı, Azərbaycan",
    desc: "Elektrik montaj işlərində usta köməkçisi tələb olunur.",
    reqs: ["Sahə üzrə ilkin biliklər", "Fiziki sağlamlıq", "Kollektivdə işləmək bacarığı"]
  }
];

export default async function VacanciesPage() {
  const { data } = await supabase.from('vacancies').select('*').order('created_at', { ascending: false });
  const vacancies = data && data.length > 0 ? data : fallbackVacancies;

  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Karyera İmkanları</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Açıq <span className="text-[#ff4f14]">Vakansiyalar</span>
          </h1>
          <p className="text-lg text-gray-600">
            Peşəkar komandamıza qoşulun və inkişaf edən şirkətimizdə karyeranızı qurun.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-4xl mx-auto w-full space-y-6">
        {vacancies.map((job: any, idx: number) => (
          <Reveal key={idx} direction="up" delay={0.2 + (idx * 0.1)}>
            <div className="bg-white rounded-3xl p-8 shadow-sm hover:shadow-lg transition-shadow border border-gray-100 flex flex-col md:flex-row gap-8 justify-between">
              <div className="flex-1">
                <div className="flex flex-wrap items-center gap-3 mb-4">
                  <span className="bg-[#ffece6] text-[#ff4f14] px-4 py-1.5 rounded-full text-sm font-bold">
                    {job.type || 'Tam iş günü'}
                  </span>
                  <span className="flex items-center gap-1 text-gray-500 text-sm font-medium">
                    <MapPin size={16} /> {job.location || 'Bakı'}
                  </span>
                  <span className="flex items-center gap-1 text-gray-500 text-sm font-medium">
                    <DollarSign size={16} /> {job.salary}
                  </span>
                </div>
                
                <h3 className="text-2xl font-bold mb-3 text-[#131312]">{job.title}</h3>
                <p className="text-gray-600 mb-6">{job.description || job.desc}</p>
                
                {(job.requirements || job.reqs) && (
                  <div className="mb-6">
                    <h4 className="font-bold text-gray-900 mb-3 flex items-center gap-2">
                      <Briefcase size={18} className="text-[#ff4f14]" /> Tələblər:
                    </h4>
                    <ul className="space-y-2">
                      {String(job.requirements || job.reqs).split(',').map((req: string, i: number) => (
                        <li key={i} className="flex items-start gap-2 text-gray-600">
                          <span className="text-[#ff4f14] mt-1">•</span>
                          <span>{req.trim()}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
              
              <div className="flex items-center md:items-end justify-center">
                <Link href={`/cv?job=${encodeURIComponent(job.title)}`} className="w-full md:w-auto bg-[#ff4f14] text-white px-8 py-4 rounded-xl font-bold hover:bg-[#e64612] transition-colors flex items-center justify-center gap-2">
                  CV Göndər
                  <ArrowRight size={20} />
                </Link>
              </div>
            </div>
          </Reveal>
        ))}
      </section>
    </div>
  );
}
"""

with open('src/app/courses/page.tsx', 'w') as f:
    f.write(courses_code)

with open('src/app/vacancies/page.tsx', 'w') as f:
    f.write(vacancies_code)

