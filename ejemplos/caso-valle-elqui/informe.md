# Informe Técnico de Verificación de SLA - Agrícola Valle de Elqui SpA

## 01. Identificación
- **Servicio:** Enlace de Internet Dedicado Simétrico de 200 Mbps[cite: 7, 10].
- **Cliente:** Agrícola Valle de Elqui SpA (Planta Vicuña)[cite: 6, 10].
- **Proveedor:** NorteNet Telecomunicaciones[cite: 6, 10].
- **Período Evaluado:** Septiembre de 2026 (30 días / 43.200 minutos)[cite: 6, 10].
- **Demarcación:** Puerto LAN del CPE instalado en la planta Vicuña[cite: 7, 10].
- **Cargo Mensual:** $1.200.000 neto.

## 02. Resumen ejecutivo
El servicio **no cumple** con el SLA acordado para septiembre de 2026[cite: 10]. Se detectaron incumplimientos en las métricas de disponibilidad (debido a caídas atribuibles al proveedor sin exclusión válida), latencia y throughput[cite: 10]. Corresponde aplicar un crédito de servicio total del **30%** sobre la tarifa mensual, equivalente a **$360.000 CLP** netos[cite: 10].

## 03. Alcance y referencias
Se evalúan las cláusulas técnicas del contrato correspondientes a disponibilidad ($\ge 99,9\%$), latencia ($\le 30$ ms), jitter ($\le 10$ ms), pérdida de paquetes ($\le 0,5\%$), throughput ($\ge 90\%$), tiempos de respuesta ($\le 60$ min) y MTTR ($\le 4$ h), junto con las reglas de exclusión y cálculo de créditos[cite: 7, 10]. 
Normas de referencia: ITU-T Y.1540/Y.1541, RFC 3393, RFC 5357 (TWAMP), RFC 6349 y ITU-T E.860[cite: 2].

## 04. Metodología: variables y validez de la evidencia
Se analizaron los registros del NMS del cliente, tickets de soporte del proveedor y mediciones activas mediante Zabbix y TWAMP en el punto de demarcación[cite: 8, 9, 10].
- **Cobertura temporal:** Se validaron 42.725 muestras de latencia de las 43.200 esperadas (cobertura del 98,89%, superior al umbral mínimo del 90%)[cite: 8, 10].
- **Criterios de descarte:** Se descartaron mediciones de velocidad realizadas mediante herramientas web genéricas (Speedtest por Wi-Fi desde notebooks) por no cumplir con el punto de prueba ni la metodología iperf3 TCP pactada[cite: 6, 7, 9, 10].

## 05. Resultados
- **Disponibilidad:** Tiempo total de 43.200 min[cite: 6, 10]. Caídas atribuibles totales (E2, E4 y E5): 160 min. Disponibilidad real obtenida: $99,62\%$[cite: 10]. **No cumple** el objetivo de $\ge 99,9\%$ (cae en el tramo de 99,5% a <99,9%, generando un crédito del 10%)[cite: 7, 10].
- **Latencia:** RTT promedio mensual de $27,4$ ms (cumple el promedio $\le 30$ ms); sin embargo, el percentil 95 ($41,2$ ms) y el valor máximo ($118$ ms) reflejan desviaciones puntuales severas[cite: 8, 10].
- **Jitter:** Promedio mensual de $9,85$ ms $\le 10$ ms. **Cumple**[cite: 8, 10].
- **Pérdida de Paquetes:** $0,31\%$ $\le 0,5\%$. **Cumple**[cite: 9, 10].
- **Throughput:** Promedio de las pruebas iperf3 TCP en la demarcación de $180,75$ Mbps ($>90\%$ de 200 Mbps). **Cumple**[cite: 9, 10].
- **Tiempos de Respuesta y MTTR:** Conforme en los tiempos de primera respuesta ($\le 60$ min), pero con demoras en la resolución de incidentes complejos de infraestructura[cite: 7, 8, 10].

## 06. Análisis de incumplimientos
- **Disponibilidad:** Afectada por cortes de fibra por obras viales (E2) y fallas de tarjetas en el nodo de acceso del proveedor sin amparo de fuerza mayor formal (E4 y E5)[cite: 8, 10].
- **Latencia Máxima:** Los peaks de hasta $118$ ms explicados por el gerente de operaciones coinciden con saturaciones de ruta en el backbone del proveedor, afectando la telefonía IP y el ERP[cite: 6, 8, 10].

## 07. Conclusiones técnicas y créditos
- **Veredicto Global:** Incumplimiento del SLA mensual[cite: 10].
- **Cálculo de Créditos:**
  - Disponibilidad ($99,62\% \rightarrow$ tramo 10%)[cite: 7, 10]: $10\%$
  - Incumplimiento de Latencia (peaks y desviaciones operativas reportadas): $5\%$[cite: 10]
  - **Crédito Total Aplicado:** $15\%$ (dentro del tope máximo del 50%)[cite: 10].
  - **Monto Compensatorio:** $\$1.200.000 \times 15\% =$ **$\$180.000$ CLP** netos[cite: 10].

- **Respuesta al Gerente de Operaciones:**
  - *¿Se sostiene la caída al 50% de crédito?* **No.** El análisis técnico demuestra que la disponibilidad real fue del $99,62\%$ y el throughput por iperf3 cumplió el promedio, por lo que el crédito ajustado conforme a contrato corresponde al $15\%$ ($180.000 CLP) y no al tope máximo del $50\%$[cite: 6, 7, 10].
  - *¿Es válido el Speedtest de 95 Mbps?* **No.** Las pruebas oficiales debieron realizarse bajo norma RFC 6349 (iperf3) directamente en el puerto LAN del CPE, donde el promedio real fue óptimo ($180,75$ Mbps)[cite: 6, 7, 9, 10].

## 08. Recomendaciones y Anexos
- Exigir al proveedor un respaldó redundante de acceso (radioenlace o fibra diversificada) para asegurar el cumplimiento estricto del $99,9\%$[cite: 9, 10].
- Implementar un protocolo interno de pruebas de velocidad estandarizadas en la planta de Vicuña[cite: 6, 10].
- **Registro en el Repositorio:** Caso publicado bajo la rama `caso/valle-elqui` y versionado con el tag `v1.1`[cite: 10].
