# Acuerdo de Nivel de Servicio (SLA) - [Nombre del Servicio]

## 1. Partes Involucradas
* **Proveedor:** [Nombre de la Empresa / Proveedor de Telecomunicaciones]
* **Cliente:** [Nombre de la Empresa Cliente / Institución]
* **Fecha de Vigencia:** [DD/MM/AAAA]

## 2. Descripción del Servicio y Demarcación
* **Tipo de Servicio:** [Ej. Enlace Dedicado de Internet / MPLS / VPN]
* **Ancho de Banda / Capacidad:** [Ej. 100 Mbps Simétrico]
* **Punto de Demarcación:** [Descripción física del equipo o interfaz donde termina la responsabilidad del proveedor y comienza la del cliente, según ITU-T E.860]

## 3. Objetivos de Nivel de Servicio (SLO)
| Métrica (SLI) | Objetivo Acordado (SLO) | Norma de Referencia |
| :--- | :--- | :--- |
| **Disponibilidad** | $\ge [99.9]\%$ | ITU-T Y.1540 |
| **Latencia (Retardo)** | $\le [20]\text{ ms}$ | ITU-T Y.1541 / G.114 |
| **Jitter (Variación)** | $\le [5]\text{ ms}$ | RFC 3393 |
| **Pérdida de Paquetes** | $\le [0.1]\%$ | ITU-T Y.1540 |
| **Throughput TCP** | $\ge [95]\%$ del nominal | RFC 6349 |

## 4. Operación, Soporte y Ventanas de Mantenimiento
* **Horario de Soporte:** [Ej. 24/7/365]
* **Tiempo Medio de Respuesta (MTTR estimado):** [Ej. 4 horas]
* **Ventanas de Mantenimiento Programado:** [Ej. Domingos de 02:00 a 06:00 AM]

## 5. Consecuencias y Créditos por Incumplimiento
* Si el cumplimiento mensual del SLO de disponibilidad cae por debajo del objetivo, se aplicarán créditos proporcionales sobre la factura mensual según la tabla de penalizaciones establecida.
