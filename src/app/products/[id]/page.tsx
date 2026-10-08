import { supabase } from "@/lib/supabase";
import { notFound } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, MessageCircle } from "lucide-react";
import Reveal from "@/components/Reveal";

export default async function ProductDetailPage({ params }: { params: { id: string } }) {
  const { data: product, error } = await supabase.from('products').select('*').eq('id', params.id).single();

  if (error || !product) {
    notFound();
  }

  // Pre-fill WhatsApp message
  const waMessage = encodeURIComponent(`Salam, mən bu məhsulla maraqlanıram: ${product.title}`);
  const waLink = `https://wa.me/994773334466?text=${waMessage}`;

  return (
    <div className="min-h-screen bg-[#f8f9f8] pt-32 pb-24 px-6 lg:px-20">
      <div className="max-w-6xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <Link href="/products" className="inline-flex items-center gap-2 text-gray-500 hover:text-[#ff4f14] font-medium mb-8 transition-colors">
            <ArrowLeft size={20} />
            Məhsullara Qayıt
          </Link>
        </Reveal>

        <div className="bg-white rounded-3xl overflow-hidden shadow-sm border border-gray-100 p-6 md:p-12">
          <div className="grid md:grid-cols-2 gap-12 items-start">
            
            {/* Image */}
            <Reveal direction="up" delay={0.2} className="h-full">
              <div className="bg-gray-50 rounded-2xl overflow-hidden h-[400px] md:h-[500px] flex items-center justify-center">
                {product.image_url ? (
                  <img src={product.image_url} alt={product.title} className="w-full h-full object-cover" />
                ) : (
                  <div className="text-gray-400">Şəkil yoxdur</div>
                )}
              </div>
            </Reveal>

            {/* Content */}
            <Reveal direction="up" delay={0.3}>
              <div className="flex flex-col h-full">
                <h1 className="text-3xl md:text-5xl font-bold text-[#131312] mb-4">{product.title}</h1>
                
                {product.price && (
                  <div className="text-3xl font-black text-[#ff4f14] mb-8">
                    {product.price}
                  </div>
                )}

                <div className="prose prose-lg text-gray-600 mb-12 whitespace-pre-line">
                  {product.description}
                </div>

                <div className="mt-auto pt-8 border-t border-gray-100">
                  <a 
                    href={waLink} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="w-full md:w-auto bg-[#25D366] text-white px-8 py-4 rounded-xl font-bold hover:bg-[#1ebd5a] transition-colors flex items-center justify-center gap-3 text-lg"
                  >
                    <MessageCircle size={24} />
                    WhatsApp ilə Sifariş Et
                  </a>
                </div>
              </div>
            </Reveal>
            
          </div>
        </div>
      </div>
    </div>
  );
}
