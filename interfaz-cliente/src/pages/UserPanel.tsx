import { LocateFixed, Plus, Minus, Truck, Cpu, Router, Radio } from 'lucide-react';

export default function UserPanel() {
  return (
    <div className="p-10 max-w-7xl mx-auto space-y-10">
      {/* Funny Alert Banner */}
      <section className="bg-primary-container/30 border-l-4 border-primary p-6 rounded-sm flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center">
            <LocateFixed className="text-primary w-6 h-6" />
          </div>
          <div>
            <h3 className="font-headline font-bold text-lg text-primary tracking-tight">¡Ubicado!</h3>
            <p className="text-on-surface-variant text-sm font-medium">Te vemos desde <span className="text-primary">Bogotá, Colombia</span>. Tu hardware llegará pronto. 📍</p>
          </div>
        </div>
        <div className="hidden sm:block text-right">
          <span className="text-[10px] uppercase tracking-[0.2em] text-slate-500 block">Estado del Enlace</span>
          <span className="text-xs font-headline font-bold text-primary">ENCRIPTADO & SEGURO</span>
        </div>
      </section>

      {/* Grid Content: Bento Style */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Map Module (Primary) */}
        <div className="lg:col-span-8 space-y-4">
          <div className="bg-surface-container-low p-2 rounded-sm shadow-2xl shadow-black/40 overflow-hidden">
            <div className="relative w-full h-[450px] bg-surface-container-highest group">
              {/* Placeholder for Interactive Map */}
              <img alt="Interactive Map of User City" className="w-full h-full object-cover opacity-60 grayscale hover:grayscale-0 transition-all duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuACx2ipHe4qfYWR8pecAhc4oL2vm7bmT5cbxPLmuiBFXivGjYjuSg-JpxXw9MPonGpDFCpmOeRHPtH3qJfOclOR68Q-_YgVuN_Ff_UupdcyC-w6L63XFqdSfXysFxczLPoZ-DdvkWCruvVa92dI0KYpgicBK0WohB9m9kSkrcqFyfXDfCujKReggl-y2xS7q5X4AhVk8SfZhU__4ACFtVvwheLpL79j30OidTCemgA0txAq9nSRtotDVLKhFr711dm2LmU8nlYe2Es" />
              
              {/* Map Overlay UI */}
              <div className="absolute inset-0 pointer-events-none p-6 flex flex-col justify-between">
                <div className="flex justify-between items-start">
                  <div className="glass-panel p-4 rounded-sm border border-outline-variant/20 pointer-events-auto">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
                      <span className="font-label text-[10px] uppercase font-bold tracking-widest text-primary">Señal de Geogestión Activa</span>
                    </div>
                    <h2 className="font-headline text-3xl font-black text-white leading-none">BOGOTÁ</h2>
                    <p className="text-slate-400 text-xs font-label mt-1">4.7110° N, 74.0721° W</p>
                  </div>
                  <div className="flex gap-2 pointer-events-auto">
                    <button className="bg-surface-container-high w-10 h-10 flex items-center justify-center hover:bg-primary hover:text-on-primary transition-colors">
                      <Plus className="w-5 h-5" />
                    </button>
                    <button className="bg-surface-container-high w-10 h-10 flex items-center justify-center hover:bg-primary hover:text-on-primary transition-colors">
                      <Minus className="w-5 h-5" />
                    </button>
                  </div>
                </div>
                <div className="flex justify-end">
                  <div className="glass-panel px-6 py-4 rounded-sm border border-outline-variant/20 flex gap-8 pointer-events-auto">
                    <div>
                      <p className="text-[10px] uppercase text-slate-500 font-bold mb-1">Fecha Local</p>
                      <p className="font-headline font-bold text-on-surface">24 MAY 2024</p>
                    </div>
                    <div className="w-[1px] bg-outline-variant/30"></div>
                    <div>
                      <p className="text-[10px] uppercase text-slate-500 font-bold mb-1">Hora Sistema</p>
                      <p className="font-headline font-bold text-primary tracking-widest">14:45:02</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="flex justify-between items-center text-xs font-label">
            <div className="flex gap-4 text-slate-500">
              <span className="flex items-center gap-1"><span className="w-2 h-2 rounded-full bg-primary"></span> Entregas en curso</span>
              <span className="flex items-center gap-1"><span className="w-2 h-2 rounded-full bg-error"></span> Alertas críticas</span>
            </div>
            <a className="text-primary hover:underline underline-offset-4" href="#">Ver mapa en pantalla completa</a>
          </div>
        </div>

        {/* Status & Order Sidebar */}
        <div className="lg:col-span-4 space-y-6">
          {/* Delivery Status Card */}
          <div className="bg-surface-container-high p-6 rounded-sm relative overflow-hidden">
            <div className="absolute top-0 right-0 p-4 opacity-10">
              <Truck className="w-24 h-24" />
            </div>
            <h4 className="font-headline font-bold text-slate-400 text-xs uppercase tracking-widest mb-4">Estado de Envío</h4>
            <div className="space-y-4">
              <div className="flex justify-between items-end">
                <div>
                  <p className="text-2xl font-black font-headline text-on-surface">MKT-88291</p>
                  <p className="text-xs text-primary font-bold">EN TRÁNSITO - AEROPUERTO EL DORADO</p>
                </div>
                <div className="text-right">
                  <p className="text-[10px] text-slate-500 font-bold uppercase">Llegada est.</p>
                  <p className="text-sm font-headline font-bold text-white">HOY 18:00</p>
                </div>
              </div>
              {/* Minimalist Progress Bar */}
              <div className="w-full h-1 bg-surface-container-highest">
                <div className="h-full bg-primary w-3/4 relative">
                  <div className="absolute -right-1 -top-1 w-3 h-3 bg-primary rounded-full shadow-[0_0_10px_#a9c8fc]"></div>
                </div>
              </div>
              <div className="flex justify-between text-[10px] font-bold text-slate-500 uppercase">
                <span>Origen: Shenzhen</span>
                <span>Destino: Bogotá</span>
              </div>
            </div>
          </div>

          {/* History List */}
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <h4 className="font-headline font-bold text-xs uppercase tracking-widest text-slate-400">Historial Reciente</h4>
              <button className="text-[10px] uppercase font-bold text-primary hover:underline">Ver Todo</button>
            </div>
            {/* Order Items */}
            <div className="space-y-2">
              <div className="bg-surface-container-low p-4 rounded-sm flex items-center justify-between border border-transparent hover:border-primary/20 transition-all cursor-pointer">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 bg-surface-container-highest flex items-center justify-center rounded-sm">
                    <Cpu className="text-slate-400 w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-sm font-bold text-on-surface">Procesador X-Quantum</p>
                    <p className="text-[10px] text-slate-500">MKT-1029 • 12 May 2024</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-xs font-headline font-bold text-on-surface">$1,250.00</p>
                  <span className="text-[9px] px-2 py-0.5 bg-secondary-container text-on-secondary-container rounded-full font-bold uppercase">Entregado</span>
                </div>
              </div>
              <div className="bg-surface-container-low p-4 rounded-sm flex items-center justify-between border border-transparent hover:border-primary/20 transition-all cursor-pointer">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 bg-surface-container-highest flex items-center justify-center rounded-sm">
                    <Router className="text-slate-400 w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-sm font-bold text-on-surface">Hub Satelital Micky</p>
                    <p className="text-[10px] text-slate-500">MKT-0944 • 05 May 2024</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-xs font-headline font-bold text-on-surface">$480.00</p>
                  <span className="text-[9px] px-2 py-0.5 bg-secondary-container text-on-secondary-container rounded-full font-bold uppercase">Entregado</span>
                </div>
              </div>
              <div className="bg-surface-container-low p-4 rounded-sm flex items-center justify-between border border-transparent hover:border-primary/20 transition-all cursor-pointer">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 bg-surface-container-highest flex items-center justify-center rounded-sm">
                    <Radio className="text-slate-400 w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-sm font-bold text-on-surface">Kit Sensores Geogestión</p>
                    <p className="text-[10px] text-slate-500">MKT-0812 • 28 Abr 2024</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-xs font-headline font-bold text-on-surface">$2,100.00</p>
                  <span className="text-[9px] px-2 py-0.5 bg-error-container text-on-error-container rounded-full font-bold uppercase">Devuelto</span>
                </div>
              </div>
            </div>
          </div>

          {/* Command Button (Primary Action) */}
          <button className="w-full py-4 bg-gradient-to-r from-primary to-[#6785b6] text-on-primary font-headline font-bold text-sm tracking-widest uppercase shadow-lg shadow-primary/10 hover:scale-[1.02] active:scale-95 transition-all">
            NUEVA SOLICITUD DE HARDWARE
          </button>
        </div>
      </div>
    </div>
  );
}
