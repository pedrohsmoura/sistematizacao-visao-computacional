# -*- coding: utf-8 -*-
"""Fine-tuning do detector YOLOv8m (equivalente a celula 3 do notebook).

Mesmos hiperparametros do Colab, exceto o batch size: a RTX 2060 tem 6 GB de
VRAM e o treino original consumiu 7,26 GB na T4. Com batch=8 o Ultralytics
acumula gradientes ate o nominal batch size (nbs=64), entao o batch efetivo
continua 64 - igual ao da execucao original.
"""
import torch
from ultralytics import YOLO

EPOCHS, IMG_SIZE, BATCH_SIZE, SEED = 40, 640, 8, 42
DATASET_YAML = 'data/raw/data.yaml'


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'PyTorch: {torch.__version__} | Dispositivo: {device}')
    if device == 'cuda':
        print('GPU:', torch.cuda.get_device_name(0))

    model = YOLO('yolov8m.pt')
    model.train(
        data=DATASET_YAML,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        seed=SEED,
        workers=4,
        device=0 if device == 'cuda' else 'cpu',
        project='vcrp_seguranca',
        name='yolo_epi_detection',
        exist_ok=True,
    )
    print('Treinamento concluido!')


if __name__ == '__main__':
    main()
