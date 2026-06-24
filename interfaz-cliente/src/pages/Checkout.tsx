import { Truck, CreditCard, Landmark, Wallet, Lock, Receipt, ShieldCheck } from 'lucide-react';

export default function Checkout() {
  return (
    <div className="max-w-7xl mx-auto px-6 py-12">
      <header className="mb-12">
        <h1 className="font-headline text-5xl font-extrabold tracking-tighter text-primary mb-2">Finalizar Compra</h1>
        <p className="font-label text-on-surface-variant tracking-wide">CONFIRMACIÓN DE ADQUISICIÓN DE HARDWARE Y LICENCIAS</p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        <section className="lg:col-span-7 space-y-10">
          <div className="bg-surface-container-low p-8 rounded-sm">
            <div className="flex items-center gap-3 mb-8 border-b border-surface-container-highest pb-4">
              <Truck className="text-primary w-6 h-6" />
              <h2 className="font-headline text-xl font-bold uppercase tracking-tight text-on-surface">Datos de Envío</h2>
            </div>
            <form className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <label className="font-label text-xs uppercase text-on-tertiary-container">Nombre Completo</label>
                <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface placeholder:text-outline-variant outline-none" placeholder="Ej. Juan Pérez" type="text" />
              </div>
              <div className="space-y-2">
                <label className="font-label text-xs uppercase text-on-tertiary-container">Correo Corporativo</label>
                <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface placeholder:text-outline-variant outline-none" placeholder="usuario@empresa.com" type="email" />
              </div>
              <div className="md:col-span-2 space-y-2">
                <label className="font-label text-xs uppercase text-on-tertiary-container">Dirección de Entrega</label>
                <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface placeholder:text-outline-variant outline-none" placeholder="Calle, Número, Oficina/Depto" type="text" />
              </div>
              <div className="space-y-2">
                <label className="font-label text-xs uppercase text-on-tertiary-container">Ciudad</label>
                <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface placeholder:text-outline-variant outline-none" placeholder="Ciudad" type="text" />
              </div>
              <div className="space-y-2">
                <label className="font-label text-xs uppercase text-on-tertiary-container">Código Postal</label>
                <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface placeholder:text-outline-variant outline-none" placeholder="00000" type="text" />
              </div>
            </form>
          </div>

          <div className="bg-surface-container-low p-8 rounded-sm">
            <div className="flex items-center gap-3 mb-8 border-b border-surface-container-highest pb-4">
              <CreditCard className="text-primary w-6 h-6" />
              <h2 className="font-headline text-xl font-bold uppercase tracking-tight text-on-surface">Método de Pago</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <label className="relative cursor-pointer group">
                <input defaultChecked className="peer sr-only" name="payment" type="radio" />
                <div className="p-4 bg-surface-container-highest border border-transparent peer-checked:border-primary peer-checked:bg-primary-container/20 rounded-sm transition-all h-full flex flex-col items-center justify-center text-center gap-2">
                  <CreditCard className="w-8 h-8" />
                  <span className="font-label text-sm font-bold uppercase">Tarjeta</span>
                </div>
              </label>
              <label className="relative cursor-pointer group">
                <input className="peer sr-only" name="payment" type="radio" />
                <div className="p-4 bg-surface-container-highest border border-transparent peer-checked:border-primary peer-checked:bg-primary-container/20 rounded-sm transition-all h-full flex flex-col items-center justify-center text-center gap-2">
                  <Landmark className="w-8 h-8" />
                  <span className="font-label text-sm font-bold uppercase">Transferencia</span>
                </div>
              </label>
              <label className="relative cursor-pointer group">
                <input className="peer sr-only" name="payment" type="radio" />
                <div className="p-4 bg-surface-container-highest border border-transparent peer-checked:border-primary peer-checked:bg-primary-container/20 rounded-sm transition-all h-full flex flex-col items-center justify-center text-center gap-2">
                  <Wallet className="w-8 h-8" />
                  <span className="font-label text-sm font-bold uppercase">Cripto/B2B</span>
                </div>
              </label>
            </div>

            <div className="mt-8 space-y-4">
              <div className="space-y-2">
                <label className="font-label text-xs uppercase text-on-tertiary-container">Número de Tarjeta</label>
                <div className="relative">
                  <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface tracking-widest placeholder:text-outline-variant outline-none" placeholder="0000 0000 0000 0000" type="text" />
                  <Lock className="absolute right-4 top-1/2 -translate-y-1/2 text-outline-variant w-4 h-4" />
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-2">
                  <label className="font-label text-xs uppercase text-on-tertiary-container">Expiración</label>
                  <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface placeholder:text-outline-variant outline-none" placeholder="MM/YY" type="text" />
                </div>
                <div className="space-y-2">
                  <label className="font-label text-xs uppercase text-on-tertiary-container">CVV</label>
                  <input className="w-full bg-surface-container-highest border-none focus:ring-1 focus:ring-primary rounded-sm py-3 px-4 text-on-surface placeholder:text-outline-variant outline-none" placeholder="***" type="password" />
                </div>
              </div>
            </div>
          </div>
        </section>

        <aside className="lg:col-span-5 space-y-6">
          <div className="bg-surface-container-high p-8 rounded-sm shadow-2xl relative overflow-hidden border border-outline-variant/10">
            <div className="absolute top-0 right-0 p-4 opacity-10">
              <Receipt className="w-32 h-32" />
            </div>
            <h2 className="font-headline text-2xl font-black uppercase tracking-tighter text-primary mb-8">Resumen de Orden</h2>
            
            <div className="space-y-6 border-b border-surface-container-highest pb-8">
              <div className="flex gap-4 items-center">
                <div className="w-16 h-16 bg-surface-container-lowest rounded-sm p-2">
                  <img alt="Hardware 1" className="w-full h-full object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBLUhLNM1ZytTkBLIAs5e8F-9gUuZTFcvimN3zoBM7EnY0WTW_KCWV7gfFyXEzQZcyS-z6QhqILty4HX3AI2U8rgPU4AcyUaYpfRl4jewuTPzwZGQSkT30NwCnxU0HN43epB1-8L_HQSyWoxELu22YHuaKQd-k-qrcr3D4k3m9B-OD-19GHnh1rqoqFSdxGLI03DezopOs_m27JdzvkvzzM9vPBqACHj9AOhvg9Pz3p1XRBwEGlQ7pFALtPwlVdHZVCW87sajESZS0" />
                </div>
                <div className="flex-1">
                  <p className="font-headline text-sm font-bold text-on-surface">Micky-Link G5000</p>
                  <p className="font-label text-xs text-on-tertiary-container">Hardware de Geogestión</p>
                </div>
                <p className="font-headline text-sm font-bold text-primary">$1,250.00</p>
              </div>
              
              <div className="flex gap-4 items-center">
                <div className="w-16 h-16 bg-surface-container-lowest rounded-sm p-2">
                  <img alt="Hardware 2" className="w-full h-full object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD3We0l1J3T34-o920JTky-BA1Bz9vEvLMPg9Z8BOGhRL4IXG153rUU7IccHx-XqmtCj4ZmvCp72Mtm6Z_Ap9A_64TceVOrDCq_tzXehwDObkWtsUMPYj8IUsqoIaveAhg8fHnOjchlM9mOzF9Fey_jX0OW1IcXvuRZCsKYO932r9Jf3roS8lNwvF6FhlsBnhPt9syitKSGApdzdKpv6YhiUeGc0PNMqwfhX-VYIW3psqXXrVF1OIEULCJu7lRTrr7NfmgIroK0yqo" />
                </div>
                <div className="flex-1">
                  <p className="font-headline text-sm font-bold text-on-surface">Pro-Sentinel Core v2</p>
                  <p className="font-label text-xs text-on-tertiary-container">Unidad de Blindaje</p>
                </div>
                <p className="font-headline text-sm font-bold text-primary">$890.00</p>
              </div>
            </div>

            <div className="py-8 space-y-4 font-label">
              <div className="flex justify-between text-sm">
                <span className="text-on-tertiary-container uppercase tracking-widest">Subtotal</span>
                <span className="text-on-surface">$2,140.00</span>
              </div>
              <div className="flex justify-between text-sm">
                <span className="text-on-tertiary-container uppercase tracking-widest">Impuestos (IVA 16%)</span>
                <span className="text-on-surface">$342.40</span>
              </div>
              <div className="flex justify-between text-sm">
                <span className="text-on-tertiary-container uppercase tracking-widest">Envío Prioritario</span>
                <span className="text-secondary">GRATIS</span>
              </div>
              <div className="flex justify-between items-end pt-4 border-t border-surface-container-highest mt-4">
                <span className="font-headline text-lg font-black uppercase text-on-surface">Total Inversión</span>
                <span className="font-headline text-3xl font-black text-primary">$2,482.40</span>
              </div>
            </div>

            <button className="w-full bg-gradient-to-r from-primary to-on-primary-container py-5 rounded-sm font-headline text-lg font-black uppercase tracking-widest text-on-primary hover:brightness-110 active:scale-[0.98] transition-all shadow-lg shadow-primary/20">
              Confirmar Blindaje de Compra
            </button>
            <div className="mt-6 flex items-center justify-center gap-2 text-xs text-on-tertiary-container uppercase tracking-tighter">
              <ShieldCheck className="w-4 h-4" />
              Encriptación de Grado Militar AES-256 Activa
            </div>
          </div>

          <div className="bg-surface-container-low p-6 rounded-sm border-l-4 border-secondary/30">
            <p className="font-label text-xs text-on-tertiary-container leading-relaxed uppercase">
              Al confirmar, se generará una factura profesional autorizada que será enviada a su portal de administración y correo corporativo.
            </p>
          </div>
        </aside>
      </div>
    </div>
  );
}
