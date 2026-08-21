# reiser-plugins

[English](README.md) · **繁體中文**

Claude 外掛市集 — Office 文件工具與版型樣式範本。

> **私有儲存庫。** 這些外掛內含版型樣式設定。在變更儲存庫可見性之前，請重新檢視每一個 skill，**並解壓縮每一個隨附的 `.pptx`**，確認沒有機構名稱、產品名稱、藍圖規劃用語、合作夥伴名稱、設備型號、機密等級標示、內部檔案路徑與個人識別資訊 —— 這些都不該出現在公開儲存庫。`.pptx` 內的 `docProps/core.xml` 會記錄最後編輯者姓名，務必檢查。請參閱 [外洩檢查](#外洩檢查)。

---

## 內容概要

一個外掛 `office-cli`，包含五個 skill 與兩套可互換的設計範本。

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
| **Reiser Warm** | 暖米色 | 珊瑚色 `#CC785C` | 個人作業、草稿、內部思考文件 |

兩者採用相同的 19 個具名版面配置，同樣的 1440 × 810 pt 格線，因此在兩套範本之間切換屬於改樣式，而非重新製作。

---

## 安裝

```
/plugin marketplace add reiserwang/reiser-plugins
/plugin install office-cli@reiser-plugins
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
│   └── contrast.md          對比度門檻與所有已驗證的比值
└── templates/
    ├── README.md            如何新增第三套範本
    ├── ana-blue/            TEMPLATE.md · palette.md · theme.json · ana-blue.pptx
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
│   └── office-cli/
│       ├── .claude-plugin/plugin.json
│       └── skills/
│           ├── house-style/    # 路由 + 共用參考文件 + templates/<name>/
│           ├── officecli-setup/
│           ├── pptx-cli/
│           ├── docx-cli/
│           └── xlsx-cli/
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
4. 若範本 `.pptx` 有變動，請開啟檔案確認版面配置數量、名稱與主題名稱，並執行下方的外洩檢查。
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
