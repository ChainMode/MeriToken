# 用語集（ja）

本用語集は iFay ブループリント多言語ドキュメントの唯一の権威辞書である。`Reserved_Term` の表に記載された項目はすべての言語版において英語原語のまま保持し、翻訳しない。`Localized_Term` の表に記載された項目は対象言語に応じて主称呼を切り替える。`Reserved_Term` でも `Localized_Term` でもない項目については、各言語が現地の慣習に従って訳す。

## Reserved_Term（すべての言語で英語原語を保持）

| 英語原語 | 説明 | 翻訳方針 | 参考リンク（Upstream_Project_Doc_Link） |
|----------|------|----------|---------------------------------------|
| iFay / ifay | iFay プロジェクト生態系の名称。アバター文脈では、`iFay`（Individual Fay）は単一の `Human Prime` に 1:N で結び付けられた個人デジタル分身を指す | Reserved：すべての言語で英語原語を保持 | https://ifay.ai |
| agent | エージェント（従来の LLM 体系で自律的にタスクを実行するプログラム実体を指す） | Reserved：すべての言語で英語原語を保持 | https://ifay.ai |
| phase | フェーズ（ブループリントにおける進化段階の番号） | Reserved：すべての言語で英語原語を保持し、番号はそのまま後置（例：`phase 1`） | — |
| credential | `Human Prime` または `Fay` 主体の身元と権属を裏付ける資格情報 | Reserved：すべての言語で英語原語を保持 | ./05-meritoken-credential.md |
| GMChain | Global Merit Chain、MeriToken が属する非貨幣的な社会貢献計量・ガバナンス上位体系 | Reserved：すべての言語で正規略称 `GMChain` を保持 | ./01-meritoken-overview.md |
| Fay | iFay 体系における自律的デジタル分身の総称（`Fay = iFay + coFay`）。`iFay` は単一の `Human Prime` に錨付けられた個人分身であり、`coFay` は説明責任を持つ自然人または組織に単層帰属する非個人の公共役割協働分身である | Reserved：すべての言語で英語原語を保持 | ./04-meritoken-usage.md |
| Human Prime | iFay 体系において対応付けられ、最終的な説明責任を担う自然人主体 | Reserved：英語原語 `Human Prime` を保持 | https://ifay.ai |
| Host | `Fay` が稼働・制御を行う端末ハードウェア機器、クライアントアプリ、または実行環境のみを指す（自然人を指すことは決してない） | Reserved：英語原語 `Host` を保持 | https://ifay.ai |

## Localized_Term（対象言語に応じて主称呼を切り替え）

| 英語原語 | 中国語の主称呼 | 処理ルール |
|----------|----------------|------------|
| MeriToken | 美誉值 | `zh-CN` および `zh-TW` の本文では「美誉值」（`zh-TW` では「美譽值」）を主称呼として用い、当該言語版で初出箇所に限り括弧書きで英語原語 `MeriToken` を併記してよい。`en`、`de`、`es`、`fr`、`ja`、`ko`、`ru` の本文では英語原語 `MeriToken` を用い、現地化された訳語に置き換えてはならない。 |

## MeriToken_Chinese_Name に関する注記

「美誉值」は MeriToken の中国語主称呼であり、`zh-CN` および `zh-TW` のブループリント本文においてのみ当該概念の通常呼称として用いられる。MeriToken は厳格に非貨幣的な社会貢献評価尺度であり、換金・投機・譲渡の対象ではない。その他の言語版（`en` を含む）では「美誉值」の文字列は出現しない。

## 非 Reserved 項目

| 中国語 | 英訳の参考 | 備考 |
|--------|------------|------|
| ブループリント | blueprint | 各言語が現地の慣習に従って訳す。 |
| 校正 | review | — |
| 資格情報の管理 | credential management | 「credential」を原語のまま保持する場合は、全体として「credential 管理」と訳す。 |
