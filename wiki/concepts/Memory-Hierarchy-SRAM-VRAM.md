---
title: "Memory Hierarchy（多層記憶體金字塔）"
---
# Memory Hierarchy
速度由快到慢依序為 GPU SRAM（手邊砧板）→ 獨顯 VRAM/HBM（廚房冰箱）→ 系統 RAM（儲藏室）→ SSD（遠方物流倉庫）。[[Dao2022-FlashAttention]] 透過 Tiling 善用 SRAM。