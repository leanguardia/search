## Examen Final Parte #2 - Calidad de sueño

Contamos con datos que indican si una persona tiene algún desorden de sueño.

El problema es una clasificación multi-clase donde la variable objetivo tiene uno de los siguientes valores:
1. None: Sin problemas de sueño
2. Insomnia: El paciente padece de insomnio
3. Sleep Apnea: El paciente sufre de pausas de respiración durante el sueño

Entrena redes neuronales de manera incremental en un Jupyter Notebook.

Ejemplo: el primer modelo es entrenado solo con los datos continuos, el segundo incluye los categóricos, el tercero incluye ingeniería de features. (Ej. transformar la presión sanguínea a número).

### Reglas
- Está permitido guiarse con su proyecto final.
- Está permitido usar documentación e internet.
- NO está permitido usar modelos lingüísticos.


### Datos
#### continuos
- Person ID: Identificador único
- Age: Edad en años
- Sleep Duration (hours): Cantidad de horas que una persona duerme al día
- Quality of Sleep (scale: 1-10): Escala subjetiva de la calidad de sueño
- Physical Activity Level (minutes/day): Minutos de actividad física al día
- Stress Level (scale: 1-10): Escala subjetiva de nivel de estrés diario
- Heart Rate (bpm): Ritmo cardiado en estado de descanso, en pulsos por minuto
- Daily Steps: Cantidad de pasos diarios


#### categóricos
- Gender: Género (Male/Female).
- Occupation: Profesión
- BMI Category: Índice de masa corporal (e.g., Underweight, Normal, Overweight).
- Blood Pressure (systolic/diastolic): Presión sanguínea, indicado como presión sistólica sobre presión diastólica
- 🎯 Sleep Disorder: Ausencia o presencia de algún desorden de sueño (None, Insomnia, Sleep Apnea).

### Entrega
Enviar el archivo .ipynb al correo dguardia@ucb.edu.bo