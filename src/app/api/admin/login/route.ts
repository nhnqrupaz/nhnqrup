import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const { email, password } = await request.json();
    
    // Check environment variables first, fallback to user provided hardcoded if not set
    const validEmail = process.env.ADMIN_EMAIL || 'natiqhemidovbusiness@gmail.com';
    const validPassword = process.env.ADMIN_PASSWORD || 'Natiq2026!';

    if (email === validEmail && password === validPassword) {
      const response = NextResponse.json({ success: true });
      
      // Set secure HTTP-only cookie
      response.cookies.set('nhn_admin_session', 'authenticated_admin', {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'lax',
        path: '/',
        maxAge: 60 * 60 * 24 * 7 // 1 week
      });
      
      return response;
    }
    
    return NextResponse.json({ success: false, message: 'İ-poçt və ya şifrə yanlışdır.' }, { status: 401 });
  } catch (error) {
    return NextResponse.json({ success: false, message: 'Server xətası' }, { status: 500 });
  }
}
