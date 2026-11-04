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
    ruta_yaml = os.path.join(os.path.dirname(__file__), 'objetivos.yaml')
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos', 'mediciones-ejemplo.csv')
    
    objetivos = cargar_yaml(ruta_yaml)
    mediciones = cargar_csv(ruta_csv)
    
    print("=" * 65)
    print(f"{'REPORTE DE VERIFICACIÓN DE SLA - TOOLKIT':^65}")
    print("=" * 65)
    print(f"{'FECHA':<12} | {'MÉTRICA':<18} | {'VALOR':<8} | {'OBJETIVO':<10} | {'VEREDICTO':<10}")
    print("-" * 65)
    
    total_incumplimientos = 0
    credito_total = 0.0
    tarifa_base = 250000.0  # Tarifa de ejemplo en CLP para cálculo de créditos

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
            
            # Evaluación lógica del SLO
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

if __name__ == "__main__":
    evaluar_sla()
