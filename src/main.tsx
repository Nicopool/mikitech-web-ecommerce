import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import Hero from './components/Hero.tsx';
import './index.css';

const heroContainer = document.getElementById('react-hero');
if (heroContainer) {
  createRoot(heroContainer).render(
    <StrictMode>
      <Hero />
    </StrictMode>,
  );
}
