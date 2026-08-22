# reiser-plugins

[English](README.md) · **繁體中文**

Claude 外掛市集 — Office 文件工具、版型樣式範本，以及台灣法律檢索。

> **私有儲存庫。** 這些外掛內含版型樣式設定。在變更儲存庫可見性之前，請重新檢視每一個 skill，**並解壓縮每一個隨附的 `.pptx`**，確認沒有機構名稱、產品名稱、藍圖規劃用語、合作夥伴名稱、設備型號、機密等級標示、內部檔案路徑與個人識別資訊 —— 這些都不該出現在公開儲存庫。`.pptx` 內的 `docProps/core.xml` 會記錄最後編輯者姓名，務必檢查。請參閱 [外洩檢查](#外洩檢查)。

---

## 內容概要

兩個外掛。

| 外掛 | 用途 |
|---|---|
| `office-cli` | 以固定版型樣式產出簡報、報告與工作表 —— 五個 skill、三套可互換的設計範本。 |
| `tw-legal-rag` | 台灣裁判與行政函釋 —— 語義檢索，並將引用紀律寫進 skill。 |

### office-cli

| Skill | 用途 |
|---|---|
| `house-style` | **進入點。** 先選設計範本，再選工具 —— 複製範本、產生新簡報，或直接編輯現有檔案。 |
| `officecli-setup` | 安裝並驗證 `officecli` 執行檔。全新工作階段請先執行。 |
| `pptx-cli` | 簡報 —— 建立、編輯、檢查、輸出 PNG。 |
| `docx-cli` | 報告、備忘錄、董事會文件、核決表單、追蹤修訂。 |
| `xlsx-cli` | 財務模型、KPI 工作表、樞紐分析、圖表，並支援公式即時運算。 |

| 範本 | 底色 | 強調色 | 適用情境 |
|---|---|---|---|
| **ANA Blue** | 白色 | 深藍 `#0B318F` | 對外具品牌識別的文件 —— 董事會、主管機關、投資人、客戶、合作夥伴 |
| **Yukima 雪間** | 冷調藍灰 | 石板藍 `#4B6F87` | 研究報告、ESG 與永續議題、長篇分析 |
| **Reiser Warm** | 暖米色 | 珊瑚色 `#CC785C` | 個人作業、草稿、內部思考文件 |

三者採用相同的 19 個具名版面配置，同樣的 1440 × 810 pt 格線，因此在範本之間切換屬於改樣式，而非重新製作。三者皆依 60-30-10 的面積比例建構，且所有色彩對比值一律由程式產生至 `references/contrast-matrix.md`，不以人工填寫。

**雪間**（ゆきま）是日本初春的季語，指積雪融化後露出的地面。這套配色正是如此：由雪的藍調，經新芽的綠，走到溫暖的土色；各色票也保留原本的日文季節名稱。

---

### tw-legal-rag

以語義檢索連接約 2,200 萬筆台灣裁判，以及行政函釋、稅務函釋與憲法解釋，後端為公開的 TLR 端點。**僅提供檢索** —— 不產生法律意見，也不為任何模型的輸出背書。

| Skill | 用途 |
|---|---|
| `judgment-research` | 檢索裁判與函釋、讀取全文，並以可驗證的引用作答。 |
| `citation-check` | 將判決打包給其他 AI，並查核答案是否引用了捏造的字號。 |

有兩項限制是寫進 skill 裡的，而非仰賴自律：搜尋只回傳結構化清單，**不含法院論理**，因此在描述任何法院見解之前必須先讀取全文；引用必須原樣輸出伺服器回傳的 `citation_markdown`，不可自行拼寫字號。查無結果就回報查無。

`citation-check` 對自身的能力刻意保守：`pass` 只代表引用的字號與 bundle 內的判決身份對得上 —— 不代表該段引文確實出自它所指的那一篇，也不代表法院見解被讀對了。

隨附的 MCP 伺服器（`https://tlr.dr-lawbot.com/mcp`）需要一次性的 OAuth 授權，請透過 `/mcp` 完成。其後的 REST 端點免金鑰，在授權完成前 skill 會自動改走該路徑。

封裝自 [aa0101181514/tw-legal-rag](https://github.com/aa0101181514/tw-legal-rag)（MIT）。查詢字串會送至第三方端點並可能被記錄，請先將機密事實抽象化為法律爭點。

---

## 安裝

```
/plugin marketplace add reiserwang/reiser-plugins
/plugin install office-cli@reiser-plugins
/plugin install tw-legal-rag@reiser-plugins
```

若安裝結果顯示 `Run /reload-plugins to activate.`，請執行該指令。

另一種方式：若有人直接提供 `office-cli.plugin` 檔案，開啟它即可 —— 桌面應用程式會顯示內容與安裝按鈕，不需要儲存庫存取權限。

### 私有儲存庫的驗證設定

由於本儲存庫為私有，在加入市集之前，git 必須能自行完成驗證：

```bash
gh auth setup-git                                            # 透過 HTTPS 使用 GitHub
git ls-remote https://github.com/reiserwang/reiser-plugins   # 不應出現輸入提示
```

GitHub 的 `owner/repo` 簡寫預設使用 SSH 複製。若偏好 HTTPS，請設定 `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`。

私有市集的背景自動更新會在停用認證輔助程式的情況下執行 `git pull`，因此可能間歇性失敗。以下設定可讓行為變得可預期：

```bash
export CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1   # 保留既有複本，而非重新複製
```

……然後在需要最新版本時手動更新：

```
/plugin marketplace update reiser-plugins
```

若改用 SSH 遠端並將金鑰加入 `ssh-agent`，可完全避免此問題 —— 背景拉取的驗證方式會與你自己執行指令時相同。

---

## 使用方式

不需要直接呼叫各個 skill。描述你要的產出，`house-style` 會自動判斷路徑。以下說法都可行：

```
用 ANA Blue 幫我把這份筆記做成第三季資安狀況的董事會簡報。
把這份簡報改成 Reiser Warm 樣式。
修正 deck.pptx 第 4 到 9 頁標題溢出的問題。
把這份試算表做成符合品牌樣式的 KPI 工作表。
把季報寫成 Word 文件。
```

### 全新工作階段的第一步

`officecli` 執行檔並未預先安裝。你可以說 **「設定 officecli」**，或直接開始任務讓 skill 自行處理。它的存在正是為了避開兩個陷阱：

- 官方文件提供的 curl 安裝指令（`d.officecli.ai/install.sh`）在雲端沙箱中會回傳 **403**，GitHub Releases 亦然。npm registry 可正常使用。
- `npm install -g officecli` 會安裝到**錯誤的產品** —— 一個不相關的 AI TUI 工具。正確的套件是 `@officecli/officecli`。

### 從範本開始製作簡報

這是最快也最忠於原樣的做法，因為會直接繼承母片、主題與全部 19 個版面配置：

```bash
cp plugins/office-cli/skills/house-style/templates/ana-blue/ana-blue.pptx deck.pptx
officecli open deck.pptx
officecli add  deck.pptx slide --layout 'Cover'
```

版面配置名稱、版面配置區索引與精確座標，請見 `skills/house-style/references/layouts.md`。

### 填入預留位置

範本刻意**不包含**任何機構或產品用語。頁尾與封面提供預留位置，必須自行替換：

| 預留位置 | 填入內容 |
|---|---|
| `{{ORG}}` | 頁尾所顯示的機構名稱 |
| `{{UNIT}}` | 發文的部門或單位 |
| `{{DECK_TITLE}}` / `{{DECK_TITLE_EN}}` | 標題的中文與英文 |
| `{{CLASSIFICATION}}` | 機密等級標示（若該文件需要標示） |

交付的檔案若仍含有 `{{`，即屬瑕疵。送出前請確認：

```bash
officecli view deck.pptx text | grep '{{' && echo "尚有預留位置未替換"
```

### 交付前的檢查

```bash
officecli view  deck.pptx issues                              # 溢出、對比不足、欄位過期
officecli view  deck.pptx screenshot --grid --out contact.png # 然後真的打開圖片看一遍
officecli close deck.pptx                                     # 存出，否則交付的是編輯前版本
```

中間那一步比字面上更重要：格線偏移與文字框溢出在文件模型中看不出來，在圖片上卻一目了然。

### 關於範本檔案的一條鐵則

**絕對不要直接用 PowerPoint 開啟隨附的範本。** 重新儲存會重新植入修訂追蹤資料，並把編輯者姓名寫進 `docProps/core.xml`。請先複製檔案，再編輯複本。

---

## 文件位置

```
plugins/office-cli/skills/house-style/
├── SKILL.md                 選範本、選流程、不可妥協的規則
├── references/
│   ├── grid.md              版面尺寸、邊界、欄寬計算、垂直節奏
│   ├── layouts.md           全部 19 個版面配置、每個物件、精確座標
│   ├── pipelines.md         複製範本 · deck-design/deck-build · Word 與 Excel
│   ├── contrast.md          對比度門檻與各範本的注意事項
│   └── contrast-matrix.md   程式產生 —— 三套配色的所有對比值
├── scripts/
│   └── contrast.py          重新產生對比表；--check 驗證色票與 .pptx 是否一致
└── templates/
    ├── README.md            如何新增範本
    ├── ana-blue/            TEMPLATE.md · palette.md · theme.json · ana-blue.pptx
    ├── yukima/              TEMPLATE.md · palette.md · theme.json · yukima.pptx
    └── reiser-warm/         TEMPLATE.md · palette.md · theme.json · reiser-warm.pptx
```

先讀 `SKILL.md`，再讀其中一個 `TEMPLATE.md`。其餘檔案依需要載入即可。

---

## 儲存庫結構

```
reiser-plugins/
├── .claude-plugin/
│   └── marketplace.json        # 目錄檔 —— 每個外掛都必須列在此處
├── plugins/
│   ├── office-cli/
│   │   ├── .claude-plugin/plugin.json
│   │   └── skills/
│   │       ├── house-style/    # 路由 + 共用參考文件 + templates/<name>/
│   │       ├── officecli-setup/
│   │       ├── pptx-cli/
│   │       ├── docx-cli/
│   │       └── xlsx-cli/
│   └── tw-legal-rag/
│       ├── .claude-plugin/plugin.json
│       ├── .mcp.json           # tlr 遠端 MCP 伺服器
│       └── skills/
│           ├── judgment-research/
│           └── citation-check/
├── README.md
└── README.zh-TW.md
```

`metadata.pluginRoot` 設為 `./plugins`，因此外掛的 `source` 只需填目錄名稱，不必寫完整相對路徑。

---

## 發布變更

只有在 **version 欄位改變**時，使用者才會收到更新 —— 單純推送修改過的檔案不會傳到任何人手上。

1. 修改 `plugins/<name>/` 底下的檔案。
2. **同時**更新 `plugins/<name>/.claude-plugin/plugin.json` 與 `.claude-plugin/marketplace.json` 中對應項目的 `version`。兩者必須一致；不一致是「我的修改沒生效」最常見的原因。
3. 驗證：在儲存庫根目錄執行 `claude plugin validate .`。
4. 若範本 `.pptx` 有變動，請開啟檔案確認版面配置數量、名稱與主題名稱，接著執行 `python3 scripts/contrast.py --check` 與下方的外洩檢查。
5. 提交並推送。
6. 使用者執行 `/plugin marketplace update reiser-plugins`。

### 打包成獨立的 `.plugin` 檔

若要提供給沒有儲存庫權限的人：

```bash
cd plugins/office-cli
zip -rq /tmp/office-cli.plugin . -x "*.DS_Store"
```

壓縮檔的根目錄必須直接包含 `.claude-plugin/plugin.json`，不可多包一層資料夾。

### 外洩檢查

每次發布前都應執行，變更儲存庫可見性前更是必須。請將樣式字串換成你自己的機構、單位與產品名稱。

```bash
PAT='機構名稱|單位名稱|產品名稱'

grep -rniE "$PAT" --include='*.md' --include='*.json' .

for f in $(find . -name '*.pptx'); do
  d=$(mktemp -d); unzip -qo "$f" -d "$d"
  grep -rl --include='*.xml' --include='*.rels' -iE "$PAT" "$d" && echo "LEAK in $f"
  grep -o '<cp:lastModifiedBy>[^<]*' "$d/docProps/core.xml"
  rm -rf "$d"
done
```

`lastModifiedBy` 那一行是最容易被忽略的。個人姓名就是這樣混進「已去識別化」的範本裡的。

---

## 新增其他外掛

```bash
mkdir -p plugins/new-plugin/.claude-plugin
# 撰寫 plugins/new-plugin/.claude-plugin/plugin.json
```

接著在 `.claude-plugin/marketplace.json` 的 `plugins` 陣列中新增一筆 —— 沒有列在其中的外掛目錄，對市集而言等同不存在。

---

## 維護說明

`office-cli` 隨附上游 OfficeCLI skill 檔案的快照作為參考資料。它們會與實際安裝的 `officecli` 執行檔逐漸產生落差，各 skill 內也已註明 —— 執行時應以 `officecli help <format> <element>` 為準。更新外掛版本時，正是重新拉取上游 skill、確認 schema 是否變動的時機。

`skills/*/references/officecli-*.md` 底下的參考檔案來自 [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)，採用 Apache-2.0 授權。詳見 `LICENSE-officecli.txt` 與 `NOTICE-officecli.txt`。

已針對 officecli **1.0.144** 驗證。
