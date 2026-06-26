import { Outlet, Link, useLocation } from 'react-router-dom';
import { Search, Bell, ShoppingCart, User, Globe, Terminal, Shield } from 'lucide-react';

export default function StoreLayout() {
  const location = useLocation();

  return (
    <div className="min-h-screen bg-surface text-on-surface font-body selection:bg-primary selection:text-on-primary flex flex-col">
      {/* TopNavBar */}
      <header className="sticky top-0 w-full z-50 flex justify-between items-center px-6 h-20 bg-[#111125]/80 backdrop-blur-xl border-b border-[#28283d]/50 shadow-2xl shadow-[#000000]/40 font-headline">
        <div className="flex items-center gap-8">
          <Link to="/" className="text-2xl font-black text-primary tracking-tighter uppercase">Mickytech Pro</Link>
          <nav className="hidden md:flex gap-6">
            <Link to="/" className={`text-sm font-medium transition-all ${location.pathname === '/' ? 'text-primary border-b-2 border-primary pb-1' : 'text-slate-300 hover:text-primary'}`}>Hardware</Link>
            <Link to="/panel" className={`text-sm font-medium transition-all ${location.pathname === '/panel' ? 'text-primary border-b-2 border-primary pb-1' : 'text-slate-300 hover:text-primary'}`}>Geogestión</Link>
            <Link to="/checkout" className={`text-sm font-medium transition-all ${location.pathname === '/checkout' ? 'text-primary border-b-2 border-primary pb-1' : 'text-slate-300 hover:text-primary'}`}>Ofertas</Link>
            <Link to="/admin" className="text-slate-300 hover:text-primary transition-all text-sm font-medium">Soporte (Admin)</Link>
          </nav>
        </div>
        <div className="flex items-center gap-4">
          <div className="hidden lg:flex items-center bg-surface-container-high px-4 py-2 rounded-sm border border-outline-variant/20">
            <Search className="text-on-surface-variant w-4 h-4 mr-2" />
            <input className="bg-transparent border-none focus:ring-0 text-sm text-on-surface w-48 outline-none" placeholder="Buscar hardware..." type="text" />
          </div>
          <div className="flex items-center gap-4 text-primary">
            <button className="hover:opacity-100 opacity-80 transition-all"><Bell className="w-5 h-5" /></button>
            <Link to="/checkout" className="hover:opacity-100 opacity-80 transition-all flex items-center gap-2 px-3 py-1 bg-primary-container text-primary rounded-sm">
              <ShoppingCart className="w-5 h-5" />
              <span className="text-xs font-bold uppercase tracking-widest">Carrito</span>
            </Link>
            <Link to="/panel" className="hover:opacity-100 opacity-80 transition-all flex items-center gap-2">
              <User className="w-5 h-5" />
              <span className="hidden sm:inline text-xs font-bold uppercase tracking-widest">Mi Cuenta</span>
            </Link>
          </div>
        </div>
      </header>

      <main className="flex-1">
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="bg-[#111125] border-t border-[#1a1a2e] pt-20 pb-10 mt-auto">
        <div className="w-full px-8 max-w-7xl mx-auto flex flex-col items-center gap-12">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-12 w-full text-center md:text-left">
            <div className="space-y-4">
              <span className="font-headline font-bold text-primary text-xl">MICKYTECH</span>
              <p className="text-slate-500 font-body text-sm leading-relaxed">Líderes en blindaje tecnológico y soluciones de geogestión avanzada para empresas de alto rendimiento.</p>
            </div>
            <div className="space-y-4">
              <h5 className="text-xs font-bold text-on-surface tracking-widest uppercase font-headline">Ecosistema</h5>
              <ul className="space-y-2 text-slate-500 text-sm">
                <li><a className="hover:text-primary hover:underline transition-all" href="#">Configurador Pro</a></li>
                <li><a className="hover:text-primary hover:underline transition-all" href="#">MickyCloud Sync</a></li>
                <li><a className="hover:text-primary hover:underline transition-all" href="#">Soporte Técnico 24/7</a></li>
              </ul>
            </div>
            <div className="space-y-4">
              <h5 className="text-xs font-bold text-on-surface tracking-widest uppercase font-headline">Legal</h5>
              <ul className="space-y-2 text-slate-500 text-sm">
                <li><a className="hover:text-primary hover:underline transition-all" href="#">Términos de Servicio</a></li>
                <li><a className="hover:text-primary hover:underline transition-all" href="#">Privacidad</a></li>
                <li><a className="hover:text-primary hover:underline transition-all" href="#">Documentación API</a></li>
              </ul>
            </div>
            <div className="space-y-4">
              <h5 className="text-xs font-bold text-on-surface tracking-widest uppercase font-headline">Newsletter Blindada</h5>
              <div className="flex">
                <input className="bg-surface-container-high border-none text-xs w-full focus:ring-1 focus:ring-primary rounded-l-sm outline-none px-3 py-2" placeholder="Email" type="email" />
                <button className="bg-primary text-on-primary px-4 py-2 rounded-r-sm transition-all hover:brightness-110 flex items-center justify-center">
                  <span className="material-symbols-outlined text-sm">send</span>
                </button>
              </div>
            </div>
          </div>
          <div className="w-full flex flex-col md:flex-row justify-between items-center border-t border-outline-variant/10 pt-8 gap-4">
            <span className="text-slate-500 text-xs uppercase tracking-widest">© 2024 Mickytech. Blindaje Tecnológico Garantizado.</span>
            <div className="flex gap-6 text-slate-500">
              <Globe className="w-5 h-5 cursor-pointer hover:text-primary transition-colors" />
              <Terminal className="w-5 h-5 cursor-pointer hover:text-primary transition-colors" />
              <Shield className="w-5 h-5 cursor-pointer hover:text-primary transition-colors" />
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
