---
title: "Roofline 效能屋頂模型 (Williams et al., 2009)"
category: "Architecture-Model"
source: "raw/papers/Williams2009-Roofline.md"
---
# Roofline 效能屋頂模型
算術強度定義為 $I = \frac{\text{FLOPs}}{\text{Bytes}}$，晶片實際效能上限為：
$$P = \min\left(\text{Peak FLOPs},\; \text{Peak Bandwidth} \times I\right)$$
- **Memory-bound（頻寬受限）**：$I$ 低於硬體脊點（Ridge Point），運算核心乾等資料從記憶體搬運（如 LLM Decode 逐字生成）。
- **Compute-bound（算力受限）**：$I$ 夠高，吃滿計算核心（如 LLM Prefill、大 Batch 矩陣運算）。
關聯：[[Roofline-Model]]、[[Memory-Hierarchy-SRAM-VRAM]]、[[Weight-Quantization-INT4]]。