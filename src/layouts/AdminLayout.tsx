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
      <aside className="fixed left-0 top-0 h-full z-40 w-64 border-r border-[#28283d] bg-[#1a1a2e] font-headline tracking-tight flex flex-col">
        <div className="p-6">
          <Link to="/" className="block">
            <h1 className="text-xl font-bold text-primary uppercase tracking-tighter">MICKYTECH</h1>
            <p className="text-[10px] text-slate-400 mt-1 uppercase tracking-widest font-label">Panel de Control</p>
          </Link>
        </div>
        <nav className="flex-1 px-3 space-y-1">
          {navItems.map((item) => {
            const isActive = location.pathname === item.path;
            return (
              <Link
                key={item.name}
                to={item.path}
                className={`flex items-center gap-3 px-4 py-3 rounded-sm transition-colors duration-300 scale-95 active:scale-90 ${
                  isActive ? 'bg-[#28283d] text-primary' : 'text-slate-400 hover:bg-[#28283d]'
                }`}
              >
                <item.icon className="w-5 h-5" />
                <span className="text-sm font-medium">{item.name}</span>
              </Link>
            );
          })}
        </nav>
        <div className="p-6 border-t border-[#28283d] flex items-center gap-3">
          <div className="w-10 h-10 rounded-sm bg-surface-container-highest flex items-center justify-center overflow-hidden">
            <img alt="Admin Avatar" className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBpLJ7VgxeA-hB3vHDK7hYlNDbqz8gtANVFjpsvjqBuucvPQPb7AYVkA6bns5IZkOZ2g2QcJWgjpxPT7f-Ggthz9IR1xVx0KECr_BTYrekhEmM65TqbXzxQfRE3t0UMRfV4dokZ6H_SrIWH0mzK56y1wLiZ28HMsM2FH7RY0uaUfqgclZC8dthWaUMmOg8YdcXi81ZLrIs47jeKQ-FaoMOyg35bDk1J2Mf6r4eqdJVOqCtJzSRytu-AVP8XIQNhnQDGaiA1EWfC46w" />
          </div>
          <div>
            <p className="text-xs font-bold text-on-surface">Admin Micky</p>
            <p className="text-[10px] text-slate-500 uppercase">Superusuario</p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="ml-64 flex-1 flex flex-col h-full relative overflow-y-auto">
        {/* Header */}
        <header className="sticky top-0 w-full z-30 flex justify-between items-center px-10 h-20 bg-[#111125]/80 backdrop-blur-xl border-b border-[#28283d]/50 shrink-0">
          <div className="flex flex-col">
            <h2 className="font-headline text-2xl font-black text-primary tracking-tighter uppercase">El Búnker</h2>
            <span className="text-[10px] font-label text-on-primary-container tracking-[0.2em]">SISTEMA DE GESTIÓN MICKYTECH PRO</span>
          </div>
          <div className="flex items-center gap-6">
            <div className="hidden md:flex items-center bg-surface-container-low px-4 py-2 border border-outline-variant/20">
              <Search className="w-4 h-4 mr-3 text-slate-500" />
              <input className="bg-transparent border-none outline-none text-xs text-on-surface w-64 placeholder:text-slate-600 focus:ring-0" placeholder="Buscar en la base de datos..." type="text" />
            </div>
            <div className="flex items-center gap-4 text-slate-300">
              <button className="hover:text-primary transition-all"><Bell className="w-5 h-5" /></button>
              <button className="hover:text-primary transition-all"><Settings className="w-5 h-5" /></button>
              <div className="h-6 w-[1px] bg-[#28283d]"></div>
              <button className="bg-primary text-on-primary font-headline text-xs font-bold px-4 py-2 rounded-sm uppercase tracking-wider">Cerrar Sesión</button>
            </div>
          </div>
        </header>

        <div className="flex-1 p-10 max-w-7xl mx-auto w-full">
          <Outlet />
        </div>

        {/* Footer */}
        <footer className="py-12 border-t border-[#1a1a2e] bg-[#111125] w-full px-8 max-w-7xl mx-auto flex flex-col items-center gap-6 shrink-0">
          <div className="flex gap-8">
            <a className="text-slate-500 text-sm hover:underline hover:text-primary" href="#">Términos de Servicio</a>
            <a className="text-slate-500 text-sm hover:underline hover:text-primary" href="#">Privacidad</a>
            <a className="text-slate-500 text-sm hover:underline hover:text-primary" href="#">Documentación API</a>
            <a className="text-slate-500 text-sm hover:underline hover:text-primary" href="#">Estado del Sistema</a>
          </div>
          <div className="flex flex-col items-center gap-2">
            <span className="font-headline font-bold text-primary uppercase tracking-tighter">MICKYTECH</span>
            <p className="text-slate-500 text-xs">© 2024 Mickytech. Blindaje Tecnológico Garantizado.</p>
          </div>
        </footer>
      </main>
    </div>
  );
}
