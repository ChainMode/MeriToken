# 용어집 (ko)

본 용어집은 iFay 블루프린트 다국어 문서의 유일한 권위 사전이다. `Reserved_Term` 표에 기재된 항목은 모든 언어 버전에서 영문 원어 그대로 유지하며 번역하지 않는다. `Localized_Term` 표에 기재된 항목은 대상 언어에 따라 주 호칭을 전환한다. `Reserved_Term` 도 `Localized_Term` 도 아닌 항목은 각 언어가 현지 관행에 따라 번역한다.

## Reserved_Term (모든 언어에서 영문 원어 유지)

| 영문 원어 | 설명 | 번역 방침 | 참고 링크 (Upstream_Project_Doc_Link) |
|-----------|------|-----------|---------------------------------------|
| iFay / ifay | iFay 프로젝트 생태계의 명칭. 분신 맥락에서 `iFay` (Individual Fay)는 단일 `Human Prime` 에 1:N 으로 귀속되는 개인 디지털 분신을 가리킨다 | Reserved: 모든 언어에서 영문 원어 유지 | https://ifay.ai |
| agent | 에이전트 (전통적인 LLM 체계에서 작업을 자율적으로 수행하는 프로그램 개체를 가리킴) | Reserved: 모든 언어에서 영문 원어 유지 | https://ifay.ai |
| phase | 단계 (블루프린트의 진화 단계 번호) | Reserved: 모든 언어에서 영문 원어 유지하고 번호는 그대로 후치 (예: `phase 1`) | — |
| credential | `Human Prime` 또는 `Fay` 주체의 신원과 권리·소유 관계를 뒷받침하는 자격 증명 | Reserved: 모든 언어에서 영문 원어 유지 | ./05-meritoken-credential.md |
| GMChain | Global Merit Chain, MeriToken 이 속하는 비화폐적 사회 기여 측정 및 거버넌스 상위 체계 | Reserved: 모든 언어에서 정규 약칭 `GMChain` 유지 | ./01-meritoken-overview.md |
| Fay | iFay 체계 내 자율 디지털 분신의 총칭 (`Fay = iFay + coFay`). `iFay` 는 단일 `Human Prime` 에 고정된 개인 분신이며, `coFay` 는 책임 자연인 또는 조직에 단층 귀속되는 비개인 공공 역할 협업 분신이다 | Reserved: 모든 언어에서 영문 원어 유지 | ./04-meritoken-usage.md |
| Human Prime | iFay 체계에서 매핑되고 최종 책임을 부담하는 자연인 주체 | Reserved: 영문 원어 `Human Prime` 유지 | https://ifay.ai |
| Host | `Fay` 가 실행되거나 권한 제어를 수행하는 단말 하드웨어 기기, 클라이언트 애플리케이션 또는 실행 환경만을 가리킨다 (절대 자연인을 가리키지 않음) | Reserved: 영문 원어 `Host` 유지 | https://ifay.ai |

## Localized_Term (대상 언어에 따라 주 호칭 전환)

| 영문 원어 | 중국어 주 호칭 | 처리 규칙 |
|-----------|----------------|-----------|
| MeriToken | 美誉值 | `zh-CN` 및 `zh-TW` 본문에서는 “美誉值” (`zh-TW`: “美譽值”)를 주 호칭으로 사용하며, 해당 언어 버전에서 처음 등장하는 위치에 한해 괄호 안에 영문 원어 `MeriToken` 을 병기할 수 있다. `en`, `de`, `es`, `fr`, `ja`, `ko`, `ru` 본문에서는 영문 원어 `MeriToken` 을 사용하며 현지화된 역어로 대체해서는 안 된다. |

## MeriToken_Chinese_Name 에 대한 비고

“美誉值”는 MeriToken 의 중국어 주 호칭이며, `zh-CN` 및 `zh-TW` 블루프린트 본문에서만 해당 개념의 일반 호칭으로 사용된다. MeriToken 은 엄격히 비화폐적인 사회 기여 평판 척도로서 현금화·투기·양도의 대상이 아니다. 그 외의 언어 버전 (`en` 포함) 에서는 “美誉值” 문자열이 등장하지 않는다.

## 비 Reserved 항목

| 중국어 | 영역 참고 | 비고 |
|--------|-----------|------|
| 블루프린트 | blueprint | 각 언어가 현지 관행에 따라 번역한다. |
| 검수 | review | — |
| 자격 증명 관리 | credential management | “credential” 을 원어로 유지하는 경우, 전체적으로 “credential 관리”로 옮긴다. |
