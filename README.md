# Procesamiento de voz

Proyecto académico de captura y análisis de audio, reconocimiento automático del habla, verificación de locutor y clonación de voz con modelos preentrenados.

## Entorno

```bash
conda create -n UNIE_VozClon python=3.12
conda activate UNIE_VozClon
python -m pip install -r requirements.txt
```

PyTorch y TorchAudio se instalan desde el índice de CPU indicado en `requirements.txt`. La primera ejecución de algunos notebooks descarga modelos y los guarda en caché o en `data/`.

## Orden de ejecución

1. `01_grabacion_audios.py` — graba las muestras necesarias en `data/`.
2. `02_espectrograma_tiempo_real.ipynb` — observa el espectrograma desde el micrófono.
3. `03_asr_wav2vec2_texto.ipynb` — prueba el ejemplo público y transcribe las grabaciones propias.
4. `04_verificacion_locutor_ecapa.ipynb` — compara embeddings de las cuatro grabaciones.
5. `05_clonacion_voz_qwen3tts.ipynb` — genera audio usando una muestra de referencia.

Reinicia el kernel de cada notebook y ejecuta sus celdas en orden. La grabación y el espectrograma en tiempo real requieren micrófono; los demás flujos necesitan los archivos indicados en `data/`.

## Uso responsable

La clonación de voz debe realizarse únicamente con consentimiento informado de la persona cuya voz se utiliza. Identifica claramente el audio sintético y no lo emplees para suplantación, engaño ni publicación no autorizada.
