import { ChevronRight, ArrowRight, ShoppingCart, Star } from 'lucide-react';

const products = [
  {
    title: "Curiosity3",
    category: "Tarjetas Gráficas",
    price: 2700000,
    originalPrice: 3000000,
    discount: "-10%",
    image: "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&q=80&w=800",
    stock: "Stock Disponible",
    rating: 0,
  },
  {
    title: "Robito",
    category: "Robots",
    price: 5000000,
    image: "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&q=80&w=800",
    stock: "Stock Disponible",
    rating: 0,
  },
  {
    title: "NVIDIA Monitores Pro-8882",
    category: "Monitores",
    price: 3857487,
    image: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&q=80&w=800",
    stock: "Stock Disponible",
    rating: 1,
  },
  {
    title: "MSI Monitores Pro-3311",
    category: "Monitores",
    price: 2450074,
    image: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&q=80&w=800",
    stock: "Agotado",
    rating: 1,
  },
  {
    title: "AMD Monitores Pro-9102",
    category: "Monitores",
    price: 3746376,
    image: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&q=80&w=800",
    stock: "Stock Disponible",
    rating: 1,
  },
  {
    title: "NVIDIA Refrigeración Pro-8581",
    category: "Refrigeración",
    price: 191237,
    image: "https://images.unsplash.com/photo-1616440347437-b1c73416efc2?auto=format&fit=crop&q=80&w=800",
    stock: "Stock Disponible",
    rating: 0,
  },
];

export default function Store() {
  return (
    <div>
      {/* Hero Banners */}
      <section className="max-w-7xl mx-auto px-6 pt-8 pb-12 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="relative bg-white rounded-lg overflow-hidden group shadow-sm border border-outline-variant">
          <img
            alt="Tarjetas Gráficas MIKITECH"
            className="w-full h-[320px] object-cover group-hover:scale-105 transition-transform duration-700"
            src="https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&q=80&w=2000"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent p-8 flex flex-col justify-end">
            <p className="text-white/80 text-sm font-medium tracking-wider uppercase mb-2">Rendimiento Extremo</p>
            <h2 className="text-white text-3xl font-bold font-headline mb-3">Tarjetas Gráficas de Última Generación</h2>
            <p className="text-white/70 text-sm mb-4 max-w-md">Experimenta trazado de rayos en tiempo real y aceleración por IA con las nuevas GPUs de arquitectura avanzada.</p>
            <a className="inline-flex items-center gap-2 bg-primary text-on-primary px-6 py-3 rounded-sm text-xs font-bold uppercase tracking-wider w-fit hover:brightness-110 transition-all" href="#">
              Explorar GPUs <ArrowRight className="w-4 h-4" />
            </a>
          </div>
        </div>
        <div className="relative bg-white rounded-lg overflow-hidden group shadow-sm border border-outline-variant">
          <img
            alt="Procesadores MIKITECH"
            className="w-full h-[320px] object-cover group-hover:scale-105 transition-transform duration-700"
            src="https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&q=80&w=2000"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent p-8 flex flex-col justify-end">
            <p className="text-white/80 text-sm font-medium tracking-wider uppercase mb-2">Cómputo Avanzado</p>
            <h2 className="text-white text-3xl font-bold font-headline mb-3">Procesadores Extremos</h2>
            <p className="text-white/70 text-sm mb-4 max-w-md">Poder multinúcleo para streaming, gaming pesado y creación de contenido 3D sin límites.</p>
            <a className="inline-flex items-center gap-2 bg-primary text-on-primary px-6 py-3 rounded-sm text-xs font-bold uppercase tracking-wider w-fit hover:brightness-110 transition-all" href="#">
              Ver Procesadores <ArrowRight className="w-4 h-4" />
            </a>
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="max-w-7xl mx-auto px-6 pb-16">
        <div className="flex items-center justify-between mb-8">
          <h3 className="font-headline text-2xl font-bold text-on-surface">Productos Destacados</h3>
          <a className="text-primary text-sm font-medium hover:underline flex items-center gap-1" href="#">
            Ver todos <ArrowRight className="w-4 h-4" />
          </a>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {products.map((product) => (
            <div key={product.title} className="bg-white rounded-lg border border-outline-variant shadow-sm hover:shadow-md transition-all group">
              <div className="relative aspect-square overflow-hidden bg-surface-container">
                <img
                  alt={product.title}
                  className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                  src={product.image}
                />
                {product.discount && (
                  <span className="absolute top-3 left-3 bg-error text-on-error-container text-[10px] font-bold px-2 py-1 rounded-sm">{product.discount}</span>
                )}
              </div>
              <div className="p-4 space-y-3">
                <p className="text-[10px] text-on-surface-variant uppercase tracking-wider font-medium">{product.category}</p>
                <h4 className="font-headline font-bold text-on-surface text-sm leading-tight">{product.title}</h4>
                <div className="flex items-center gap-1">
                  {Array.from({ length: 5 }).map((_, i) => (
                    <Star key={i} className={`w-3 h-3 ${i < product.rating ? 'text-brand-orange fill-brand-orange' : 'text-outline'}`} />
                  ))}
                  <span className="text-[10px] text-on-surface-variant ml-1">({product.rating})</span>
                </div>
                <p className={`text-[10px] font-medium ${product.stock === 'Agotado' ? 'text-error' : 'text-green-600'}`}>{product.stock}</p>
                <div className="flex items-center gap-2">
                  <span className="font-headline font-bold text-on-surface text-lg">${product.price.toLocaleString('es-CO')}</span>
                  {product.originalPrice && (
                    <span className="text-on-surface-variant text-xs line-through">${product.originalPrice.toLocaleString('es-CO')}</span>
                  )}
                </div>
                <p className="text-[10px] text-green-700 font-medium">Envío gratis • 1 año garantía</p>
                <div className="flex gap-2 pt-1">
                  <a className="flex-1 text-center text-xs font-medium text-primary border border-primary py-2 rounded-sm hover:bg-primary-container transition-colors" href="#">
                    Detalles
                  </a>
                  <button className={`flex-1 text-xs font-bold uppercase tracking-wider py-2 rounded-sm transition-all flex items-center justify-center gap-1 ${product.stock === 'Agotado' ? 'bg-outline text-white cursor-not-allowed' : 'bg-primary text-on-primary hover:brightness-110'}`}>
                    <ShoppingCart className="w-3 h-3" />
                    {product.stock === 'Agotado' ? 'Agotado' : 'Agregar'}
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Secondary Banners */}
      <section className="max-w-7xl mx-auto px-6 pb-16 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="relative bg-white rounded-lg overflow-hidden group shadow-sm border border-outline-variant">
          <img
            alt="SSD Almacenamiento"
            className="w-full h-[280px] object-cover group-hover:scale-105 transition-transform duration-700"
            src="https://images.unsplash.com/photo-1562976540-1502c2145186?auto=format&fit=crop&q=80&w=2000"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent p-6 flex flex-col justify-end">
            <p className="text-white/80 text-[10px] font-bold tracking-wider uppercase mb-1">Velocidad Pura</p>
            <h3 className="text-white text-xl font-bold font-headline mb-2">Almacenamiento SSD NVMe</h3>
            <a className="text-white text-xs font-medium hover:underline flex items-center gap-1" href="#">
              Ver Almacenamiento <ArrowRight className="w-3 h-3" />
            </a>
          </div>
        </div>
        <div className="relative bg-white rounded-lg overflow-hidden group shadow-sm border border-outline-variant">
          <img
            alt="Gabinetes"
            className="w-full h-[280px] object-cover group-hover:scale-105 transition-transform duration-700"
            src="https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&q=80&w=2000"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent p-6 flex flex-col justify-end">
            <p className="text-white/80 text-[10px] font-bold tracking-wider uppercase mb-1">Flujo de Aire Optimizado</p>
            <h3 className="text-white text-xl font-bold font-headline mb-2">Gabinetes y Refrigeración Premium</h3>
            <a className="text-white text-xs font-medium hover:underline flex items-center gap-1" href="#">
              Explorar Gabinetes <ArrowRight className="w-3 h-3" />
            </a>
          </div>
        </div>
        <div className="relative bg-white rounded-lg overflow-hidden group shadow-sm border border-outline-variant">
          <img
            alt="Periféricos"
            className="w-full h-[280px] object-cover group-hover:scale-105 transition-transform duration-700"
            src="https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&q=80&w=2000"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent p-6 flex flex-col justify-end">
            <p className="text-white/80 text-[10px] font-bold tracking-wider uppercase mb-1">Setup Profesional</p>
            <h3 className="text-white text-xl font-bold font-headline mb-2">Periféricos de Alto Rendimiento</h3>
            <a className="text-white text-xs font-medium hover:underline flex items-center gap-1" href="#">
              Ver Periféricos <ArrowRight className="w-3 h-3" />
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}