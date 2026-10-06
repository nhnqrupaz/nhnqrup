'use client';
import Reveal from "@/components/Reveal";
import { ArrowRight, Briefcase, MapPin, DollarSign } from "lucide-react";

const vacancies = [
  {
    title: "Elektrik köməkçisi",
    salary: "800 ₼",
    type: "Tam iş günü",
    location: "Bakı",
    desc: "Təcrübəli elektrik ustalarına dəstək göstərəcək və öyrənməyə həvəsli namizədlər axtarırıq."
  },
  {
    title: "Elektrik",
    salary: "1000 ₼",
    type: "Tam iş günü",
    location: "Bakı",
    desc: "Obyektlərdə elektrik çəkilişləri və quraşdırma işlərini müstəqil şəkildə həyata keçirəcək mütəxəssis."
  },
  {
    title: "Elektromexanik",
    salary: "1200 ₼",
    type: "Tam iş günü",
    location: "Bakı",
    desc: "Generatorlar və mühərriklər üzrə həm mexaniki, həm də elektrik problemlərini həll edəcək usta."
  }
];

export default function VacanciesPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      {/* Hero */}
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Karyera</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Bizim Komandamıza <span className="text-[#ff4f14]">Qoşulun</span>
          </h1>
          <p className="text-lg text-gray-600">
            Peşəkar mühitdə çalışmaq, öyrənmək və inkişaf etmək istəyirsinizsə, uyğun vakansiyaya müraciət edin.
          </p>
        </Reveal>
      </section>

      {/* List */}
      <section className="px-6 lg:px-20 max-w-5xl mx-auto w-full">
        <div className="flex flex-col gap-6">
          {vacancies.map((job, idx) => (
            <Reveal key={idx} direction="up" delay={0.2 + (idx * 0.1)}>
              <div className="bg-white rounded-[2rem] p-8 md:p-10 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col md:flex-row md:items-center justify-between group border border-gray-100">
                
                <div className="mb-6 md:mb-0 max-w-2xl">
                  <h3 className="text-2xl font-bold mb-4">{job.title}</h3>
                  <div className="flex flex-wrap items-center gap-4 text-sm font-medium text-gray-500 mb-4">
                    <span className="flex items-center gap-1.5 bg-gray-50 px-3 py-1.5 rounded-full"><DollarSign size={16} className="text-[#ff4f14]" /> {job.salary}</span>
                    <span className="flex items-center gap-1.5 bg-gray-50 px-3 py-1.5 rounded-full"><Briefcase size={16} className="text-[#ff4f14]" /> {job.type}</span>
                    <span className="flex items-center gap-1.5 bg-gray-50 px-3 py-1.5 rounded-full"><MapPin size={16} className="text-[#ff4f14]" /> {job.location}</span>
                  </div>
                  <p className="text-gray-600">
                    {job.desc}
                  </p>
                </div>
                
                <button className="shrink-0 bg-[#f8f9f8] text-[#131312] px-8 py-4 rounded-full font-bold group-hover:bg-[#ff4f14] group-hover:text-white transition-colors flex items-center justify-center gap-2">
                  CV Göndər
                  <ArrowRight size={20} />
                </button>
              </div>
            </Reveal>
          ))}
        </div>
      </section>
    </div>
  );
}
