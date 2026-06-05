import React from "react";
import { Vortex } from "./ui/vortex";
import { ColourfulText } from "./ui/colourful-text";

export default function Hero() {
  return (
    <div className="w-full h-[70vh] overflow-hidden mt-[-8rem]">
      {/* Usamos mt-[-8rem] para que el hero pase por debajo del navbar semi-transparente */}
      <Vortex
        backgroundColor="transparent"
        className="flex items-center flex-col justify-center px-2 md:px-10 py-4 w-full h-full pt-[8rem]"
      >
        <h2 className="text-white text-4xl md:text-7xl font-bold text-center mb-4">
          La Siguiente Era <br /> del <ColourfulText text="Rendimiento" />
        </h2>
        <p className="text-gray-300 text-sm md:text-2xl max-w-2xl text-center mt-6">
          Equípate con el mejor hardware para gamers y profesionales exigentes. Experimenta la verdadera potencia.
        </p>
        <div className="flex flex-col sm:flex-row items-center gap-4 mt-10">
          <a href="/productos/" className="px-8 py-4 bg-blue-600 hover:bg-blue-500 transition duration-300 rounded-full text-white font-bold shadow-[0_0_20px_rgba(37,99,235,0.7)] hover:scale-105 transform">
            Ver Catálogo
          </a>
          <a href="/productos/?categoria=graficas" className="px-8 py-4 bg-transparent border border-white/30 hover:border-white hover:bg-white/10 transition duration-300 rounded-full text-white font-bold backdrop-blur-sm hover:scale-105 transform">
            Tarjetas Gráficas
          </a>
        </div>
      </Vortex>
    </div>
  );
}
