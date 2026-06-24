import { ChevronRight, ArrowRight, ShoppingCart, ArrowLeft, MapPin } from 'lucide-react';

export default function Store() {
  return (
    <div className="max-w-7xl mx-auto px-6 py-10 grid grid-cols-12 gap-8">
      {/* Sidebar Navigation (Filters & Categories) */}
      <aside className="col-span-12 lg:col-span-3 space-y-10">
        {/* Currency Converter */}
        <section className="bg-surface-container-low p-6 rounded-sm border border-outline-variant/10 shadow-sm">
          <h3 className="font-headline text-xs font-bold uppercase tracking-[0.2em] text-on-surface-variant mb-4">Divisa en Tiempo Real</h3>
          <div className="flex items-center justify-between bg-surface-container-highest p-3 rounded-sm">
            <div className="flex items-center gap-2">
              <span className="material-symbols-outlined text-primary text-sm">payments</span>
              <span className="font-label text-sm font-semibold">USD / EUR</span>
            </div>
            <span className="font-headline text-sm text-primary">0.9254</span>
          </div>
        </section>

        {/* Categories Filter */}
        <section>
          <h3 className="font-headline text-xs font-bold uppercase tracking-[0.2em] text-on-surface-variant mb-6">Categorías Blindadas</h3>
          <ul className="space-y-1">
            <li className="group">
              <a className="flex items-center justify-between py-2 px-3 text-sm font-label text-primary bg-surface-container-high rounded-sm" href="#">
                <span>Procesadores (CPUs)</span>
                <ChevronRight className="w-4 h-4" />
              </a>
            </li>
            {['Placas Base', 'GPUs High-End', 'Memoria RAM DDR5', 'Almacenamiento NVMe', 'Refrigeración Líquida', 'Fuentes Modulares', 'Chasis Blindados', 'Workstations', 'Servidores Rack', 'Networking Pro', 'Sensores IoT', 'Módulos GPS L1/L5', 'Terminales RTK'].map((cat) => (
              <li key={cat}>
                <a className="flex items-center justify-between py-2 px-3 text-sm font-label text-on-surface-variant hover:bg-surface-container-high hover:text-primary transition-colors" href="#">
                  {cat}
                </a>
              </li>
            ))}
          </ul>
        </section>

        {/* Technical Filters */}
        <section className="bg-surface-container-low p-6 rounded-sm border border-outline-variant/10">
          <h3 className="font-headline text-xs font-bold uppercase tracking-[0.2em] text-on-surface-variant mb-6">Especificaciones</h3>
          <div className="space-y-6">
            <div>
              <label className="font-label text-xs font-semibold text-on-surface block mb-3">Rango de Frecuencia (GHz)</label>
              <input className="w-full accent-primary bg-surface-container-highest h-1 rounded-full appearance-none" type="range" />
              <div className="flex justify-between text-[10px] mt-2 text-on-tertiary-container">
                <span>2.4 GHz</span>
                <span>6.2 GHz</span>
              </div>
            </div>
            <div className="space-y-2">
              <label className="flex items-center gap-3 cursor-pointer group">
                <input className="rounded-sm border-outline-variant bg-surface-container-highest text-primary focus:ring-primary ring-offset-surface" type="checkbox" />
                <span className="text-sm font-label text-on-surface-variant group-hover:text-on-surface">Certificación IP68</span>
              </label>
              <label className="flex items-center gap-3 cursor-pointer group">
                <input className="rounded-sm border-outline-variant bg-surface-container-highest text-primary focus:ring-primary ring-offset-surface" type="checkbox" />
                <span className="text-sm font-label text-on-surface-variant group-hover:text-on-surface">Redundancia Dual</span>
              </label>
            </div>
          </div>
        </section>
      </aside>

      {/* Product Grid Content */}
      <section className="col-span-12 lg:col-span-9">
        {/* Hero Announcement */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
          <div className="relative bg-surface-container-low p-8 h-[320px] overflow-hidden flex flex-col justify-end group">
            <img alt="GPU RTX Hardware" className="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCjOuukUpVvWi5nIdedOJW5ZJmQ_akx9CpKN5TbDmMSgkFOZRBRUZx12Sw5pMG2iDoWLOfqBVquLFkHZbcS4ZL1ddwxMniLR812PXTnh8I2kdl0uPTADxoao-kOahMqSXFPVILB1mF-EpDeKrRZObOf2M22lB4kPVE0m-2sevTY8LZwFHXHGPvNdAp9vX8FiYxhQ0io09YlmnLw33JrqdF6OcL2NIvXwKOhhV0t-XppKY0odO3ilGXc47RE2Cr8t3lI--8kGSCTZ2Y" />
            <div className="relative z-10">
              <span className="inline-block px-2 py-1 bg-primary text-on-primary text-[10px] font-bold tracking-widest uppercase mb-4">Stock Limitado</span>
              <h2 className="font-headline text-3xl font-bold -tracking-tight mb-4 leading-none">Unidades GPU Quantum-Link®</h2>
              <button className="font-label text-xs font-bold text-primary flex items-center gap-2 group/btn">
                EXPLORAR RENDIMIENTO <ArrowRight className="w-4 h-4 group-hover/btn:translate-x-2 transition-transform" />
              </button>
            </div>
          </div>
          <div className="bg-primary-container p-8 h-[320px] flex flex-col justify-between border border-primary/20">
            <div className="flex justify-between items-start">
              <MapPin className="text-primary w-10 h-10" />
              <div className="text-right">
                <p className="font-headline text-2xl font-bold tracking-tighter text-on-primary-container">GEOGESTIÓN 4.0</p>
                <p className="font-label text-xs text-on-primary-container opacity-60">Sincronización Global Pro</p>
              </div>
            </div>
            <div>
              <p className="font-body text-sm text-on-secondary-container mb-6 max-w-[240px]">Controla tus nodos de hardware con precisión centimétrica desde nuestro panel integrado.</p>
              <a className="inline-block px-6 py-3 bg-primary text-on-primary text-xs font-bold uppercase tracking-widest rounded-sm hover:brightness-110 transition-all" href="#">Ver Módulos RTK</a>
            </div>
          </div>
        </div>

        {/* Product Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-10">
          {/* Card 1 */}
          <div className="flex flex-col gap-6 group">
            <div className="relative aspect-square bg-surface-container-low p-1 overflow-hidden">
              <img alt="Placa Base Pro" className="w-full h-full object-cover opacity-80 group-hover:scale-110 transition-transform duration-500" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC24YTJ9s72BY2ZR9BRqzOhgaZjLUaw8B3YrotaKzX9EKa5P69qTikS-et_Yig4DhxtpMa39R4SSaIJ2mTyh0GElrko5n60UVf3-RAt2WNmR_RQ1BajxzpPfe_A4hmZaG_Sm4K75Xvtjd07ZHu84PCW-WSrskQtUIAW645ZupVet5IZrXA3OFHhg_K6HDx9e7jtH9aW0LxvYmNZXkiqh8Q3_m8E_p9lg-zzQfF9OGYZY9p7TtEZQUbUvLta429ZZ2X1HRpqReUrQ30" />
              <div className="absolute top-4 right-4 flex flex-col gap-2">
                <span className="bg-surface/80 backdrop-blur-md px-2 py-1 text-[10px] font-bold text-primary border border-primary/20">NUEVO</span>
              </div>
            </div>
            <div className="space-y-3">
              <div className="flex justify-between items-start">
                <h4 className="font-headline text-lg font-bold -tracking-tight text-on-surface">MickyCore Z790 Cyber-Armor</h4>
                <span className="font-headline text-lg text-primary">$549.00</span>
              </div>
              <div className="flex gap-2">
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">LGA 1700</span>
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">Wi-Fi 7</span>
              </div>
              <p className="font-body text-xs text-on-surface-variant leading-relaxed">Blindaje térmico integral con soporte nativo para geolocalización de red de baja latencia.</p>
              <button className="w-full py-3 bg-surface-container-highest hover:bg-primary hover:text-on-primary transition-all text-[10px] font-bold uppercase tracking-[0.2em] flex items-center justify-center gap-2">
                <ShoppingCart className="w-4 h-4" /> Añadir al Búnker
              </button>
            </div>
          </div>

          {/* Card 2 */}
          <div className="flex flex-col gap-6 group">
            <div className="relative aspect-square bg-surface-container-low p-1 overflow-hidden">
              <img alt="Modulo GPS" className="w-full h-full object-cover opacity-80 group-hover:scale-110 transition-transform duration-500" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBZbG7nlTJOA3-SDQVAzq7HPjO5p9xqRXEVZXRupNwRXUTMN1A-292EDrEz0TP4pawN22ZEpAqsGrZWcSrimAk7o3Fb5JTFolHlPwOi-q560seSbyudvnPKLqAmf1Hzo1Z7DxbfxtQd-g3C8E76ZFXcdtn1VNScXST1ibqvGoQQWlZ-LiQrKXxX9gS69zh-eVS5vgT6dTdU0DB-AzXMLZykDGjhQwoKy3j1s2Ao9xmWuOEjBiHDjDF3alrhGiCuLpGIRVhJte-MKr4" />
            </div>
            <div className="space-y-3">
              <div className="flex justify-between items-start">
                <h4 className="font-headline text-lg font-bold -tracking-tight text-on-surface">Terminal RTK Geo-Pulse X1</h4>
                <span className="font-headline text-lg text-primary">$1,299.00</span>
              </div>
              <div className="flex gap-2">
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">±1cm Prec.</span>
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">IP67</span>
              </div>
              <p className="font-body text-xs text-on-surface-variant leading-relaxed">Módulo de geogestión industrial para mapeo de precisión. Compatible con MickyCloud Sync.</p>
              <button className="w-full py-3 bg-surface-container-highest hover:bg-primary hover:text-on-primary transition-all text-[10px] font-bold uppercase tracking-[0.2em] flex items-center justify-center gap-2">
                <ShoppingCart className="w-4 h-4" /> Añadir al Búnker
              </button>
            </div>
          </div>

          {/* Card 3 */}
          <div className="flex flex-col gap-6 group">
            <div className="relative aspect-square bg-surface-container-low p-1 overflow-hidden">
              <img alt="SSD Pro" className="w-full h-full object-cover opacity-80 group-hover:scale-110 transition-transform duration-500" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCEKB8L1Pmmuf1-nMjI0dt-6Zs4WONUnhKck3EEZTh_IjoNSBhAtNEocLvRBGcxu9O9P0whRpaGv5wURDFbJ3We-IwrY04iZ_u089nhBej1Y_0PN_70-uXmGT2eOygWc2GFQNc_EQ2jac5Zs4kKZi91-4qrSlpBusNlkNMoJQv6RHBlr0PPfBusZAbzJxsHa68KQ9VWWP4nw8GiB-IXlLV1z9R3PDWYfUzrcpx7nD9qeEBHzQg2f1HC1oun1lXue4jMtne7Y6RJDZg" />
              <div className="absolute bottom-4 left-4">
                <span className="bg-error-container text-on-error-container px-2 py-1 text-[10px] font-bold">SALE -20%</span>
              </div>
            </div>
            <div className="space-y-3">
              <div className="flex justify-between items-start">
                <h4 className="font-headline text-lg font-bold -tracking-tight text-on-surface">Titan-Drive NVMe 4TB</h4>
                <div className="flex flex-col items-end">
                  <span className="font-headline text-lg text-primary">$319.00</span>
                  <span className="text-[10px] text-on-surface-variant line-through">$399.00</span>
                </div>
              </div>
              <div className="flex gap-2">
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">7500 MB/s</span>
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">AES-256</span>
              </div>
              <p className="font-body text-xs text-on-surface-variant leading-relaxed">Cifrado de grado militar y velocidades de acceso instantáneo para estaciones de datos.</p>
              <button className="w-full py-3 bg-surface-container-highest hover:bg-primary hover:text-on-primary transition-all text-[10px] font-bold uppercase tracking-[0.2em] flex items-center justify-center gap-2">
                <ShoppingCart className="w-4 h-4" /> Añadir al Búnker
              </button>
            </div>
          </div>

          {/* Card 4 */}
          <div className="flex flex-col gap-6 group">
            <div className="relative aspect-square bg-surface-container-low p-1 overflow-hidden">
              <img alt="Servidor Rack" className="w-full h-full object-cover opacity-80 group-hover:scale-110 transition-transform duration-500" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDh-p0oNu20NGr2I2MAXK4qdQTVxyAXsmX7JrpXxwEHUixIXINC6RG4aT0koBaPvb-MJ4RWksPYZQWS46L_uGgO4JcFTYSj8HbTZLfah53wrhKm_62zVWM9txosQNWvskf1AfgSQ0NA2lCCVQIre5Z3TxfmA_qp5JpUEbYn0CVzjh2pkxHOskZ0DeY49claeLN9QvIm1Fs38HcLDUUGoXua9qnuypdwlS1NRf_7Wcwc4xV14Ayq_qzfHjLnW36ePiQwg86gMz7OmEI" />
            </div>
            <div className="space-y-3">
              <div className="flex justify-between items-start">
                <h4 className="font-headline text-lg font-bold -tracking-tight text-on-surface">MickyRack Node V2</h4>
                <span className="font-headline text-lg text-primary">$2,450.00</span>
              </div>
              <div className="flex gap-2">
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">2U Rack</span>
                <span className="px-2 py-1 bg-surface-container-highest text-[10px] font-label font-medium text-on-tertiary-container rounded-sm uppercase tracking-wider">Dual CPU</span>
              </div>
              <p className="font-body text-xs text-on-surface-variant leading-relaxed">Infraestructura centralizada para despliegues masivos de hardware y procesamiento.</p>
              <button className="w-full py-3 bg-surface-container-highest hover:bg-primary hover:text-on-primary transition-all text-[10px] font-bold uppercase tracking-[0.2em] flex items-center justify-center gap-2">
                <ShoppingCart className="w-4 h-4" /> Añadir al Búnker
              </button>
            </div>
          </div>
        </div>

        {/* Pagination */}
        <div className="mt-20 flex justify-center items-center gap-4">
          <button className="w-10 h-10 flex items-center justify-center border border-outline-variant/30 text-on-surface-variant hover:border-primary transition-colors">
            <ArrowLeft className="w-5 h-5" />
          </button>
          <div className="flex items-center gap-2">
            <span className="w-10 h-10 flex items-center justify-center bg-primary text-on-primary font-headline text-sm font-bold">1</span>
            <span className="w-10 h-10 flex items-center justify-center text-on-surface-variant font-headline text-sm hover:text-primary transition-colors cursor-pointer">2</span>
            <span className="w-10 h-10 flex items-center justify-center text-on-surface-variant font-headline text-sm hover:text-primary transition-colors cursor-pointer">3</span>
          </div>
          <button className="w-10 h-10 flex items-center justify-center border border-outline-variant/30 text-on-surface-variant hover:border-primary transition-colors">
            <ArrowRight className="w-5 h-5" />
          </button>
        </div>
      </section>
    </div>
  );
}
