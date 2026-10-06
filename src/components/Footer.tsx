'use client';

import Link from "next/link";
import { FaInstagram } from "react-icons/fa";

export default function Footer() {
  return (
    <footer id="contact" className="bg-[#131312] text-white pt-10 md:pt-16 pb-6 px-6 lg:px-20 overflow-hidden">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-12 gap-8 md:gap-12 mb-8 md:mb-12">
        <div className="col-span-1 md:col-span-6 flex flex-col justify-center">
          <div className="flex items-center gap-4 mb-4 md:mb-6">
            <img src="/Logo.png" alt="NHN Qrup" className="w-16 h-16 rounded-full object-cover bg-white p-1" />
            <span className="font-bold text-3xl tracking-tight italic">NHN Qrup</span>
          </div>
          <p className="text-white/70 mb-4 md:mb-6 italic max-w-sm">
            Peşəkar xidmətlər, innovativ həllər və gələcəyə inamlı addım. Hər zaman sizinlə.
          </p>
          <div className="flex items-center gap-4 text-white/50">
            <a href="https://www.instagram.com/nhnqrup.az/" target="_blank" rel="noopener noreferrer" className="hover:text-[#ff4f14] transition-colors" title="Bizi Instagram-da izləyin">
              <FaInstagram size={28} />
            </a>
          </div>
        </div>
        
        <div className="col-span-1 md:col-span-3 flex flex-col">
          <h4 className="font-bold text-lg mb-4 md:mb-6">Keçidlər</h4>
          <ul className="flex flex-col gap-4 text-white/70">
            <li><Link href="/" className="hover:text-white transition-colors">Ana Səhifə</Link></li>
            <li><Link href="/products" className="hover:text-white transition-colors">Məhsullar</Link></li>
            <li><Link href="/services" className="hover:text-white transition-colors">Xidmətlər</Link></li>
            <li><Link href="/courses" className="hover:text-white transition-colors">Kurslar</Link></li>
            <li><Link href="/vacancies" className="hover:text-white transition-colors">Vakansiyalar</Link></li>
          </ul>
        </div>

        <div className="col-span-1 md:col-span-3 flex flex-col">
          <h4 className="font-bold text-lg mb-4 md:mb-6">Haqqımızda</h4>
          <ul className="flex flex-col gap-4 text-white/70">
            <li><Link href="/about" className="hover:text-white transition-colors">Haqqımızda</Link></li>
            <li><Link href="/cv" className="hover:text-white transition-colors">CV Göndər</Link></li>
            <li><Link href="/contact" className="hover:text-white transition-colors">Əlaqə</Link></li>
            <li><Link href="/terms" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>
            <li><Link href="/privacy" className="hover:text-white transition-colors">Məxfilik siyasəti</Link></li>
          </ul>
        </div>
      </div>
      
      <div className="max-w-7xl mx-auto pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between text-white/50 text-sm">
        <p>© 2024 NHN Qrup. Bütün hüquqlar qorunur.</p>
        <p className="mt-4 md:mt-0 font-medium tracking-wider">NHN QRUP MMC</p>
      </div>
    </footer>
  );
}
