'use client';
import { useState, useEffect } from 'react';
import { supabase } from '@/lib/supabase';
import { Plus, Trash2, Upload, Edit, X, Save } from 'lucide-react';

export default function AdminProducts() {
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [form, setForm] = useState<any>({});
  const [editingId, setEditingId] = useState<string | null>(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const { data } = await supabase.from('products').select('*').order('created_at', { ascending: false });
    if (data) setItems(data);
    setLoading(false);
  };

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>, fieldName: string) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const formData = new FormData();
    formData.append('image', file);
    const res = await fetch('/api/admin/upload', { method: 'POST', body: formData });
    const data = await res.json();
    if (data.success) {
      setForm({ ...form, [fieldName]: data.url });
    } else {
      alert('Xəta: ' + data.message);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    const payload = { ...form };
    delete payload.id;
    delete payload.created_at;

    if (editingId) {
      const { error } = await supabase.from('products').update(payload).eq('id', editingId);
      if (error) alert('Xəta: ' + error.message);
      else {
        setForm({});
        setEditingId(null);
        fetchData();
      }
    } else {
      const { error } = await supabase.from('products').insert([payload]);
      if (error) alert('Xəta: ' + error.message);
      else {
        setForm({});
        fetchData();
      }
    }
  };

  const handleEdit = (item: any) => {
    setForm(item);
    setEditingId(item.id);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleCancelEdit = () => {
    setForm({});
    setEditingId(null);
  };

  const handleDelete = async (id: string) => {
    if(confirm('Silmək istədiyinizə əminsiniz?')) {
      await supabase.from('products').delete().eq('id', id);
      fetchData();
    }
  };

  if (loading) return <p>Yüklənir...</p>;

  return (
    <div className="max-w-5xl">
      <h1 className="text-3xl font-bold mb-8">Məhsullar İdarəetməsi</h1>
      
      <div className="bg-white p-6 md:p-8 rounded-2xl shadow-sm border border-gray-100 mb-8 transition-all">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-bold flex items-center gap-2">
            {editingId ? <><Edit size={20} className="text-blue-500"/> Redaktə edilir</> : <><Plus size={20} className="text-[#ff4f14]"/> Yeni Əlavə Et</>}
          </h2>
          {editingId && (
            <button onClick={handleCancelEdit} className="text-gray-500 hover:text-gray-700 flex items-center gap-1 text-sm bg-gray-100 px-3 py-1.5 rounded-lg">
              <X size={16} /> Ləğv et
            </button>
          )}
        </div>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          
          <div>
            <label className="block text-sm font-medium mb-1">Başlıq</label>
            <input required type="text" value={form.title || ''} onChange={e => setForm({...form, title: e.target.value})} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-2" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Məzmun / Açıqlama</label>
            <textarea required value={form.description || ''} onChange={e => setForm({...form, description: e.target.value})} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-2 min-h-[100px]" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Şəkil</label>
            {form.image_url && <img src={form.image_url} className="h-24 w-auto mb-2 rounded" />}
            <label className="flex items-center gap-2 bg-gray-50 border border-gray-200 px-4 py-2 rounded-xl cursor-pointer w-fit">
              <Upload size={16} /> Şəkil Yüklə
              <input type="file" className="hidden" accept="image/*" onChange={e => handleUpload(e, 'image_url')} />
            </label>
          </div>
          <button type="submit" className={`px-6 py-3 rounded-xl font-bold transition-colors text-white flex items-center gap-2 w-fit ${editingId ? 'bg-blue-600 hover:bg-blue-700' : 'bg-[#131312] hover:bg-[#ff4f14]'}`}>
            {editingId ? <><Save size={20} /> Yenilə</> : 'Əlavə Et'}
          </button>
        </form>
      </div>

      <div className="bg-white p-6 md:p-8 rounded-2xl shadow-sm border border-gray-100">
        <h2 className="text-xl font-bold mb-6">Mövcud Məhsullar</h2>
        <div className="space-y-4">
          {items.map((item) => (
            <div key={item.id} className="flex items-center justify-between p-4 border border-gray-100 rounded-xl hover:shadow-sm transition-shadow">
              <div className="flex items-center gap-4">
                {item.image_url && <img src={item.image_url} alt="" className="w-16 h-16 object-cover rounded-lg" />}
                {item.logo_url && <img src={item.logo_url} alt="" className="w-16 h-16 object-contain rounded-lg" />}
                <div>
                  <h3 className="font-bold text-lg">{item.title || item.name}</h3>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <button onClick={() => handleEdit(item)} className="text-blue-500 p-2 hover:bg-blue-50 rounded-lg transition-colors" title="Redaktə et">
                  <Edit size={20} />
                </button>
                <button onClick={() => handleDelete(item.id)} className="text-red-500 p-2 hover:bg-red-50 rounded-lg transition-colors" title="Sil">
                  <Trash2 size={20} />
                </button>
              </div>
            </div>
          ))}
          {items.length === 0 && <p className="text-gray-500">Heç nə tapılmadı.</p>}
        </div>
      </div>
    </div>
  );
}
