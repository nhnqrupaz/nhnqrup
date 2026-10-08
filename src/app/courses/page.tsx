import Link from "next/link";
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
                    {course.features ? (Array.isArray(course.features) ? course.features : String(course.features).split(',')).map((f: string, i: number) => (
                      <div key={i} className="flex items-center gap-3 text-gray-700">
                        <CheckIcon />
                        <span className="font-medium">{f.trim()}</span>
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
