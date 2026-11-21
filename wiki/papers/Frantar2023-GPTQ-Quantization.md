---
title: "GPTQ：4-bit 訓練後權重量化 (Frantar et al., 2023)"
category: "Inference-Optimization"
source: "raw/papers/Frantar2023-GPTQ-Quantization.md"
---
# GPTQ 權重量化壓縮
模型權重顯存佔用公式：$\text{VRAM}_{\text{weights}} \approx N_{\text{params}} \times \frac{b}{8}\;\text{Bytes}$。
GPTQ 為一次性訓練後量化（PTQ），透過二階海森矩陣（Hessian）逆矩陣補償捨入誤差，將權重從 FP16（16-bit）壓縮至 **INT4（4-bit）**：
- 體積壓縮 ~4 倍（7B 模型從 ~14 GB 降至 ~3.5–4.5 GB），能裝入 8GB 筆電；3B INT4 約 1.5–2.0 GB，能裝入行動輕薄設備。
- 論文實測推論加速：A100 約 **3.25x**、A6000 約 **4.5x**。關聯：[[Weight-Quantization-INT4]]。