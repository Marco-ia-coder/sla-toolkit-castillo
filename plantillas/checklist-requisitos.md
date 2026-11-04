# Checklist de Levantamiento de Requisitos del Cliente (SLR)

Utilice este formato en la fase de entrevista con el cliente (ITIL 4 Service Level Management)[cite: 1, 2].

- [ ] **1. Identificación del Negocio:** ¿Cuál es la actividad principal de la empresa cliente y qué aplicaciones críticas corren sobre la red (ej. VoIP, ERP, Videoconferencia, Bases de datos)?
- [ ] **2. Requerimientos de Ancho de Banda:** ¿Cuál es la tasa de transferencia pico y promedio esperada (Burst / Committed Information Rate - CIR)?
- [ ] **3. Ubicaciones y Topología:** ¿Cuáles son las sedes geográficas a conectar y qué tipo de redundancia o enlaces de respaldo se requieren?
- [ ] **4. Expectativas de Disponibilidad (SLR):** ¿Qué nivel de disponibilidad exige el negocio (ej. 99.9%, 99.99%)?
- [ ] **5. Tolerancia a Latencia y Jitter:** ¿Qué umbrales máximos toleran las aplicaciones en tiempo real (ej. Telefonía IP $\le 150\text{ ms}$ según ITU-T G.114)[cite: 2]?
- [ ] **6. Ventanas de Operación:** ¿Opera el cliente 24/7 o cuenta con horarios específicos donde se puedan programar mantenimientos?
