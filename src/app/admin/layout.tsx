'use client';
import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { LayoutDashboard, Image as ImageIcon, Briefcase, GraduationCap, Package, Users, LogOut } from 'lucide-react';

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const router = useRouter();

  // If we are on the login page, don't show the sidebar
  if (pathname === '/admin/login') {
    return <>{children}</>;
  }

  const handleLogout = async () => {
    await fetch('/api/admin/logout', { method: 'POST' });
    router.push('/admin/login');
  };

  const menu = [
    { name: 'Ayarlar (Şəkillər)', path: '/admin', icon: ImageIcon },
    { name: 'Məhsullar', path: '/admin/products', icon: Package },
    { name: 'Kurslar', path: '/admin/courses', icon: GraduationCap },
    { name: 'Vakansiyalar', path: '/admin/vacancies', icon: Briefcase },
    { name: 'Partnyorlar', path: '/admin/partners', icon: Users },
  ];

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col md:flex-row">
      {/* Sidebar */}
      <aside className="w-full md:w-64 bg-[#131312] text-white flex flex-col min-h-fit md:min-h-screen shrink-0">
        <div className="p-6 border-b border-white/10">
          <Link href="/" className="font-black text-2xl tracking-tight text-white flex items-center gap-2">
            NHN Qrup <span className="text-[#ff4f14] text-sm font-medium bg-white/10 px-2 py-1 rounded">Admin</span>
          </Link>
        </div>
        
        <nav className="flex-grow p-4 flex flex-col gap-2">
          {menu.map(item => {
            const Icon = item.icon;
            const isActive = pathname === item.path;
            return (
              <Link 
                key={item.path} 
                href={item.path}
                className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-colors ${
                  isActive ? 'bg-[#ff4f14] text-white font-bold' : 'text-white/70 hover:bg-white/10 hover:text-white'
                }`}
              >
                <Icon size={20} />
                {item.name}
              </Link>
            )
          })}
        </nav>

        <div className="p-4 border-t border-white/10">
          <button 
            onClick={handleLogout}
            className="flex items-center gap-3 w-full px-4 py-3 text-red-400 hover:bg-white/10 rounded-xl transition-colors"
          >
            <LogOut size={20} />
            Çıxış et
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6 md:p-12 overflow-y-auto">
        {children}
      </main>
    </div>
  );
}
