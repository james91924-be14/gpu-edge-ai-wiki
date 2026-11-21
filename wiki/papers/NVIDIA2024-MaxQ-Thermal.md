---
title: "NVIDIA Max-Q 與跨裝置功耗／溫控降頻機制"
category: "Hardware-Thermal"
source: "raw/papers/NVIDIA2024-MaxQ-Thermal.md"
---
# 功耗牆、溫度牆與 DVFS 降頻
動態功耗遵循 $P_{\text{dyn}} = \alpha C V^2 f$，電壓平方會讓廢熱呈非線性暴增。
- 行動輕薄陣營：手機無風扇僅能承受 5–10W（表溫/晶片約 48–60°C 觸發降頻），輕薄筆電 TGP 約 15–28W（約 76–80°C）。
- 獨顯效能陣營：電競筆電 TGP 常見 100–115W，典型溫度牆約 $87^\circ\text{C}$。
- 適度降壓（Undervolt）可減少 20%–30% 發熱量，僅損失約 5%–10% 峰值算力。
- 特定機型實測降頻曲線：[來源未提供]。詳見 [[Thermal-Throttling]]、[[Roofline-Model]]。