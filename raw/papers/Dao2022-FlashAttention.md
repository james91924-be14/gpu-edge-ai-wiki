# Raw Immutable Source: Dao2022-FlashAttention

---
title: "FlashAttention：記憶體階層感知運算 (Dao et al., 2022)"
category: "Inference-Optimization"
source: "raw/papers/Dao2022-FlashAttention.md"
---
# FlashAttention 分塊計算與 Online Softmax
利用 [[Memory-Hierarchy-SRAM-VRAM]] 巨大頻寬落差（論文 A100 例：片上 SRAM ~20 MB / 19 TB/s vs 外部 HBM 40–80 GB / 1.5–2.0 TB/s），透過 **Tiling 分塊計算** 與 **Online Softmax** 留在 SRAM 一次算完精確注意力（零近似誤差）。
- HBM IO 複雜度由 $\Theta(N^2)$ 降至 $\Theta(N^2 d^2 M^{-1})$。
- 論文於 A100 訓練 GPT-2 達最高 **3x 加速**；消費級手機與筆電實測加速倍率屬 [來源未提供]。
