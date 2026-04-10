import { Package, PlusSquare, CloudDownload, ArrowRight, Download, Truck, RefreshCw, CheckCircle } from 'lucide-react';

export default function Dashboard() {
  return (
    <div className="space-y-10">
      {/* Bento Grid Section: Top Metrics */}
      <section className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {/* Inventory High-Level Card */}
        <div className="md:col-span-2 bg-surface-container-low p-8 relative overflow-hidden flex flex-col justify-between group">
          <div className="z-10">
            <span className="text-[10px] font-label font-bold text-primary tracking-widest uppercase mb-4 block">Resumen de Inventario</span>
            <div className="flex items-baseline gap-2">
              <h3 className="font-headline text-6xl font-black text-on-surface tracking-tighter">107</h3>
              <span className="text-slate-500 font-headline text-xl">SKUS</span>
            </div>
            <p className="text-sm text-slate-400 mt-2 max-w-xs">Blindaje tecnológico activo. El stock total de hardware está sincronizado con el nodo central.</p>
          </div>
          <div className="mt-8 flex gap-4 z-10">
            <div className="bg-surface-container-highest px-3 py-1 flex items-center gap-2">
              <div className="w-1.5 h-1.5 bg-primary rounded-full animate-pulse"></div>
              <span className="text-[10px] font-label text-on-surface uppercase">84% Capacidad</span>
            </div>
            <div className="bg-surface-container-highest px-3 py-1 flex items-center gap-2">
              <span className="text-[10px] font-label text-error uppercase">12 Críticos</span>
            </div>
          </div>
          <Package className="absolute -right-4 -bottom-4 w-32 h-32 opacity-5 text-primary group-hover:opacity-10 transition-opacity" />
        </div>

        {/* Logistics Status Summary */}
        <div className="bg-surface-container-low p-6 flex flex-col justify-between">
          <span className="text-[10px] font-label font-bold text-slate-500 tracking-widest uppercase mb-4 block">Flujo Logístico</span>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-xs text-on-surface-variant font-medium">Procesando</span>
              <span className="font-headline text-primary font-bold">14</span>
            </div>
            <div className="w-full h-1 bg-surface-container-highest">
              <div className="bg-primary h-full w-[45%]"></div>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-xs text-on-surface-variant font-medium">En Camino</span>
              <span className="font-headline text-secondary font-bold">08</span>
            </div>
            <div className="w-full h-1 bg-surface-container-highest">
              <div className="bg-secondary h-full w-[25%]"></div>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-xs text-on-surface-variant font-medium">Entregado</span>
              <span className="font-headline text-on-primary-container font-bold">85</span>
            </div>
            <div className="w-full h-1 bg-surface-container-highest">
              <div className="bg-on-primary-container h-full w-[85%]"></div>
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="bg-primary-container p-6 flex flex-col justify-between">
          <span className="text-[10px] font-label font-bold text-on-primary-container tracking-widest uppercase mb-4 block">Comandos Rápidos</span>
          <div className="grid grid-cols-2 gap-2">
            <button className="bg-[#1a1a2e] p-4 flex flex-col gap-2 items-center justify-center hover:bg-surface-container-highest transition-colors">
              <PlusSquare className="text-primary w-6 h-6" />
              <span className="text-[9px] font-bold uppercase text-slate-400 tracking-tighter">Nuevo SKU</span>
            </button>
            <button className="bg-[#1a1a2e] p-4 flex flex-col gap-2 items-center justify-center hover:bg-surface-container-highest transition-colors">
              <CloudDownload className="text-primary w-6 h-6" />
              <span className="text-[9px] font-bold uppercase text-slate-400 tracking-tighter">Exportar</span>
            </button>
          </div>
          <button className="w-full mt-4 bg-primary text-on-primary font-headline text-[10px] font-black py-3 uppercase tracking-widest">
            GENERAR REPORTE GLOBAL
          </button>
        </div>
      </section>

      {/* Main Data Section: CRM Table */}
      <section className="space-y-6">
        <div className="flex justify-between items-end">
          <div>
            <h2 className="font-headline text-3xl font-bold tracking-tighter uppercase text-on-surface">CRM de Clientes</h2>
            <p className="text-sm text-slate-500 font-body">Gestión de accesos y perfiles autorizados.</p>
          </div>
          <div className="flex gap-2">
            <button className="px-4 py-2 border border-outline-variant/30 text-[10px] font-bold uppercase text-slate-400 tracking-widest hover:bg-surface-container-low transition-all">Filtrar por Status</button>
            <button className="px-4 py-2 bg-surface-container-high text-primary text-[10px] font-bold uppercase tracking-widest hover:opacity-80">Agregar Cliente</button>
          </div>
        </div>
        <div className="bg-surface-container-low overflow-hidden">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-surface-container-highest">
                <th className="px-6 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest font-label">Identificador</th>
                <th className="px-6 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest font-label">Cliente / Operación</th>
                <th className="px-6 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest font-label">Ubicación Logística</th>
                <th className="px-6 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest font-label">Estatus Sistema</th>
                <th className="px-6 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest font-label text-right">Acción de Comando</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-surface-container-highest/30">
              <tr className="hover:bg-surface-container-high/40 transition-colors group">
                <td className="px-6 py-5 font-headline text-xs font-bold text-primary">#MT-9942</td>
                <td className="px-6 py-5">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-surface-container-highest rounded-sm flex items-center justify-center text-[10px] font-bold">AQ</div>
                    <div className="flex flex-col">
                      <span className="text-sm font-semibold text-on-surface">Alpha Quant Systems</span>
                      <span className="text-[10px] text-slate-500">Hardware de Redes Pesadas</span>
                    </div>
                  </div>
                </td>
                <td className="px-6 py-5 text-xs text-slate-400 font-label">Ciudad de México, MX</td>
                <td className="px-6 py-5">
                  <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[9px] font-bold bg-primary/10 text-primary border border-primary/20 uppercase">Activo</span>
                </td>
                <td className="px-6 py-5 text-right">
                  <button className="text-[10px] font-black uppercase tracking-tighter text-error hover:underline transition-all">Inhabilitar</button>
                </td>
              </tr>
              <tr className="hover:bg-surface-container-high/40 transition-colors">
                <td className="px-6 py-5 font-headline text-xs font-bold text-primary">#MT-8812</td>
                <td className="px-6 py-5">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-surface-container-highest rounded-sm flex items-center justify-center text-[10px] font-bold">NS</div>
                    <div className="flex flex-col">
                      <span className="text-sm font-semibold text-on-surface">Nova Shield Tech</span>
                      <span className="text-[10px] text-slate-500">Geogestión Satelital</span>
                    </div>
                  </div>
                </td>
                <td className="px-6 py-5 text-xs text-slate-400 font-label">Madrid, ES</td>
                <td className="px-6 py-5">
                  <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[9px] font-bold bg-error/10 text-error border border-error/20 uppercase">Inhabilitado</span>
                </td>
                <td className="px-6 py-5 text-right">
                  <button className="text-[10px] font-black uppercase tracking-tighter text-primary hover:underline transition-all">Habilitar</button>
                </td>
              </tr>
              <tr className="hover:bg-surface-container-high/40 transition-colors">
                <td className="px-6 py-5 font-headline text-xs font-bold text-primary">#MT-7756</td>
                <td className="px-6 py-5">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-surface-container-highest rounded-sm flex items-center justify-center text-[10px] font-bold">BC</div>
                    <div className="flex flex-col">
                      <span className="text-sm font-semibold text-on-surface">Bunker Core Labs</span>
                      <span className="text-[10px] text-slate-500">Módulos de Almacenamiento</span>
                    </div>
                  </div>
                </td>
                <td className="px-6 py-5 text-xs text-slate-400 font-label">Bogotá, CO</td>
                <td className="px-6 py-5">
                  <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[9px] font-bold bg-primary/10 text-primary border border-primary/20 uppercase">Activo</span>
                </td>
                <td className="px-6 py-5 text-right">
                  <button className="text-[10px] font-black uppercase tracking-tighter text-error hover:underline transition-all">Inhabilitar</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      {/* Bottom Section: Logistics & Map Concept */}
      <section className="grid grid-cols-1 lg:grid-cols-3 gap-10">
        {/* Logistics Feed */}
        <div className="lg:col-span-1 space-y-6">
          <h3 className="font-headline text-xl font-bold uppercase tracking-tighter text-on-surface">Logística de Pedidos</h3>
          <div className="space-y-4">
            <div className="bg-surface-container-high p-4 flex gap-4">
              <div className="w-10 h-10 shrink-0 bg-[#0f3460] flex items-center justify-center">
                <Truck className="text-primary w-5 h-5" />
              </div>
              <div className="flex-1">
                <div className="flex justify-between items-start mb-1">
                  <span className="text-xs font-bold text-on-surface">ORD-44510</span>
                  <span className="text-[9px] bg-secondary-container text-on-secondary-container px-2 py-0.5 uppercase font-bold">En Camino</span>
                </div>
                <p className="text-[10px] text-slate-400 font-body">Transportando: Firewall Blindado Pro x4</p>
                <div className="mt-2 text-[9px] font-label text-slate-500 uppercase tracking-widest">ETA: 2 Horas</div>
              </div>
            </div>
            <div className="bg-surface-container-high p-4 flex gap-4">
              <div className="w-10 h-10 shrink-0 bg-surface-container-highest flex items-center justify-center border border-primary/10">
                <RefreshCw className="text-primary/40 w-5 h-5" />
              </div>
              <div className="flex-1">
                <div className="flex justify-between items-start mb-1">
                  <span className="text-xs font-bold text-on-surface">ORD-44509</span>
                  <span className="text-[9px] bg-surface-container-low text-slate-400 px-2 py-0.5 uppercase font-bold">Procesando</span>
                </div>
                <p className="text-[10px] text-slate-400 font-body">Ensamblando: Módulo Geostacionario v2</p>
              </div>
            </div>
            <div className="bg-surface-container-high p-4 flex gap-4">
              <div className="w-10 h-10 shrink-0 bg-on-primary-container/20 flex items-center justify-center">
                <CheckCircle className="text-on-primary-container w-5 h-5" />
              </div>
              <div className="flex-1">
                <div className="flex justify-between items-start mb-1">
                  <span className="text-xs font-bold text-on-surface">ORD-44508</span>
                  <span className="text-[9px] bg-on-primary-container text-primary-container px-2 py-0.5 uppercase font-bold">Entregado</span>
                </div>
                <p className="text-[10px] text-slate-400 font-body">Finalizado: Rack Servidores 42U</p>
              </div>
            </div>
          </div>
        </div>

        {/* Geomanagement / Support Access */}
        <div className="lg:col-span-2 space-y-6">
          <div className="flex justify-between items-center">
            <h3 className="font-headline text-xl font-bold uppercase tracking-tighter text-on-surface">Geogestión en Tiempo Real</h3>
            <div className="flex gap-4">
              <div className="flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-primary"></div>
                <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Nodos Online: 42</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-error"></div>
                <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Alertas: 02</span>
              </div>
            </div>
          </div>
          <div className="h-64 bg-surface-container-low relative border border-outline-variant/10 overflow-hidden group">
            <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?auto=format&fit=crop&q=80&w=1200')] bg-cover bg-center grayscale opacity-30 group-hover:opacity-50 transition-opacity"></div>
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="text-center z-10">
                <button className="bg-surface-container-highest/90 backdrop-blur-md px-6 py-3 text-[10px] font-black uppercase tracking-[0.2em] border border-primary/20 hover:bg-primary hover:text-on-primary transition-all">Abrir Terminal Geográfica</button>
              </div>
            </div>
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-48 h-48 border border-primary/20 rounded-full"></div>
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 border border-primary/10 rounded-full"></div>
          </div>
          <div className="grid grid-cols-2 gap-6">
            <div className="bg-surface-container-low p-5 flex items-center justify-between group cursor-pointer hover:bg-surface-container-high">
              <div className="flex flex-col">
                <span className="text-[10px] font-label font-bold text-slate-500 uppercase tracking-widest">Base de Conocimiento</span>
                <span className="text-sm font-bold text-on-surface">Soporte Técnico Especializado</span>
              </div>
              <ArrowRight className="text-primary w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </div>
            <div className="bg-surface-container-low p-5 flex items-center justify-between group cursor-pointer hover:bg-surface-container-high">
              <div className="flex flex-col">
                <span className="text-[10px] font-label font-bold text-slate-500 uppercase tracking-widest">Auditoría Operativa</span>
                <span className="text-sm font-bold text-on-surface">Descargar Reportes Anuales</span>
              </div>
              <Download className="text-primary w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
