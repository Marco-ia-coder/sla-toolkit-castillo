# Fórmulas y Modelos de Cálculo para SLA de Red

Este documento recopila las fórmulas matemáticas y de ingeniería de redes utilizadas en el toolkit para calcular el rendimiento, disponibilidad, eficiencia y compensaciones de los servicios[cite: 3].

---

## 1. Disponibilidad Porcentual y Caída Permitida

Permite calcular el porcentaje de tiempo que el servicio se encuentra operativo frente al tiempo total del período de medición, así como el tiempo máximo de inactividad tolerado (downtime) para cumplir con el SLO.

* **Fórmula de Disponibilidad:**
  $$\text{Disponibilidad (\%)} = \left(1 - \frac{\text{Tiempo de Inactividad (Downtime)}}{\text{Tiempo Total del Período}}\right) \times 100$$

* **Fórmula de Caída Permitida:**
  $$\text{Downtime Máximo} = \text{Tiempo Total} \times \left(1 - \frac{\text{SLO Target}}{100}\right)$$

* **Variables y Unidades:**
  * $\text{Downtime}$: Tiempo total de interrupción (Horas o Minutos).
  * $\text{Tiempo Total}$: Duración total del período (ej. un mes de 30 días = $720\text{ horas} = 43,200\text{ minutos}$).
  * $\text{SLO Target}$: Porcentaje objetivo de disponibilidad (ej. $99.9\%$).
* **Norma de Origen:** ITIL 4 / Service Level Management[cite: 2].
* **Ejemplo Resuelto:** 
  Para un mes de 30 días ($720\text{ horas}$) con un SLO de $99.9\%$:
  $$\text{Downtime Máximo} = 720 \times \left(1 - \frac{99.9}{100}\right) = 720 \times 0.001 = 0.72\text{ horas} = 43.2\text{ minutos}.$$

---

## 2. Disponibilidad en Serie y en Paralelo

Se utiliza cuando un servicio de red depende de múltiples componentes o enlaces interconectados.

### A. Componentes en Serie
Si un fallo en cualquiera de los componentes interrumpe todo el servicio:
$$\text{Disponibilidad Total} = \text{Disp}_1 \times \text{Disp}_2 \times \dots \times \text{Disp}_n$$
* **Norma de Origen:** Ingeniería de Confiabilidad y Conectividad de Redes[cite: 2].
* **Ejemplo Resuelto:** Dos equipos en serie con $99.9\%$ y $99.5\%$ de disponibilidad respectivamente:
  $$\text{Disp}_{\text{total}} = 0.999 \times 0.995 = 0.994005 \rightarrow 99.40\%.$$

### B. Componentes en Paralelo (Redundancia)
Si el sistema cuenta con un enlace de respaldo activo:
$$\text{Disponibilidad Total} = 1 - \left[(1 - \text{Disp}_1) \times (1 - \text{Disp}_2)\right]$$
* **Ejemplo Resuelto:** Dos enlaces redundantes con $99.0\%$ de disponibilidad cada uno:
  $$\text{Disp}_{\text{total}} = 1 - [(1 - 0.99) \times (1 - 0.99)] = 1 - [0.01 \times 0.01] = 1 - 0.0001 = 0.9999 \rightarrow 99.99\%.$$

---

## 3. Throughput y Eficiencia TCP

Evalúa el rendimiento de transferencia real de datos frente a la capacidad nominal contratada.

* **Fórmula:**
  $$\text{Eficiencia TCP (\%)} = \left(\frac{\text{Throughput Real Medido}}{\text{Ancho de Banda Nominal}}\right) \times 100$$
* **Variables y Unidades:**
  * Throughput y Ancho de Banda en Megabits por segundo ($\text{Mbps}$) o Gigabits por segundo ($\text{Gbps}$).
* **Norma de Origen:** RFC 6349 (Pruebas de Throughput TCP)[cite: 2].
* **Ejemplo Resuelto:** En un enlace nominal de $100\text{ Mbps}$, una prueba arroja un rendimiento efectivo de $92\text{ Mbps}$:
  $$\text{Eficiencia} = \left(\frac{92}{100}\right) \times 100 = 92\%.$$

---

## 4. Pérdida de Paquetes y Jitter

* **Pérdida de Paquetes (%):**
  $$\text{Pérdida (\%)} = \left(\frac{\text{Paquetes Enviados} - \text{Paquetes Recibidos}}{\text{Paquetes Enviados}}\right) \times 100$$
* **Jitter (Variación de Retardo):**
  Calculado como la desviación estándar o la diferencia absoluta media entre los tiempos de llegada de paquetes consecutivos.
* **Norma de Origen:** ITU-T Y.1540 (Métricas IP) y RFC 3393[cite: 2].
* **Ejemplo Resuelto:** De $10,000$ paquetes enviados, se reciben $9,990$:
  $$\text{Pérdida} = \left(\frac{10000 - 9990}{10000}\right) \times 100 = \left(\frac{10}{10000}\right) \times 100 = 0.1\%.$$

---

## 5. Latencia Teórica por Distancia en Fibra Óptica

Estima el retardo de propagación puro en medios físicos de fibra óptica monomodo (SMF).

* **Fórmula:**
  $$\text{Latencia Teórica (ms)} = \text{Distancia (km)} \times \text{Factor de Propagación}$$
* **Variables y Unidades:**
  * Factor de propagación de la luz en el núcleo de vidrio de la fibra $\approx 5\ \mu\text{s/km}$ ($0.005\text{ ms/km}$ de ida). Para retardo ida y vuelta (RTT), se multiplica por $2$ ($\approx 0.01\text{ ms/km}$).
* **Norma de Origen:** ITU-T G.114 e Ingeniería de Medios de Transmisión[cite: 2].
* **Ejemplo Resuelto:** Un enlace de fibra entre La Serena y Coquimbo de $15\text{ km}$ (RTT):
  $$\text{RTT Teórico} = 15\text{ km} \times 0.01\text{ ms/km} = 0.15\text{ ms}.$$

---

## 6. Crédito de Servicio por Incumplimiento

Calcula la compensación económica que el proveedor debe retribuir al cliente ante caídas de calidad fuera del SLO.

* **Fórmula:**
  $$\text{Crédito de Servicio (\% de la Tarifa)} = f(\text{Desviación del SLO})$$
  *(Típicamente estructurado por tramos: ej. Si la disponibilidad real está entre $99.0\%$ y $99.8\%$, se devuelve un $10\%$ del cargo mensual; si es menor a $99.0\%$, se devuelve un $25\%$).*
* **Norma de Origen:** ISO/IEC 20000-1 (Gestión de Niveles de Servicio)[cite: 2].
* **Ejemplo Resuelto:** Tarifa mensual de $\$200,000$ CLP. Por incumplimiento del SLO en un tramo que define un $10\%$ de compensación:
  $$\text{Monto Compensatorio} = \$200
$$\text{Monto Compensatorio} = \$200,000 \times 0.10 = \$20,000\text{ CLP}.$$
