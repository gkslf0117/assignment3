Assignment #3 Neural Network Verification with Marabou

이 과제는 SMT 기반의 신경망 검증 도구인 Marabou를 사용하여, 외부에서 생성한 PyTorch 모델의 강건성을 수학적으로 증명하는 것입니다.

1. Project Overview
- Model: `TinyMNIST` (2-layer Fully Connected Network)
- Framework: PyTorch, Marabou (maraboupy)
- Goal: 입력값의 미세한 변화에 대해 모델의 분류 결과가 변하지 않는지 수학적으로 검증합니다.

2. Repository Structure
- gen_model.py: PyTorch를 사용하여 검증용 외부 모델을 설계하고 ONNX 포맷으로 내보내는 스크립트입니다.
- test.py: Marabou Python API를 사용하여 입력 제약 조건을 설정하고 검증(SAT/UNSAT)을 수행하는 메인 스크립트입니다.
- requirements.txt: 프로젝트 실행에 필요한 외부 라이브러리 목록입니다.
- mnist_small.onnx: 생성된 외부 모델 파일입니다.
- report.pdf: 실험 과정, 결과 분석 및 Marabou 사용 경험을 정리한 보고서입니다.

3. Environment Setup
Prerequisites
- Ubuntu (또는 WSL2 환경 권장)
- Python 3.8+
- Marabou가 시스템에 빌드되어 있어야 하며, `maraboupy`가 설치되어 있어야 합니다.

Installation

-1. 의존성 라이브러리 설치
pip install -r requirements.txt

-2. Marabou 빌드 및 환경변수 설정 



4. How to Run
Step 1: 먼저 검증에 사용할 외부 모델을 생성합니다.

python gen_model.py


Step 2: 생성된 모델을 대상으로 Marabou 검증을 실행합니다.

python test.py



5. Verification SpecificationInput Constraints: 픽셀 기준값 $0.5$를 중심으로 $\epsilon=0.01$ 범위의 $L_\infty$  제약 조건을 설정합니다. ($0.49 \le x_i \le 0.51$)Output Property: 입력 데이터가 Class 0으로 분류되어야 하는 상황에서, Class 1의 점수가 Class 0보다 높아질 수 있는 지점(output[1] > output[0])이 존재하는지 확인합니다.




6. ResultsResult: SAT Findings: 미세한 노이즈($\epsilon=0.01$)가 추가될 때 모델이 Class 1 또는 다른 클래스로 오분류할 수 있는 취약점을 발견하였습니다.





#Acknowledge
과제 구현 과정에서 OpenAI의 도움을 받았음 밝힙니다.



