export const dynamic = 'force-dynamic';
export const revalidate = 0;

import Reveal from "@/components/Reveal";
import { Suspense } from "react";
import CVForm from "@/components/CVForm";
import { supabase } from "@/lib/supabase";

export default async function CVPage() {
  const { data: coursesData } = await supabase.from('courses').select('id, title').order('created_at', { ascending: false });
  const { data: vacanciesData } = await supabase.from('vacancies').select('id, title').order('created_at', { ascending: false });
  
  const fallbackCourses = [{id: 'f1', title: 'Elektrik Kursu'}, {id: 'f2', title: 'Ağıllı Ev (Smart Home)'}, {id: 'f3', title: 'Zəif Axın Sistemləri'}, {id: 'f4', title: 'PLC Proqramlaşdırma'}];
  const fallbackVacancies = [{id: 'v1', title: 'Elektrik'}, {id: 'v2', title: 'Elektrik köməkçisi'}, {id: 'v3', title: 'Elektromexanik'}];

  const courses = coursesData && coursesData.length > 0 ? coursesData : fallbackCourses;
  const vacancies = vacanciesData && vacanciesData.length > 0 ? vacanciesData : fallbackVacancies;


  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Müraciət</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Bizə <span className="text-[#ff4f14]">Müraciət Edin</span>
          </h1>
          <p className="text-lg text-gray-600">
            NHN QRUP komandasına qoşulmaq və ya peşəkar kurslarımıza qeydiyyatdan keçmək üçün formu doldurun.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-3xl mx-auto w-full">
        <Reveal direction="up" delay={0.2}>
          <div className="bg-white p-8 md:p-12 rounded-[2rem] shadow-sm border border-gray-100">
            <Suspense fallback={<p className="text-center text-gray-500">Yüklənir...</p>}>
              <CVForm courses={courses} vacancies={vacancies} />
            </Suspense>
          </div>
        </Reveal>
      </section>
    </div>
  );
}
