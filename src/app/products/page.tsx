'use client';
import Reveal from "@/components/Reveal";
import { PackageOpen } from "lucide-react";

export default function ProductsPage() {
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
