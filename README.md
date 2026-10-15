# 🔐 Detector de Ataques de Fuerza Bruta

Proyecto de ciberseguridad desarrollado en Python para detectar posibles
ataques de fuerza bruta mediante el análisis de intentos fallidos de autenticación.

## 📌 Descripción

El programa simula eventos de inicio de sesión y monitorea los intentos
fallidos de autenticación de cada usuario.

Cuando un usuario alcanza una cantidad determinada de intentos fallidos
consecutivos, el sistema genera una alerta de seguridad de severidad ALTA.

El objetivo del proyecto es demostrar de forma sencilla cómo se pueden
utilizar reglas de detección para identificar comportamientos potencialmente
sospechosos dentro de eventos de autenticación.

## ⚙️ Funcionalidades

- Monitoreo de eventos de autenticación.
- Conteo de intentos fallidos por usuario.
- Detección de posibles ataques de fuerza bruta.
- Generación de alertas de seguridad.
- Clasificación de la alerta como severidad ALTA.
- Reinicio del contador después de una autenticación exitosa.
- Umbral de detección configurable.

## 🚨 Ejemplo de detección

    [FAILED LOGIN] User: admin | Attempts: 4
    [FAILED LOGIN] User: admin | Attempts: 5
    [HIGH ALERT] Possible brute-force attack detected against user: admin

En este ejemplo, el sistema detecta cinco intentos fallidos consecutivos
contra la cuenta `admin` y genera una alerta.

## 🧠 Lógica de detección

El prototipo utiliza una regla basada en un umbral:

    Intentos fallidos >= 5 → ALERTA ALTA

El valor puede modificarse mediante la variable:

    ALERT_THRESHOLD = 5

En un entorno real, este umbral debería ajustarse de acuerdo con las
políticas de seguridad y el comportamiento normal de los usuarios de
la organización para reducir falsos positivos.

## 🛡️ MITRE ATT&CK

El comportamiento detectado está relacionado con la técnica:

**T1110 — Brute Force**

Esta técnica corresponde a intentos de obtener acceso a una cuenta
mediante múltiples intentos de autenticación.

## ▶️ Ejecución

### Requisitos

- Python 3

No se necesitan librerías externas.

### Ejecutar el programa

    python detector.py

En Windows también puede utilizarse:

    py detector.py

## 📈 Posibles mejoras

El proyecto puede ampliarse para:

- Analizar logs reales de Windows.
- Registrar la dirección IP de origen.
- Detectar múltiples intentos dentro de una ventana de tiempo.
- Exportar las alertas a JSON o CSV.
- Integrarse con una plataforma SIEM.
- Incorporar respuesta automática ante incidentes.
- Crear un dashboard para visualizar las alertas.
- Correlacionar diferentes tipos de eventos de seguridad.

## 🎯 Objetivo del proyecto

Este proyecto fue desarrollado como una prueba de concepto para demostrar
el funcionamiento básico de un sistema de monitoreo de eventos de seguridad
y detección de comportamientos sospechosos mediante reglas.

El prototipo busca representar, de forma simplificada, uno de los procesos
que podría realizar un sistema SIEM dentro de un entorno de ciberseguridad.
