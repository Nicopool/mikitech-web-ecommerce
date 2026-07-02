import { Outlet, Link, useLocation } from 'react-router-dom';
import { Search, Bell, ShoppingCart, User, Globe, Terminal, Shield } from 'lucide-react';

export default function StoreLayout() {
  const location = useLocation();

  return (
    <div className="min-h-screen bg-surface text-on-surface font-body selection:bg-primary selection:text-on-primary flex flex-col">
      {/* TopNavBar */}
      <header className="sticky top-0 w-full z-50 flex justify-between items-center px-6 h-16 bg-white border-b border-outline-variant shadow-sm font-headline">
        <div className="flex items-center gap-8">
          <Link to="/" className="text-2xl font-black tracking-tighter uppercase flex items-center gap-1">
            <span className="text-brand-orange">MIKI</span><span className="text-on-surface">TECH</span>
          </Link>
          <nav className="hidden md:flex gap-6">
            <Link to="/" className={`text-sm font-medium transition-all ${location.pathname === '/' ? 'text-primary border-b-2 border-primary pb-1' : 'text-on-surface-variant hover:text-primary'}`}>Hardware</Link>
            <Link to="/panel" className={`text-sm font-medium transition-all ${location.pathname === '/panel' ? 'text-primary border-b-2 border-primary pb-1' : 'text-on-surface-variant hover:text-primary'}`}>Geogestión</Link>
            <Link to="/checkout" className={`text-sm font-medium transition-all ${location.pathname === '/checkout' ? 'text-primary border-b-2 border-primary pb-1' : 'text-on-surface-variant hover:text-primary'}`}>Ofertas</Link>
            <Link to="/admin" className="text-on-surface-variant hover:text-primary transition-all text-sm font-medium">Soporte (Admin)</Link>
          </nav>
        </div>
        <div className="flex items-center gap-4">
          <div className="hidden lg:flex items-center bg-surface-container px-4 py-2 rounded-sm border border-outline-variant">
            <Search className="text-on-surface-variant w-4 h-4 mr-2" />
            <input className="bg-transparent border-none focus:ring-0 text-sm text-on-surface w-48 outline-none" placeholder="Buscar hardware..." type="text" />
          </div>
          <div className="flex items-center gap-4 text-primary">
            <button className="hover:text-primary transition-colors text-on-surface-variant"><Bell className="w-5 h-5" /></button>
            <Link to="/checkout" className="hover:text-primary transition-colors flex items-center gap-2 px-3 py-1 bg-primary-container text-on-primary-container rounded-sm">
              <ShoppingCart className="w-5 h-5" />
              <span className="text-xs font-bold uppercase tracking-widest">Carrito</span>
            </Link>
            <Link to="/panel" className="hover:text-primary transition-colors flex items-center gap-2 text-on-surface-variant">
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
      <footer className="bg-[#0F172A] border-t border-outline-variant/10 pt-16 pb-10 mt-auto">
        <div className="w-full px-8 max-w-7xl mx-auto flex flex-col items-center gap-12">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-12 w-full text-center md:text-left">
            <div className="space-y-4">
              <span className="font-headline font-bold text-white text-xl tracking-tight uppercase">
                <span className="text-brand-orange">MIKI</span>TECH
              </span>
              <p className="text-slate-400 font-body text-sm leading-relaxed">Expertos en hardware de alta gama. Ofrecemos lo último en tecnología de computación, optimizando el rendimiento para gamers y profesionales exigentes.</p>
            </div>
            <div className="space-y-4">
              <h5 className="text-xs font-bold text-slate-300 tracking-widest uppercase font-headline">Navegación</h5>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><Link to="/" className="hover:text-white transition-colors">Inicio</Link></li>
                <li><Link to="/panel" className="hover:text-white transition-colors">Tienda Online</Link></li>
                <li><a className="hover:text-white transition-colors" href="#">Contacto</a></li>
              </ul>
            </div>
            <div className="space-y-4">
              <h5 className="text-xs font-bold text-slate-300 tracking-widest uppercase font-headline">Tecnología</h5>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><a className="hover:text-white transition-colors" href="#">Procesadores</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Tarjetas de Video</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Periféricos</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Almacenamiento</a></li>
              </ul>
            </div>
            <div className="space-y-4">
              <h5 className="text-xs font-bold text-slate-300 tracking-widest uppercase font-headline">Comunidad</h5>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><a className="hover:text-white transition-colors" href="#">Centro de Ayuda</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Garantías Miki</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Términos y Condiciones</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Protección de Datos</a></li>
              </ul>
            </div>
          </div>
          <div className="w-full flex flex-col md:flex-row justify-between items-center border-t border-white/10 pt-8 gap-4">
            <span className="text-slate-500 text-xs uppercase tracking-widest">© 2026 MIKITECH WEB. Todos los derechos reservados. Bogotá, Colombia.</span>
            <div className="flex gap-6 text-slate-500">
              <Globe className="w-5 h-5 cursor-pointer hover:text-white transition-colors" />
              <Terminal className="w-5 h-5 cursor-pointer hover:text-white transition-colors" />
              <Shield className="w-5 h-5 cursor-pointer hover:text-white transition-colors" />
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
