'use client';

import { useState, useEffect, useRef } from 'react';
import { supabase } from '@/lib/supabase';
import { Upload, Save } from 'lucide-react';

export default function AdminSettings() {
  const [heroImage, setHeroImage] = useState('');
  const [ctaImage, setCtaImage] = useState('');
  const [whyUsImage, setWhyUsImage] = useState('');
  const [urgentImage, setUrgentImage] = useState('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    fetchSettings();
  }, []);

  const fetchSettings = async () => {
    try {
      const { data, error } = await supabase.from('settings').select('*').eq('id', 1).single();
      if (data) {
        setHeroImage(data.hero_image_url || '');
        setCtaImage(data.cta_image_url || '');
        setWhyUsImage(data.why_us_image_url || '');
        setUrgentImage(data.urgent_image_url || '');
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>, setter: (val: string) => void) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('image', file);

    const res = await fetch('/api/admin/upload', {
      method: 'POST',
      body: formData,
    });
    const data = await res.json();
    if (data.success) {
      setter(data.url);
    } else {
      alert('Şəkil yüklənərkən xəta: ' + data.message);
    }
  };

  const saveSettings = async () => {
    setSaving(true);
    const { error } = await supabase
      .from('settings')
      .upsert({ id: 1, hero_image_url: heroImage, cta_image_url: ctaImage, why_us_image_url: whyUsImage, urgent_image_url: urgentImage, updated_at: new Date().toISOString() });
    
    setSaving(false);
    if (error) {
      alert('Yadda saxlayarkən xəta: ' + error.message);
    } else {
      alert('Uğurla yadda saxlanıldı!');
    }
  };

  if (loading) return <p>Yüklənir...</p>;

  return (
    <div className="max-w-3xl">
      <h1 className="text-3xl font-bold mb-8">Sayt Şəkilləri (Ayarlar)</h1>

      <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 mb-8 space-y-8">
        
        {/* Hero Image */}
        <div>
          <label className="block text-sm font-bold text-gray-700 mb-2">Ana Ekran Şəkli (Hero)</label>
          {heroImage && (
            <img src={heroImage} alt="Hero" className="w-full h-48 object-cover rounded-xl mb-4" />
          )}
          <label className="flex items-center gap-2 bg-gray-50 border border-gray-200 px-4 py-3 rounded-xl cursor-pointer hover:bg-gray-100 transition-colors">
            <Upload size={20} className="text-gray-500" />
            <span className="text-gray-600 font-medium">Yeni şəkil seç və yüklə</span>
            <input type="file" className="hidden" accept="image/*" onChange={e => handleUpload(e, setHeroImage)} />
          </label>
        </div>

        <hr className="border-gray-100" />

        {/* CTA Image */}
        <div>
          <label className="block text-sm font-bold text-gray-700 mb-2">Zəng Qutucuğu Şəkli (CTA)</label>
          {ctaImage && (
            <img src={ctaImage} alt="CTA" className="w-full h-48 object-cover rounded-xl mb-4" />
          )}
          <label className="flex items-center gap-2 bg-gray-50 border border-gray-200 px-4 py-3 rounded-xl cursor-pointer hover:bg-gray-100 transition-colors">
            <Upload size={20} className="text-gray-500" />
            <span className="text-gray-600 font-medium">Yeni şəkil seç və yüklə</span>
            <input type="file" className="hidden" accept="image/*" onChange={e => handleUpload(e, setCtaImage)} />
          </label>
        </div>

        <hr className="border-gray-100" />

        {/* Why Us Image */}
        <div>
          <label className="block text-sm font-bold text-gray-700 mb-2">Niyə Bizi Seçməlisiniz (Orta Şəkil)</label>
          {whyUsImage && (
            <img src={whyUsImage} alt="Why Us" className="w-full h-48 object-cover rounded-xl mb-4" />
          )}
          <label className="flex items-center gap-2 bg-gray-50 border border-gray-200 px-4 py-3 rounded-xl cursor-pointer hover:bg-gray-100 transition-colors">
            <Upload size={20} className="text-gray-500" />
            <span className="text-gray-600 font-medium">Yeni şəkil seç və yüklə</span>
            <input type="file" className="hidden" accept="image/*" onChange={e => handleUpload(e, setWhyUsImage)} />
          </label>
        </div>

        <hr className="border-gray-100" />

        {/* Urgent Image */}
        <div>
          <label className="block text-sm font-bold text-gray-700 mb-2">Təcili Xidmət Şəkli (Dairəvi Şəkil)</label>
          {urgentImage && (
            <img src={urgentImage} alt="Urgent" className="w-48 h-48 object-cover rounded-full mx-auto border-8 border-gray-100 mb-4" />
          )}
          <label className="flex items-center gap-2 bg-gray-50 border border-gray-200 px-4 py-3 rounded-xl cursor-pointer hover:bg-gray-100 transition-colors">
            <Upload size={20} className="text-gray-500" />
            <span className="text-gray-600 font-medium">Yeni şəkil seç və yüklə</span>
            <input type="file" className="hidden" accept="image/*" onChange={e => handleUpload(e, setUrgentImage)} />
          </label>
        </div>

      </div>

      <button 
        onClick={saveSettings}
        disabled={saving}
        className="bg-[#ff4f14] text-white px-8 py-4 rounded-xl font-bold flex items-center gap-2 hover:bg-[#e64612] transition-colors disabled:opacity-50"
      >
        <Save size={20} />
        {saving ? 'Yadda Saxlanılır...' : 'Dəyişiklikləri Yadda Saxla'}
      </button>
    </div>
  );
}
