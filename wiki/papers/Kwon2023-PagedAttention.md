---
title: "PagedAttention：分頁式 KV Cache 管理 (Kwon et al., 2023)"
category: "Memory-Management"
source: "raw/papers/Kwon2023-PagedAttention.md"
---
# PagedAttention 分頁管理
傳統連續顯存預留導致動態 KV Cache 浪費高達 **60%–80%**。
PagedAttention 借鏡作業系統虛擬記憶體分頁，將 KV Cache 切為非連續固定區塊（KV Blocks），以 Block Table 映射並支援 Copy-on-Write 共享前綴：
- 將顯存浪費率壓低至 **4% 以下**。
- 論文 vLLM 環境下吞吐量提升 **2x–4x**。關聯：[[KV-Cache-Paging]]。