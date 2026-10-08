export const dynamic = 'force-dynamic';
export const revalidate = 0;

import Reveal from "@/components/Reveal";
import { PackageOpen } from "lucide-react";
import { supabase } from "@/lib/supabase";
import Link from "next/link";

export default async function ProductsPage() {
  const { data: products } = await supabase.from('products').select('*').order('created_at', { ascending: false });

  if (!products || products.length === 0) {
    return (
      <div className="flex flex-col min-h-[70vh] bg-[#f8f9f8] pt-32 pb-24 items-center justify-center">
        <Reveal direction="up" delay={0.1}>
          <div className="flex flex-col items-center text-center px-6">
            <div className="w-24 h-24 bg-[#ffece6] rounded-full flex items-center justify-center mb-8">
              <PackageOpen size={48} className="text-[#ff4f14]" />
            </div>
            <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
              Məhsullarımız <span className="text-[#ff4f14]">Tezliklə</span>
            </h1>
            <p className="text-lg text-gray-600 max-w-2xl">
              Təklif etdiyimiz mühəndislik, ağıllı ev və elektrik avadanlıqları barədə məlumatlar tezliklə bu səhifədə yerləşdiriləcək.
            </p>
          </div>
        </Reveal>
      </div>
    );
  }

  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Kataloq</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Bizim <span className="text-[#ff4f14]">Məhsullar</span>
          </h1>
          <p className="text-lg text-gray-600">
            Yüksək keyfiyyətli mühəndislik, elektrik və ağıllı ev avadanlıqları ilə tanış olun.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-7xl mx-auto w-full">
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {products.map((product: any, idx: number) => (
            <Reveal key={product.id} direction="up" delay={0.2 + (idx * 0.1)} className="h-full">
              <Link href={`/products/${product.id}`} className="block h-full">
                <div className="bg-white rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col h-full group border border-gray-100 relative">
                  {product.price && (
                    <div className="absolute top-4 right-4 bg-[#ff4f14] text-white px-4 py-1.5 rounded-full font-bold z-10 shadow-lg text-sm">
                      {product.price}
                    </div>
                  )}
                  {product.image_url && (
                    <div className="h-64 overflow-hidden relative bg-gray-100 flex items-center justify-center">
                      <img src={product.image_url} alt={product.title} className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
                    </div>
                  )}
                  <div className="p-8 flex flex-col flex-grow">
                    <h3 className="text-2xl font-bold mb-4 text-[#131312] group-hover:text-[#ff4f14] transition-colors">{product.title}</h3>
                    <p className="text-gray-600 flex-grow line-clamp-3">{product.description}</p>
                    <div className="mt-6 text-[#ff4f14] font-semibold flex items-center gap-2">
                      Ətraflı Bax <span className="text-lg">→</span>
                    </div>
                  </div>
                </div>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>
    </div>
  );
}
