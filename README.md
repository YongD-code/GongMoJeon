# 공모전

Unreal Engine 프로젝트입니다.

## 열기

1. Unreal Engine을 설치합니다.
2. `공모전.uproject` 파일을 Unreal Editor로 엽니다.
3. 필요한 경우 에디터에서 프로젝트 파일을 다시 생성합니다.

## GitHub 업로드 안내

이 저장소는 Unreal Engine의 생성 파일(`Saved/`, `Intermediate/`, `DerivedDataCache/` 등)을 Git에서 제외하고, `.uasset`과 `.umap` 같은 큰 바이너리 에셋은 Git LFS로 관리하도록 설정되어 있습니다.

처음 내려받는 사람은 다음 명령을 한 번 실행하면 됩니다.

```powershell
git lfs install
git lfs pull
```
