# 다른 컴퓨터에서 시작 (Windows)

저장소: https://github.com/gncorpseo-commits/AICE_ASSOCIATE

## 1. 설치

- [Git](https://git-scm.com/download/win)
- [Python 3.12](https://www.python.org/downloads/) — **Add python.exe to PATH** 체크

설치 후 **새 PowerShell**을 엽니다.

```powershell
py -3.12 --version
git --version
```

둘 다 버전이 나오면 됩니다.

## 2. 받기 + Jupyter 켜기

```powershell
git clone https://github.com/gncorpseo-commits/AICE_ASSOCIATE.git AICE_Associate_samples
cd AICE_Associate_samples
py -3.12 -m pip install numpy pandas matplotlib seaborn scikit-learn jupyter notebook ipykernel tensorflow
py -3.12 -m notebook
```

이미 폴더가 있으면:

```powershell
cd AICE_Associate_samples
git pull
py -3.12 -m notebook
```

첫 pip는 5~15분 걸릴 수 있습니다. 창을 닫지 마세요.

정상: `Collecting numpy` 같은 설치 로그, 그다음 브라우저.
비정상: `>>>` Python 입력창 → 창을 닫고 위 `py -3.12 -m` 명령을 쓰세요. `start_study.bat` 은 쓰지 마세요.

## 3. 무엇을 여나

| 목적 | 파일 |
|------|------|
| 시험 직전 공식 샘플 (회귀) | `official_samples/regression/problem.ipynb` |
| 시험 직전 공식 샘플 (분류) | `official_samples/classification/problem.ipynb` |
| 평소 학습 | `mock_exams/level_1_basic/mock_01_delivery.ipynb` 부터 |
| 채점 | 같은 이름의 `*_solution.ipynb` / `answer_keys.md` |

셀은 위에서부터 Shift+Enter 로 실행하세요. 노트북과 CSV는 같은 폴더에 있습니다.

## 4. 같은 문제를 다시 풀 때

답을 쓰고 저장하면 그 파일이 끝난 시험지가 됩니다. 빈칸으로 되돌리려면:

```powershell
git checkout -- official_samples/regression/problem.ipynb
git checkout -- mock_exams/level_1_basic/mock_01_delivery.ipynb
```

노트북을 닫았다가 다시 엽니다. `Kernel → Restart & Clear Output` 은 출력만 지우고, 적어 둔 코드는 남습니다.
