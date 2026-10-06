'use client';
import Link from "next/link";
export default function Header() {
  return (
<header className="fixed top-0 w-full z-50 flex justify-center p-6 transition-all duration-300">
        <div className="bg-white rounded-full px-6 py-4 flex items-center justify-between w-full max-w-5xl shadow-sm">
          <button onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} className="flex items-center gap-3 cursor-pointer hover:opacity-80 transition-opacity">
            <img src="/LogoPNG.png" alt="NHN Qrup Logo" className="h-8 w-auto object-contain" />
            <span className="font-black text-2xl md:text-3xl tracking-tight text-[#131312]">NHN Qrup</span>
          </button>
          <nav className="hidden lg:flex gap-5 text-[15px] font-medium text-[#131312]">
            <button onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} className="hover:text-[#ff4f14] transition-colors">Ana Səhifə</button>
            <Link href="/products" className="hover:text-[#ff4f14] transition-colors">Məhsullar</Link>
            <Link href="/services" className="hover:text-[#ff4f14] transition-colors">Xidmətlər</Link>
            <Link href="/courses" className="hover:text-[#ff4f14] transition-colors">Kurslar</Link>
            <Link href="/vacancies" className="hover:text-[#ff4f14] transition-colors">Vakansiyalar</Link>
            <Link href="/cv" className="hover:text-[#ff4f14] transition-colors">CV Göndər</Link>
          </nav>
          <Link href="/contact" className="bg-[#ff4f14] text-white px-6 py-3 rounded-full font-semibold hover:bg-[#e64612] transition-colors whitespace-nowrap">
            ƏLAQƏ
          </Link>
        </div>
      </header>
  );
}
