import { Outlet, Link, useLocation } from 'react-router-dom';
import { Package, Users, Truck, BarChart, Headset, Search, Bell, Settings } from 'lucide-react';

export default function AdminLayout() {
  const location = useLocation();

  const navItems = [
    { name: 'Inventario', icon: Package, path: '/admin' },
    { name: 'CRM', icon: Users, path: '/admin/crm' },
    { name: 'Logística', icon: Truck, path: '/admin/logistica' },
    { name: 'Reportes', icon: BarChart, path: '/admin/reportes' },
    { name: 'Soporte', icon: Headset, path: '/admin/soporte' },
  ];

  return (
    <div className="flex h-screen bg-surface font-body selection:bg-primary selection:text-on-primary overflow-hidden">
      {/* Sidebar */}
      <aside className="fixed left-0 top-0 h-full z-40 w-64 bg-[#0F172A] border-r border-white/5 font-headline tracking-tight flex flex-col">
        <div className="p-6 border-b border-white/5">
          <Link to="/" className="block">
            <h1 className="text-xl font-bold uppercase tracking-tighter">
              <span className="text-brand-orange">MIKI</span><span className="text-white">TECH</span>
            </h1>
            <p className="text-[10px] text-slate-500 mt-1 uppercase tracking-widest font-label">Panel de Control</p>
          </Link>
        </div>
        <nav className="flex-1 px-3 py-4 space-y-1">
          {navItems.map((item) => {
            const isActive = location.pathname === item.path;
            return (
              <Link
                key={item.name}
                to={item.path}
                className={`flex items-center gap-3 px-4 py-3 rounded-sm transition-all duration-300 ${
                  isActive ? 'bg-white/10 text-white' : 'text-slate-400 hover:bg-white/5 hover:text-white'
                }`}
              >
                <item.icon className="w-5 h-5" />
                <span className="text-sm font-medium">{item.name}</span>
              </Link>
            );
          })}
        </nav>
        <div className="p-6 border-t border-white/5 flex items-center gap-3">
          <div className="w-10 h-10 rounded-sm bg-white/10 flex items-center justify-center overflow-hidden">
            <img alt="Admin Avatar" className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBpLJ7VgxeA-hB3vHDK7hYlNDbqz8gtANVFjpsvjqBuucvPQPb7AYVkA6bns5IZkOZ2g2QcJWgjpxPT7f-Ggthz9IR1xVx0KECr_BTYrekhEmM65TqbXzxQfRE3t0UMRfV4dokZ6H_SrIWH0mzK56y1wLiZ28HMsM2FH7RY0uaUfqgclZC8dthWaUMmOg8YdcXi81ZLrIs47jeKQ-FaoMOyg35bDk1J2Mf6r4eqdJVOqCtJzSRytu-AVP8XIQNhnQDGaiA1EWfC46w" />
          </div>
          <div>
            <p className="text-xs font-bold text-white">Admin Micky</p>
            <p className="text-[10px] text-slate-500 uppercase">Superusuario</p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="ml-64 flex-1 flex flex-col h-full relative overflow-y-auto bg-surface">
        {/* Header */}
        <header className="sticky top-0 w-full z-30 flex justify-between items-center px-10 h-16 bg-white border-b border-outline-variant shrink-0">
          <div className="flex flex-col">
            <h2 className="font-headline text-xl font-bold text-on-surface tracking-tight">Panel de Administración</h2>
            <span className="text-[10px] font-label text-on-surface-variant tracking-[0.2em] uppercase">SISTEMA DE GESTIÓN MIKITECH</span>
          </div>
          <div className="flex items-center gap-6">
            <div className="hidden md:flex items-center bg-surface-container px-4 py-2 border border-outline-variant rounded-sm">
              <Search className="w-4 h-4 mr-3 text-on-surface-variant" />
              <input className="bg-transparent border-none outline-none text-xs text-on-surface w-64 placeholder:text-on-surface-variant focus:ring-0" placeholder="Buscar en la base de datos..." type="text" />
            </div>
            <div className="flex items-center gap-4 text-on-surface-variant">
              <button className="hover:text-primary transition-colors"><Bell className="w-5 h-5" /></button>
              <button className="hover:text-primary transition-colors"><Settings className="w-5 h-5" /></button>
              <div className="h-6 w-[1px] bg-outline-variant"></div>
              <button className="bg-primary text-on-primary font-headline text-xs font-bold px-4 py-2 rounded-sm uppercase tracking-wider hover:brightness-110 transition-all">Cerrar Sesión</button>
            </div>
          </div>
        </header>

        <div className="flex-1 p-10 max-w-7xl mx-auto w-full">
          <Outlet />
        </div>

        {/* Footer */}
        <footer className="py-10 border-t border-outline-variant bg-white w-full px-8 shrink-0">
          <div className="max-w-7xl mx-auto flex flex-col items-center gap-6">
            <div className="flex gap-8">
              <a className="text-on-surface-variant text-sm hover:text-primary transition-colors" href="#">Términos de Servicio</a>
              <a className="text-on-surface-variant text-sm hover:text-primary transition-colors" href="#">Privacidad</a>
              <a className="text-on-surface-variant text-sm hover:text-primary transition-colors" href="#">Documentación API</a>
              <a className="text-on-surface-variant text-sm hover:text-primary transition-colors" href="#">Estado del Sistema</a>
            </div>
            <div className="flex flex-col items-center gap-2">
              <span className="font-headline font-bold text-on-surface uppercase tracking-tight">
                <span className="text-brand-orange">MIKI</span>TECH
              </span>
              <p className="text-on-surface-variant text-xs">© 2026 MIKITECH WEB. Todos los derechos reservados.</p>
            </div>
          </div>
        </footer>
      </main>
    </div>
  );
}
