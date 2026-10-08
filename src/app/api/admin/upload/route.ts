import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    const image = formData.get('image');
    
    if (!image) {
      return NextResponse.json({ success: false, message: 'Şəkil tapılmadı' }, { status: 400 });
    }

    const imgbbApiKey = process.env.NEXT_PUBLIC_IMGBB_API_KEY;
    if (!imgbbApiKey) {
      return NextResponse.json({ success: false, message: 'ImgBB API açarı tapılmadı' }, { status: 500 });
    }

    const imgbbFormData = new FormData();
    imgbbFormData.append('image', image);

    const res = await fetch(`https://api.imgbb.com/1/upload?key=${imgbbApiKey}`, {
      method: 'POST',
      body: imgbbFormData
    });

    const data = await res.json();

    if (data.success) {
      return NextResponse.json({ success: true, url: data.data.url });
    } else {
      return NextResponse.json({ success: false, message: data.error?.message || 'ImgBB xətası' }, { status: 400 });
    }

  } catch (error: any) {
    return NextResponse.json({ success: false, message: error.message }, { status: 500 });
  }
}
