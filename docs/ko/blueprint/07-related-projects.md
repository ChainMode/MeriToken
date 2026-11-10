# 07 ifay 체계와의 관계

> 본 문서는 “최소 필요 위치 설명 + 공식 문서 페이지 외부 링크 목록” 의 형태로, ifay 체계 내 몇몇 상위 주제와 MeriToken 블루프린트의 관계를 수렴하여, 본 저장소 내에서 상위 주제를 길게 풀어 쓰는 일을 회피한다.

## 배경

본 저장소의 블루프린트는 MeriToken 의 심층 분석을 주축으로 한다. ifay, GMC, Fay, agent, phase, 전체 프레임워크 등의 주제는 MeriToken 분석에 필요한 보조 배경으로 자리매김할 뿐, 본 저장소의 집필 목표는 아니다.

유지보수 비용과 버전 표류를 회피하기 위해, 본 블루프린트는 위의 상위 주제에 대해 저장소 안에서 장문의 서술을 전개하지 않는다. 각 주제에는 MeriToken 과 관련된 최소 필요 위치 설명만 제공하고, ifay.ai 상의 해당 공식 문서 페이지를 가리키는 외부 링크를 통해 독자를 상위 프로젝트의 권위 있는 서술로 안내한다.

독자가 ifay 체계를 처음 접한다면, 본 문서를 “외부 링크 진입 페이지” 로 사용할 것을 권장한다. 먼저 공식 문서 외부 링크 목록의 링크에 따라 빠르게 상위 배경을 구축한 뒤, [01-meritoken-overview.md](./01-meritoken-overview.md) 로 돌아와 주선에 진입한다.

## 본 블루프린트와의 관계

다음 상위 용어들은 본 블루프린트에서 “최소 설명” 의 형태로 등장하며, MeriToken 과의 최소 연결은 다음과 같다.

- **ifay**: 프로젝트 체계의 명칭이며, MeriToken 이 의지하는 전반적인 기술 및 사회 운영 환경이다. 본 블루프린트는 ifay 체계 자체를 풀어 쓰지 않으며, MeriToken 의 운영 환경을 기술할 때 필요에 따라서만 ifay 를 인용한다.
- **GMC**: Global Merit Chain, MeriToken 의 상위 체계. 본 블루프린트는 [01-meritoken-overview.md](./01-meritoken-overview.md) 에서 MeriToken 과 GMC 의 종속 관계를 설명하며, GMC 의 전체 설계는 풀어 쓰지 않는다.
- **Fay**: ifay 체계 안에서 “MeriToken 을 참조한다” 는 역할을 담당하는 비개인 주체이며, 개인 주체와 함께 MeriToken 의 두 가지 참조자 중 하나다. 본 블루프린트는 [04-meritoken-usage.md](./04-meritoken-usage.md) 에서 MeriToken 을 참조하는 Fay 주체의 참조 방식과 응용 시나리오를 독립적으로 다룬다.
- **agent**: 전통적인 LLM 체계에서 작업을 자율적으로 수행하는 프로그램 개체이며, ifay 패러다임에서 MeriToken 의 참조자인 개인 주체 / Fay 주체와 대조를 이룬다. 본 블루프린트는 agent 와 ifay 패러다임의 차이를 풀어 쓰지 않으며, 외부 링크에서 권위 있는 정의의 진입점만 제공한다.
- **phase**: 블루프린트가 속한 프로젝트의 진화 단계 번호. 구체적인 단계 의미론, 타임라인, 마일스톤은 ifay.ai 문서가 유지하며, 본 저장소는 다시 풀어 쓰지 않는다.
- **전체 프레임워크**: ifay 프로젝트의 전반적 아키텍처와 각 구성 요소의 상호 작용 관계. 본 저장소의 블루프린트는 MeriToken 이라는 구성 요소에 초점을 맞추며, 전체 프레임워크는 ifay.ai 상의 해당 공식 문서 페이지를 직접 방문할 것.

## 공식 문서 외부 링크 목록

다음 표는 본 블루프린트에 필요한 최소 외부 링크 집합을 제시하며, 링크 형태는 “ifay.ai 상의 해당 공식 문서 페이지를 가리키는” 것으로 고정된다. 구체적인 URL 은 설계 계층에서 고정하였으며, `ifay.ai` 가 아닌 도메인으로 대체하는 것은 허용되지 않는다.

| 상위 용어 | 본 블루프린트에서의 최소 설명 | Upstream_Project_Doc_Link |
|-----------|--------------------------------|---------------------------|
| ifay     | MeriToken 이 의지하는 전반적 프로젝트 체계 | https://ifay.ai/docs/ifay |
| GMC      | MeriToken 의 상위 체계 (Global Merit Chain) | https://ifay.ai/docs/gmc |
| Fay      | 비개인 주체의 MeriToken 참조자, 개인 주체와 나란히 함 | https://ifay.ai/docs/fay |
| agent    | ifay 패러다임과 대조를 이루는 전통적 대리 프로그램 패러다임 | https://ifay.ai/docs/agent |

phase, 전체 프레임워크 등 그 외의 상위 주제는 ifay.ai 사이트 안에 전용 페이지가 마련되어 있으며, 독자가 필요에 따라 사이트 내비게이션에서 검색해 방문하면 된다. 본 블루프린트에서는 링크 표류를 회피하기 위해 본 목록에 그 링크를 고정하지 않는다.

## 용어 각주

본 문서에 등장하는 `Reserved_Term`:

- **ifay**: 프로젝트 체계 명칭. 자세한 내용은 [glossary.md](./glossary.md) 를 참조.
- **GMC**: Global Merit Chain, MeriToken 의 상위 체계. 자세한 내용은 [glossary.md](./glossary.md) 를 참조.
- **Fay**: 비개인 주체의 MeriToken 참조자. 자세한 내용은 [glossary.md](./glossary.md) 를 참조.
- **agent**: 전통적인 LLM 체계에서의 에이전트. 자세한 내용은 [glossary.md](./glossary.md) 를 참조.
- **phase**: 블루프린트의 진화 단계 번호. 자세한 내용은 [glossary.md](./glossary.md) 를 참조.

MeriToken 의 중국어 주 호칭은 `zh-CN` 과 `zh-TW` 블루프린트 본문에서만 해당 개념의 일반 호칭으로 사용된다. 자세한 내용은 [glossary.md](./glossary.md) 의 `Localized_Term` 절을 참조.
