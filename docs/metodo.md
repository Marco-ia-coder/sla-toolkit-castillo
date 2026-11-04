# Método de Diseño de SLA (ITIL 4 e ITU-T E.860)

Este documento detalla el ciclo metodológico de 6 pasos empleado en el toolkit para diseñar, calcular y verificar Acuerdos de Nivel de Servicio (SLA) en redes de telecomunicaciones.

---

## Paso 1: Definir el Servicio
* **Qué se hace:** Se determina con precisión la naturaleza del servicio de red a entregar (ej. Enlace Dedicado, MPLS, SD-WAN), especificando el alcance geográfico, los límites tecnológicos y el **punto de demarcación** exacto entre el proveedor y el cliente.
* **Norma de referencia:** ITU-T E.860.
* **Produce:** Especificación técnica del servicio y diagrama de demarcación de responsabilidades.

## Paso 2: Levantar los Requisitos del Cliente (SLR)
* **Qué se hace:** Se recopilan las necesidades del negocio expresadas en el lenguaje del cliente (Service Level Requirements - SLR), identificando aplicaciones críticas, horarios de operación y criticidad ante fallas.
* **Norma de referencia:** ITIL 4 (Service Level Management).
* **Produce:** Checklist de requisitos y necesidades de negocio validadas.

## Paso 3: Elegir las Métricas (SLI)
* **Qué se hace:** Se seleccionan los Indicadores de Nivel de Servicio (Service Level Indicators - SLI) cuantificables necesarios para evaluar el comportamiento del enlace: Disponibilidad, Retardo (Latencia), Variación de retardo (Jitter), Pérdida de paquetes y Throughput.
* **Norma de referencia:** ITU-T Y.1540 / Y.1541, MEF 10.4 y RFCs de la IETF.
* **Produce:** Matriz de SLIs seleccionados y sus respectivos métodos de medición.

## Paso 4: Fijar Objetivos Viables (SLO)
* **Qué se hace:** Se establecen los Objetivos de Nivel de Servicio (Service Level Objectives - SLO) evaluando estrictamente la capacidad y viabilidad técnica de la infraestructura real (cálculo de enlaces en serie/paralelo, latencia física por distancia), asegurando no comprometer metas inalcanzables.
* **Norma de referencia:** ITIL 4 y cálculos de ingeniería de redes.
* **Produce:** Valores umbrales permitidos (objetivos cuantitativos) para cada SLO.

## Paso 5: Definir Operación y Medición
* **Qué se hace:** Se establecen los protocolos de monitoreo, herramientas de prueba activas/pasivas, el período de medición (ej. mensual), ventanas de mantenimiento excluidas, tiempos de respuesta, MTTR (Mean Time To Repair) y los flujos de escalamiento y reportes.
* **Norma de referencia:** ISO/IEC 20000-1 y RFC 5357 (TWAMP).
* **Produce:** Procedimiento operativo de control y plan de reportes periódicos.

## Paso 6: Definir Consecuencias y Revisión
* **Qué se hace:** Se estipulan las penalizaciones y créditos de servicio aplicables en caso de incumplimiento de los SLOs, implementando un ciclo de mejora continua (PDCA - Plan-Do-Check-Act) para revisar y actualizar el SLA periódicamente.
* **Norma de referencia:** ISO/IEC 20000-1 (Gestión de Servicios).
* **Produce:** Cláusula de compensación económica/créditos y directrices de revisión continua.
