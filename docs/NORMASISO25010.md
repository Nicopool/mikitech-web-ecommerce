markdown

# PROMPT PARA ANTIGRAVITY - EVALUACIÓN ISO/IEC 25010

## CONTEXTO

Necesito que evalúes mi aplicación (que está en desarrollo) contra la norma **ISO/IEC 25010** (calidad de producto y calidad en uso). Quiero identificar qué características cumplo, cuáles tengo parcialmente y cuáles me faltan implementar.

## DESCRIPCIÓN DE LA APLICACIÓN

[COMPLETA ESTA SECCIÓN]

**Nombre del proyecto:** [Nombre de tu app]

**Descripción breve:**
[Explica qué hace tu aplicación, para quién es, cuál es su propósito principal]

**Tecnologías utilizadas:**

- Backend: [Ej: Node.js + Express + PostgreSQL]
- Frontend: [Ej: React + Redux]
- Autenticación: [Ej: JWT + bcrypt]
- Infraestructura: [Ej: AWS, Docker, etc.]
- Otros: [Ej: Redis, WebSockets, etc.]

**Funcionalidades principales:**

1. [Funcionalidad 1]
2. [Funcionalidad 2]
3. [Funcionalidad 3]
...

**Usuarios/roles:**

- [Roles: admin, usuario, invitado, etc.]

**Estado actual del proyecto:**

- [ ] En desarrollo inicial
- [ ] En producción (versión beta)
- [ ] En producción estable
- [ ] En mantenimiento

## OBJETIVO DE LA EVALUACIÓN

Quiero que analices mi aplicación contra las siguientes características de la **ISO/IEC 25010** y me entregues:

### 1. ANÁLISIS POR CARACTERÍSTICA

Para CADA una de las 8 características (y subcaracterísticas), debes:

1. **Definir** la característica en términos simples
2. **Evaluar** si mi aplicación la cumple (✅ Sí, ⚠️ Parcial, ❌ No)
3. **Justificar** por qué cumple o no cumple
4. **Evidenciar** con ejemplos concretos de mi código/arquitectura
5. **Proponer** acciones concretas para mejorar o implementar

**Características a evaluar:**

#### A. ADECUACIÓN FUNCIONAL (Functional Suitability)

- **Exhaustividad funcional:** ¿Cubro todas las funciones especificadas?
- **Corrección funcional:** ¿Las funciones producen resultados correctos?
- **Pertinencia funcional:** ¿Las funciones son apropiadas para las necesidades?

#### B. EFICIENCIA DE RENDIMIENTO (Performance Efficiency)

- **Comportamiento temporal:** ¿Tiempos de respuesta aceptables?
- **Utilización de recursos:** ¿Uso eficiente de CPU, memoria, red?
- **Capacidad:** ¿Puede manejar la carga esperada?

#### C. COMPATIBILIDAD (Compatibility)

- **Coexistencia:** ¿Puede coexistir con otros sistemas?
- **Interoperabilidad:** ¿Intercambia datos con otros sistemas?

#### D. USABILIDAD (Usability)

- **Aprendizaje:** ¿Fácil de aprender para nuevos usuarios?
- **Operabilidad:** ¿Fácil de operar y controlar?
- **Protección contra errores:** ¿Previene errores de usuario?
- **Estética:** ¿Interfaz atractiva y consistente?
- **Accesibilidad:** ¿Accesible para personas con discapacidades?

#### E. FIABILIDAD (Reliability)

- **Madurez:** ¿Frecuencia de fallos aceptable?
- **Disponibilidad:** ¿Tiempo de actividad garantizado?
- **Tolerancia a fallos:** ¿Maneja fallos sin caer?
- **Capacidad de recuperación:** ¿Se recupera de fallos?

#### F. SEGURIDAD (Security)

- **Confidencialidad:** ¿Datos protegidos de accesos no autorizados?
- **Integridad:** ¿Datos protegidos de modificaciones no autorizadas?
- **No repudio:** ¿Se puede probar que una acción ocurrió?
- **Responsabilidad:** ¿Se pueden rastrear acciones de usuarios?
- **Autenticidad:** ¿Verifica identidades correctamente?

#### G. MANTENIBILIDAD (Maintainability)

- **Modularidad:** ¿Código dividido en módulos independientes?
- **Reusabilidad:** ¿Componentes reutilizables?
- **Analizabilidad:** ¿Fácil de diagnosticar problemas?
- **Modificabilidad:** ¿Fácil de hacer cambios?
- **Testabilidad:** ¿Fácil de probar?

#### H. PORTABILIDAD (Portability)

- **Adaptabilidad:** ¿Fácil de adaptar a diferentes entornos?
- **Instalabilidad:** ¿Fácil de instalar/desplegar?
- **Reemplazabilidad:** ¿Fácil de reemplazar por otro sistema?

### 2. CALIDAD EN USO (Quality in Use)

Evaluar:

- **Efectividad:** ¿Los usuarios logran sus objetivos?
- **Eficiencia:** ¿Los usuarios logran objetivos con mínimo esfuerzo?
- **Satisfacción:** ¿Los usuarios están satisfechos?
- **Contexto de uso:** ¿Funciona en el entorno real del usuario?

### 3. PLAN DE ACCIÓN PRIORIZADO

Basado en el análisis, quiero:

1. **Lista de brechas críticas** (lo que falta y es prioritario)
2. **Lista de mejoras recomendadas** (lo que se puede optimizar)
3. **Roadmap de implementación** (orden sugerido para mejorar)
4. **Métricas/KPIs** para medir cada característica
5. **Herramientas sugeridas** para medir cada aspecto

### 4. EJEMPLOS DE MÉTRICAS CUANTITATIVAS

Para cada característica, sugiere métricas medibles:

| Característica | Métrica | Valor Objetivo | Cómo Medirlo |
|----------------|---------|----------------|--------------|
| Rendimiento | Tiempo de carga | < 2 segundos | Lighthouse, GTmetrix |
| Disponibilidad | Uptime | 99.9% | Monitoreo (Pingdom) |
| Seguridad | Vulnerabilidades críticas | 0 | OWASP ZAP, Snyk |
| Mantenibilidad | Deuda técnica | < 5% | SonarQube |
| ... | ... | ... | ... |

### 5. CHECKLIST DE IMPLEMENTACIÓN

Crear checklist de verificación para cada característica:
[ ] ¿Tenemos logs estructurados?
[ ] ¿Hacemos pruebas de carga?
[ ] ¿Tenemos monitoreo de errores?
[ ] ¿Hacemos análisis de vulnerabilidades?
[ ] ¿Tenemos documentación actualizada?
[ ] ¿Hacemos pruebas de usabilidad?
[ ] ...

text

### 6. RECOMENDACIONES ESPECÍFICAS POR TECNOLOGÍA

Basado en mi stack tecnológico, recomienda:

- **Herramientas de testing** (unitarias, integración, E2E, carga)
- **Herramientas de monitoreo** (APM, logs, métricas)
- **Herramientas de seguridad** (SAST, DAST, SCA)
- **Herramientas de calidad de código** (linters, formateadores)
- **Herramientas de documentación** (Swagger, JSDoc, etc.)

## INFORMACIÓN ADICIONAL SOBRE MI PROYECTO

[OPCIONAL: Agrega más detalles]

**Nivel de madurez actual:**

- [ ] No tengo pruebas automatizadas
- [ ] Tengo algunas pruebas unitarias
- [ ] Tengo pruebas unitarias + integración
- [ ] Tengo pruebas unitarias + integración + E2E
- [ ] Tengo CI/CD implementado

**Prácticas actuales:**

- [ ] Code reviews
- [ ] Documentación técnica
- [ ] Monitoreo en producción
- [ ] Alertas/configuración de errores
- [ ] Backup de datos
- [ ] Logs estructurados

**Restricciones:**

- Presupuesto limitado para herramientas pagas
- Equipo pequeño (X desarrolladores)
- Tiempo limitado para implementar mejoras
- Requisitos de cumplimiento normativo adicionales (ej: GDPR, HIPAA)

## FORMATO DE RESPUESTA ESPERADO

Quiero un informe estructurado con:

1. **Resumen ejecutivo** (puntuación general por característica)
2. **Análisis detallado** (cada característica con su evaluación)
3. **Matriz de cumplimiento** (tabla con estado actual vs. deseado)
4. **Plan de acción** (priorizado y con plazos sugeridos)
5. **Anexos** (herramientas sugeridas, métricas, checklists)

## PREGUNTAS ESPECÍFICAS QUE QUIERO RESPONDIDAS

1. ¿Cuáles son las 3 principales brechas de calidad que debo atacar primero?
2. ¿Mi aplicación es suficientemente segura para producción?
3. ¿Qué tan mantenible es mi código actual?
4. ¿Mi arquitectura permite escalar?
5. ¿Qué riesgos debo mitigar antes de lanzar a producción?

## NOTAS ADICIONALES

- Actualmente estamos en [fase de desarrollo/pruebas/producción]
- Tenemos [X] usuarios activos
- El equipo está compuesto por [X] desarrolladores
- Nuestro presupuesto para herramientas es [bajo/medio/alto]
- Queremos enfocarnos especialmente en [usabilidad/seguridad/rendimiento]

---

**Por favor, actúa como un consultor experto en calidad de software y arquitectura, y proporciona una evaluación honesta, detallada y accionable.**
📋 Cómo usar este prompt:
Copia todo el contenido del bloque de código

Completa TODAS las secciones con la información real de tu proyecto

Sé honesto sobre el estado actual (Antigravity te dará mejores recomendaciones)

Pégalo en Antigravity y espera el análisis detallado

🔍 Consejos adicionales:
Para obtener mejores resultados:
Sé específico en la descripción de tu aplicación

Comparte ejemplos de código si es posible (o describe la arquitectura)

Menciona problemas reales que hayas tenido (ej: "la app se cae cuando hay 100 usuarios")

Define prioridades (¿qué es más importante para ti: seguridad, rendimiento o usabilidad?)

Ejemplo de una sección completada:
markdown
**Descripción breve:**
Mi aplicación es un panel de administración para gestionar inventario de una tienda de ropa. Los usuarios pueden ver productos, crear órdenes y gestionar proveedores. Tiene 3 roles: admin, usuario, invitado. Actualmente tiene 50 usuarios activos.

**Tecnologías:**

- Backend: Node.js + Express + PostgreSQL + Prisma
- Frontend: React + TailwindCSS
- Autenticación: JWT + bcrypt
- Infraestructura: Vercel (frontend), Render (backend), Supabase (DB)
📊 ¿Qué esperar del resultado?
Antigravity te dará algo como esto:

text
RESUMEN DE CUMPLIMIENTO ISO/IEC 25010

✅ Adecuación Funcional: 85% - Bueno, pero faltan casos edge
⚠️ Eficiencia de Rendimiento: 60% - Tiempos de carga altos en consultas pesadas
❌ Seguridad: 40% - Falta rate limiting y validación de roles adecuada
⚠️ Usabilidad: 70% - Interfaz limpia pero falta accesibilidad
✅ Mantenibilidad: 80% - Código modular, pero falta documentación
...
