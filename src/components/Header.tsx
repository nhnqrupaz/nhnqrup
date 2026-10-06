'use client';

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useState } from "react";
import { Menu, X, Phone } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function Header() {
  const pathname = usePathname();
  const router = useRouter();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const handleHomeClick = (e: React.MouseEvent) => {
    e.preventDefault();
    if (pathname === '/') {
      // @ts-ignore
      if (typeof window !== 'undefined' && window.lenis) {
        // @ts-ignore
        window.lenis.scrollTo(0, { duration: 1.5, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    } else {
      router.push('/');
    }
    setIsMobileMenuOpen(false);
  };

  const navLinks = [
    { name: 'Məhsullar', path: '/products' },
    { name: 'Xidmətlər', path: '/services' },
    { name: 'Kurslar', path: '/courses' },
    { name: 'Vakansiyalar', path: '/vacancies' },
    { name: 'CV Göndər', path: '/cv' },
    { name: 'Əlaqə', path: '/contact' }
  ];

  return (
    <header className="fixed top-0 w-full z-50 flex justify-center p-4 md:p-6 transition-all duration-300">
      <div className="bg-white rounded-full px-4 md:px-5 py-3 md:py-4 flex items-center justify-between w-full max-w-5xl shadow-sm relative gap-2">
        
        <a href="/" onClick={handleHomeClick} className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity z-50">
          <img src="/LogoPNG.png" alt="NHN Qrup Logo" className="h-8 md:h-10 w-auto object-contain" />
          <span className="font-black text-lg md:text-2xl tracking-tight text-[#131312] whitespace-nowrap shrink-0">NHN Qrup</span>
        </a>
        
        {/* Desktop Nav */}
        <nav className="hidden lg:flex items-center gap-5 xl:gap-6 text-[15px] xl:text-[16px] font-medium text-[#131312] absolute left-1/2 -translate-x-1/2">
          <a href="/" onClick={handleHomeClick} className="hover:text-[#ff4f14] transition-colors cursor-pointer">Ana Səhifə</a>
          {navLinks.map((link) => (
            <Link key={link.path} href={link.path} className="hover:text-[#ff4f14] transition-colors">{link.name}</Link>
          ))}
        </nav>
        
        <div className="hidden lg:block z-50">
          <Link href="/contact" className="bg-[#ff4f14] text-white px-6 py-2.5 rounded-full font-semibold hover:bg-[#e64612] transition-colors whitespace-nowrap">
            ƏLAQƏ
          </Link>
        </div>

        {/* Mobile Buttons */}
        <div className="flex items-center gap-3 lg:hidden z-50 ml-auto">
          <Link href="/contact" className="bg-[#ff4f14] text-white px-3 md:px-4 py-2 rounded-full text-xs font-bold hover:bg-[#e64612] transition-colors flex items-center gap-1 shadow-sm whitespace-nowrap shrink-0">
            <Phone size={14} />
            ƏLAQƏ
          </Link>
          <button 
            className="p-1 text-[#131312]" 
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>

        {/* Mobile Menu Dropdown */}
        <AnimatePresence>
          {isMobileMenuOpen && (
            <motion.div
              initial={{ opacity: 0, y: -20, scale: 0.95 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: -20, scale: 0.95 }}
              transition={{ duration: 0.2 }}
              className="absolute top-[120%] left-0 w-full bg-white rounded-3xl shadow-xl p-5 flex flex-col gap-3 lg:hidden border border-gray-100 z-40"
            >
              <a href="/" onClick={handleHomeClick} className="text-base font-bold text-[#131312] hover:text-[#ff4f14] border-b border-gray-100 pb-2 cursor-pointer">Ana Səhifə</a>
              {navLinks.map((link) => (
                <Link 
                  key={link.path} 
                  href={link.path} 
                  onClick={() => setIsMobileMenuOpen(false)}
                  className="text-base font-bold text-[#131312] hover:text-[#ff4f14] border-b border-gray-100 pb-2"
                >
                  {link.name}
                </Link>
              ))}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </header>
  );
}
