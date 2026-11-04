[script_de_construcci_n_completo.md](https://github.com/user-attachments/files/34347123/script_de_construcci_n_completo.md)
#!/bin/bash

# Script de automatización para generar la totalidad del contenido del SLA Toolkit

# 1. README.md

cat << 'EOF' > README.md

# Toolkit para el Diseño, Cálculo y Verificación de SLA de Red

Este repositorio contiene un toolkit modular y reutilizable diseñado para construir, calcular y verificar Acuerdos de Nivel de Servicio (SLA) en servicios de red y telecomunicaciones, basado en normativas internacionales (ITIL 4, ITU-T E.860, Y.1540, MEF 10.4, entre otras).

## Estructura del Repositorio

* **`docs/`**: Documentación del método de diseño en 6 pasos, normas de referencia y glosario técnico.

* **`plantillas/`**: Plantillas reutilizables en Markdown para SLA, checklist de requisitos del cliente e informes de cumplimiento.

* **`formulas/`**: Repositorio de fórmulas matemáticas y de ingeniería de red con variables, unidades y ejemplos resueltos.

* **`herramientas/`**: Script en Python (`calc_sla.py`) para la verificación automatizada de SLOs y cálculo de compensaciones económicas a partir de archivos de configuración (`objetivos.yaml`).

* **`datos/`**: Registros de mediciones históricas en formato CSV.

* **`ejemplos/`**: Caso de aplicación práctica completo aplicado a un enlace dedicado de Internet.

## Requisitos Técnicos

* **Python 3.x** instalado en el sistema.

* Librería **PyYAML** para procesar los archivos de objetivos. Puedes instalarla ejecutando:

  ```
  pip install pyyaml
  
  ```

## Instrucciones de Uso (Calculadora de SLA)

Para ejecutar la herramienta automatizada de verificación de cumplimiento y cálculo de créditos de servicio:

```
python3 herramientas/calc_sla.py

```

EOF

# 2. LICENSE

cat << 'EOF' > LICENSE
MIT License

Copyright (c) 2026 Marco Castillo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom rites the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

# 3. CHANGELOG.md

cat << 'EOF' > CHANGELOG.md

# Registro de Cambios (CHANGELOG)

Todas las modificaciones notables de este toolkit serán documentadas en este archivo.

## \[1.0.0\] - 2026-11-03

### Añadido

* Estructura base completa del repositorio Git (`docs/`, `plantillas/`, `formulas/`, `herramientas/`, `datos/`, `ejemplos/`).

* Documentación formal del método de diseño en 6 pasos (ITIL 4 e ITU-T E.860).

* Documentación de normas de referencia y glosario técnico de SLA.

* Plantillas reutilizables para SLA, checklist de requisitos e informe de cumplimiento.

* Repositorio de fórmulas matemáticas y de ingeniería de red con ejemplos resueltos.

* Automatización de cálculo de cumplimiento y créditos en Python (`calc_sla.py`).

* Caso de ejemplo práctico aplicado a un enlace dedicado corporativo.
  EOF

# 4. docs/metodo.md

cat << 'EOF' > docs/metodo.md

# Método de Diseño de SLA (ITIL 4 e ITU-T E.860)

Este documento detalla el ciclo metodológico de 6 pasos empleado en el toolkit para diseñar, calcular y verificar Acuerdos de Nivel de Servicio (SLA) en redes de telecomunicaciones.

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
  EOF

# 5. docs/normas.md

cat << 'EOF' > docs/normas.md

# Normas de Referencia para el Diseño de SLA

Este documento detalla las normativas internacionales aplicadas en cada fase del toolkit para garantizar rigor técnico en telecomunicaciones.

## Tabla de Normas y su Uso en el Toolkit

| Ámbito | Norma | Uso en el Toolkit | 
| ----- | ----- | ----- | 
| **Gestión del SLA** | ITIL 4 - Service Level Management | Proceso de requisitos, acuerdo, monitoreo y revisión. | 
| **Gestión del SLA** | ISO/IEC 20000-1 | Requisitos certificables de gestión de servicios. | 
| **Estructura del SLA** | ITU-T E.860 | Partes que debe tener un SLA de telecomunicaciones. | 
| **Estructura del SLA** | ISO/IEC 19086-1 | Equivalente para servicios cloud. | 
| **Métricas IP** | ITU-T Y.1540 / Y.1541 | Definición de retardo, jitter, pérdida y disponibilidad IP; clases de QoS. | 
| **Métricas Ethernet** | MEF 10.4 | Atributos de servicio y disponibilidad en Carrier Ethernet. | 
| **Medición** | RFC 7679 / RFC 7680 | Retardo y pérdida unidireccionales. | 
| **Medición** | RFC 3393 | Variación del retardo (jitter). | 
| **Medición** | RFC 5357 (TWAMP) | Medición activa bidireccional. | 
| **Medición** | RFC 6349 | Pruebas de throughput TCP. | 
| **Referencia de voz** | ITU-T G.114 | Retardo unidireccional recomendado ($\le 150\text{ ms}$). | 
| EOF |  |  | 

# 6. docs/glosario.md

cat << 'EOF' > docs/glosario.md

# Glosario Técnico de SLA

Definiciones de los términos clave utilizados en la gestión, cálculo y verificación de servicios de red.

* **SLA (Service Level Agreement - Acuerdo de Nivel de Servicio):** Contrato formal entre un proveedor de servicios y un cliente que define el nivel de servicio esperado, las métricas de rendimiento y las consecuencias ante el incumplimiento.

* **SLI (Service Level Indicator - Indicador de Nivel de Servicio):** Métrica cuantitativa real que mide el nivel de rendimiento de un servicio (ej. latencia en milisegundos, porcentaje de paquetes perdidos).

* **SLO (Service Level Objective - Objetivo de Nivel de Servicio):** Meta o umbral específico fijado para un SLI que el proveedor se compromete a cumplir (ej. disponibilidad $\ge 99.9\%$).

* **SLR (Service Level Requirement - Requisito de Nivel de Servicio):** Necesidad de negocio del cliente expresada en su propio lenguaje antes de traducirse en objetivos técnicos.

* **OLA (Operational Level Agreement - Acuerdo de Nivel Operativo):** Acuerdo interno entre equipos o departamentos del proveedor para garantizar que se alcancen los SLA con el cliente.

* **MTBF (Mean Time Between Failures - Tiempo Medio Entre Fallas):** Mide la confiabilidad de un sistema, indicando el tiempo promedio estimado que opera de manera continua sin sufrir interrupciones.

* **MTTR (Mean Time To Repair - Tiempo Medio de Reparación):** Tiempo promedio que toma restaurar un servicio a su estado operativo normal tras una falla.
  EOF

# 7. plantillas/plantilla-sla.md

cat << 'EOF' > plantillas/plantilla-sla.md

# Acuerdo de Nivel de Servicio (SLA) - \[Nombre del Servicio\]

## 1. Partes Involucradas

* **Proveedor:** \[Nombre de la Empresa / Proveedor de Telecomunicaciones\]

* **Cliente:** \[Nombre de la Empresa Cliente / Institución\]

* **Fecha de Vigencia:** \[DD/MM/AAAA\]

## 2. Descripción del Servicio y Demarcación

* **Tipo de Servicio:** \[Ej. Enlace Dedicado de Internet / MPLS / VPN\]

* **Ancho de Banda / Capacidad:** \[Ej. 100 Mbps Simétrico\]

* **Punto de Demarcación:** \[Descripción física del equipo o interfaz donde termina la responsabilidad del proveedor y comienza la del cliente, según ITU-T E.860\]

## 3. Objetivos de Nivel de Servicio (SLO)

| Métrica (SLI) | Objetivo Acordado (SLO) | Norma de Referencia | 
| ----- | ----- | ----- | 
| **Disponibilidad** | $\ge [99.9]\%$ | ITU-T Y.1540 | 
| **Latencia (Retardo)** | $\le [20]\text{ ms}$ | ITU-T Y.1541 / G.114 | 
| **Jitter (Variación)** | $\le [5]\text{ ms}$ | RFC 3393 | 
| **Pérdida de Paquetes** | $\le [0.1]\%$ | ITU-T Y.1540 | 
| **Throughput TCP** | $\ge [95]\%$ del nominal | RFC 6349 | 

## 4. Operación, Soporte y Ventanas de Mantenimiento

* **Horario de Soporte:** \[Ej. 24/7/365\]

* **Tiempo Medio de Respuesta (MTTR estimado):** \[Ej. 4 horas\]

* **Ventanas de Mantenimiento Programado:** \[Ej. Domingos de 02:00 a 06:00 AM\]

## 5. Consecuencias y Créditos por Incumplimiento

* Si el cumplimiento mensual del SLO de disponibilidad cae por debajo del objetivo, se aplicarán créditos proporcionales sobre la factura mensual según la tabla de penalizaciones establecida.
  EOF

# 8. plantillas/checklist-requisitos.md

cat << 'EOF' > plantillas/checklist-requisitos.md

# Checklist de Levantamiento de Requisitos del Cliente (SLR)

Utilice este formato en la fase de entrevista con el cliente (ITIL 4 Service Level Management).

* \[ \] **1. Identificación del Negocio:** ¿Cuál es la actividad principal de la empresa cliente y qué aplicaciones críticas corren sobre la red (ej. VoIP, ERP, Videoconferencia, Bases de datos)?

* \[ \] **2. Requerimientos de Ancho de Banda:** ¿Cuál es la tasa de transferencia pico y promedio esperada (Burst / Committed Information Rate - CIR)?

* \[ \] **3. Ubicaciones y Topología:** ¿Cuáles son las sedes geográficas a conectar y qué tipo de redundancia o enlaces de respaldo se requieren?

* \[ \] **4. Expectativas de Disponibilidad (SLR):** ¿Qué nivel de disponibilidad exige el negocio (ej. 99.9%, 99.99%)?

* \[ \] **5. Tolerancia a Latencia y Jitter:** ¿Qué umbrales máximos toleran las aplicaciones en tiempo real (ej. Telefonía IP $\le 150\text{ ms}$ según ITU-T G.114)?

* \[ \] **6. Ventanas de Operación:** ¿Opera el cliente 24/7 o cuenta con horarios específicos donde se puedan programar mantenimientos?
  EOF

# 9. plantillas/informe-cumplimiento.md

cat << 'EOF' > plantillas/informe-cumplimiento.md

# Informe Técnico de Verificación de SLA

* **Período Evaluado:** \[Mes / Año\]

* **Cliente:** \[Nombre del Cliente\]

* **Servicio Evaluado:** \[Nombre del Enlace\]

## 1. Resumen de Mediciones

| Métrica | SLO Comprometido | Valor Medido Real | Veredicto (Cumple / No Cumple) | 
| ----- | ----- | ----- | ----- | 
| Disponibilidad |  |  |  | 
| Latencia Promedio |  |  |  | 
| Jitter |  |  |  | 
| Pérdida de Paquetes |  |  |  | 

## 2. Análisis de Incidentes y Exclusiones

* **Total de horas de interrupción imputables al proveedor:**

* **Detalle de incidencias o ventanas de mantenimiento aplicadas:**

## 3. Cálculo de Créditos de Servicio

* **Tarifa Mensual del Servicio:**

* **Porcentaje de Crédito Aplicable:**

* **Monto Compensatorio a Bonificar:**
  EOF

# 10. formulas/formulas.md

cat << 'EOF' > formulas/formulas.md

# Fórmulas y Modelos de Cálculo para SLA de Red

Este documento recopila las fórmulas matemáticas y de ingeniería de redes utilizadas en el toolkit para calcular el rendimiento, disponibilidad, eficiencia y compensaciones de los servicios.

## 1. Disponibilidad Porcentual y Caída Permitida

Permite calcular el porcentaje de tiempo que el servicio se encuentra operativo frente al tiempo total del período de medición, así como el tiempo máximo de inactividad tolerado (downtime) para cumplir con el SLO.

* **Fórmula de Disponibilidad:**
  

  $$
  \text{Disponibilidad (\%)} = \left(1 - \frac{\text{Tiempo de Inactividad (Downtime)}}{\text{Tiempo Total del Período}}\right) \times 100
  $$

* **Fórmula de Caída Permitida:**
  

  $$
  \text{Downtime Máximo} = \text{Tiempo Total} \times \left(1 - \frac{\text{SLO Target}}{100}\right)
  $$

* **Variables y Unidades:**

  * $\text{Downtime}$: Tiempo total de interrupción (Horas o Minutos).

  * $\text{Tiempo Total}$: Duración total del período (ej. un mes de 30 días = $720\text{ horas} = 43,200\text{ minutos}$).

  * $\text{SLO Target}$: Porcentaje objetivo de disponibilidad (ej. $99.9\%$).

* **Norma de Origen:** ITIL 4 / Service Level Management.

* **Ejemplo Resuelto:**
  Para un mes de 30 días ($720\text{ horas}$) con un SLO de $99.9\%$:
  

  $$
  \text{Downtime Máximo} = 720 \times \left(1 - \frac{99.9}{100}\right) = 720 \times 0.001 = 0.72\text{ horas} = 43.2\text{ minutos}.
  $$

## 2. Disponibilidad en Serie y en Paralelo

Se utiliza cuando un servicio de red depende de múltiples componentes o enlaces interconectados.

### A. Componentes en Serie

Si un fallo en cualquiera de los componentes interrumpe todo el servicio:

$$
\text{Disponibilidad Total} = \text{Disp}_1 \times \text{Disp}_2 \times \dots \times \text{Disp}_n
$$

* **Norma de Origen:** Ingeniería de Confiabilidad y Conectividad de Redes.

* **Ejemplo Resuelto:** Dos equipos en serie con $99.9\%$ y $99.5\%$ de disponibilidad respectivamente:
  

  $$
  \text{Disp}_{\text{total}} = 0.999 \times 0.995 = 0.994005 \rightarrow 99.40\%.
  $$

### B. Componentes en Paralelo (Redundancia)

Si el sistema cuenta con un enlace de respaldo activo:

$$
\text{Disponibilidad Total} = 1 - \left[(1 - \text{Disp}_1) \times (1 - \text{Disp}_2)\right]
$$

* **Ejemplo Resuelto:** Dos enlaces redundantes con $99.0\%$ de disponibilidad cada uno:
  

  $$
  \text{Disp}_{\text{total}} = 1 - [(1 - 0.99) \times (1 - 0.99)] = 1 - [0.01 \times 0.01] = 1 - 0.0001 = 0.9999 \rightarrow 99.99\%.
  $$

## 3. Throughput y Eficiencia TCP

Evalúa el rendimiento de transferencia real de datos frente a la capacidad nominal contratada.

* **Fórmula:**
  

  $$
  \text{Eficiencia TCP (\%)} = \left(\frac{\text{Throughput Real Medido}}{\text{Ancho de Banda Nominal}}\right) \times 100
  $$

* **Variables y Unidades:**

  * Throughput y Ancho de Banda en Megabits por segundo ($\text{Mbps}$) o Gigabits por segundo ($\text{Gbps}$).

* **Norma de Origen:** RFC 6349 (Pruebas de Throughput TCP).

* **Ejemplo Resuelto:** En un enlace nominal de $100\text{ Mbps}$, una prueba arroja un rendimiento efectivo de $92\text{ Mbps}$:
  

  $$
  \text{Eficiencia} = \left(\frac{92}{100}\right) \times 100 = 92\%.
  $$

## 4. Pérdida de Paquetes y Jitter

* **Pérdida de Paquetes (%):**
  

  $$
  \text{Pérdida (\%)} = \left(\frac{\text{Paquetes Enviados} - \text{Paquetes Recibidos}}{\text{Paquetes Enviados}}\right) \times 100
  $$

* **Jitter (Variación de Retardo):**
  Calculado como la desviación estándar o la diferencia absoluta media entre los tiempos de llegada de paquetes consecutivos.

* **Norma de Origen:** ITU-T Y.1540 (Métricas IP) y RFC 3393.

* **Ejemplo Resuelto:** De $10,000$ paquetes enviados, se reciben $9,990$:
  

  $$
  \text{Pérdida} = \left(\frac{10000 - 9990}{10000}\right) \times 100 = \left(\frac{10}{10000}\right) \times 100 = 0.1\%.
  $$

## 5. Latencia Teórica por Distancia en Fibra Óptica

Estima el retardo de propagación puro en medios físicos de fibra óptica monomodo (SMF).

* **Fórmula:**
  

  $$
  \text{Latencia Teórica (ms)} = \text{Distancia (km)} \times \text{Factor de Propagación}
  $$

* **Variables y Unidades:**

  * Factor de propagación de la luz en el núcleo de vidrio de la fibra $\approx 5\ \mu\text{s/km}$ ($0.005\text{ ms/km}$ de ida). Para retardo ida y vuelta (RTT), se multiplica por $2$ ($\approx 0.01\text{ ms/km}$).

* **Norma de Origen:** ITU-T G.114 e Ingeniería de Medios de Transmisión.

* **Ejemplo Resuelto:** Un enlace de fibra entre La Serena y Coquimbo de $15\text{ km}$ (RTT):
  

  $$
  \text{RTT Teórico} = 15\text{ km} \times 0.01\text{ ms/km} = 0.15\text{ ms}.
  $$

## 6. Crédito de Servicio por Incumplimiento

Calcula la compensación económica que el proveedor debe retribuir al cliente ante caídas de calidad fuera del SLO.

* **Fórmula:**
  

  $$
  \text{Crédito de Servicio (\% de la Tarifa)} = f(\text{Desviación del SLO})
  $$

* **Norma de Origen:** ISO/IEC 20000-1 (Gestión de Niveles de Servicio).

* **Ejemplo Resuelto:** Tarifa mensual de $\$200,000$ CLP. Por incumplimiento del SLO en un tramo que define un $10\%$ de compensación:
  

  $$
  \text{Monto Compensatorio} = \$200,000 \times 0.10 = \$20,000\text{ CLP}.
  $$

  
  EOF

# 11. herramientas/objetivos.yaml

cat << 'EOF' > herramientas/objetivos.yaml
disponibilidad:
limite: 99.9
operador: ">="
unidad: "%"
peso_penalizacion: 0.10

latencia:
limite: 20.0
operador: "<="
unidad: "ms"
peso_penalizacion: 0.05

jitter:
limite: 5.0
operador: "<="
unidad: "ms"
peso_penalizacion: 0.05

perdida_paquetes:
limite: 0.1
operador: "<="
unidad: "%"
peso_penalizacion: 0.10

throughput:
limite: 95.0
operador: ">="
unidad: "%"
peso_penalizacion: 0.05
EOF

# 12. datos/mediciones-ejemplo.csv

cat << 'EOF' > datos/mediciones-ejemplo.csv
fecha,metrica,valor,unidad
2026-10-01,disponibilidad,99.95,%
2026-10-05,latencia,18.5,ms
2026-10-10,jitter,3.2,ms
2026-10-15,perdida_paquetes,0.05,%
2026-10-20,throughput,96.0,%
2026-10-25,disponibilidad,99.50,%
EOF

# 13. herramientas/calc_sla.py

cat << 'EOF' > herramientas/calc_sla.py
import csv
import sys
import os

try:
import yaml
except ImportError:
print("Error: La librería PyYAML no está instalada. Ejecute 'pip install pyyaml'.")
sys.exit(1)

def cargar_yaml(ruta):
if not os.path.exists(ruta):
print(f"Error: No se encuentra el archivo de objetivos en {ruta}")
sys.exit(1)
with open(ruta, 'r', encoding='utf-8') as f:
return yaml.safe_load(f)

def cargar_csv(ruta):
if not os.path.exists(ruta):
print(f"Error: No se encuentra el archivo de datos en {ruta}")
sys.exit(1)
with open(ruta, 'r', encoding='utf-8') as f:
reader = csv.DictReader(f)
return list(reader)

def evaluar_sla():
ruta_yaml = os.path.join(os.path.dirname(**file**), 'objetivos.yaml')
ruta_csv = os.path.join(os.path.dirname(**file**), '..', 'datos', 'mediciones-ejemplo.csv')

```
objetivos = cargar_yaml(ruta_yaml)
mediciones = cargar_csv(ruta_csv)

print("=" * 65)
print(f"{'REPORTE DE VERIFICACIÓN DE SLA - TOOLKIT':^65}")
print("=" * 65)
print(f"{'FECHA':<12} | {'MÉTRICA':<18} | {'VALOR':<8} | {'OBJETIVO':<10} | {'VEREDICTO':<10}")
print("-" * 65)

total_incumplimientos = 0
credito_total = 0.0
tarifa_base = 250000.0

for med in mediciones:
    fecha = med['fecha']
    metrica = med['metrica']
    try:
        valor = float(med['valor'])
    except ValueError:
        continue
    
    if metrica in objetivos:
        obj = objetivos[metrica]
        limite = obj['limite']
        operador = obj['operador']
        unidad = obj['unidad']
        
        cumple = False
        if operador == '<=':
            cumple = valor <= limite
        elif operador == '>=':
            cumple = valor >= limite
            
        estado = "CUMPLE" if cumple else "NO CUMPLE"
        
        if not cumple:
            total_incumplimientos += 1
            credito_total += tarifa_base * obj['peso_penalizacion']
            
        print(f"{fecha:<12} | {metrica:<18} | {valor:<5} {unidad:<2} | {limite:<6} {unidad:<2} | {estado:<10}")

print("=" * 65)
print(f"Resumen de Verificación:")
print(f" - Total de métricas evaluadas: {len(mediciones)}")
print(f" - Incumplimientos detectados: {total_incumplimientos}")
print(f" - Crédito de servicio estimado por compensación: ${credito_total:,.2f} CLP")
print("=" * 65)

```

if **name** == "**main**":
evaluar_sla()
EOF

# 14. ejemplos/enlace-dedicado/sla.md

cat << 'EOF' > ejemplos/enlace-dedicado/sla.md

# Acuerdo de Nivel de Servicio (SLA) - Enlace Dedicado Corporativo

* **Proveedor:** Inacap Telecomunicaciones S.A.

* **Cliente:** Empresa Conecta SpA (La Serena)

* **Servicio:** Enlace de Internet Simétrico Dedicado de 100 Mbps

## 1. Demarcación (ITU-T E.860)

El punto de demarcación se establece en el puerto GigabitEthernet 0/1 del Router de Borde del Proveedor ubicado en las dependencias del cliente.

## 2. Compromisos de Nivel de Servicio (SLO)

* **Disponibilidad:** $\ge 99.9\%$ mensual.

* **Latencia RTT:** $\le 20\text{ ms}$ hacia el primer salto internacional.

* **Jitter:** $\le 5\text{ ms}$.

* **Pérdida de Paquetes:** $\le 0.1\%$.
  EOF

# 15. ejemplos/enlace-dedicado/informe.md

cat << 'EOF' > ejemplos/enlace-dedicado/informe.md

# Informe Técnico de Verificación - Enlace Dedicado (Octubre 2026)

* **Herramienta de Verificación:** `calc_sla.py` (Toolkit v1.0)

* **Período:** Octubre de 2026

## Resultados Obtenidos

A partir de la ejecución de la herramienta de cálculo sobre el registro de mediciones del mes, se obtuvieron los siguientes resultados:

* Total de métricas evaluadas: **6**

* Incumplimientos detectados: **1** (Métrica de disponibilidad del 25-10-2026 con 99.5%)

* **Veredicto General:** Incumplimiento parcial del SLO mensual.

* **Compensación aplicada:** Crédito de servicio calculado por valor de **\$25,000.00 CLP** sobre la tarifa base de operación.
  EOF

echo "¡Construcción completa de todos los archivos finalizada exitosamente!"
