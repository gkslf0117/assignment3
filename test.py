from maraboupy import Marabou
import numpy as np

def run_verification():
    print("Loading ONNX model into Marabou...")
    # 생성한 모델 로드
    network = Marabou.read_onnx("mnist_small.onnx")

    # 1. 변수 추출 및 Flatten (반복문 밖에서 수행)
    input_vars = network.inputVars[0].flatten()
    output_vars = network.outputVars[0].flatten()

    epsilon = 0.01
    base_val = 0.5 
    
    # 2. 입력 제약 조건 설정
    print(f"Setting up input constraints (L-infinity perturbation, epsilon={epsilon})...")
    for i in range(len(input_vars)):
        # .item()을 붙여서 numpy 타입을 순수 파이썬 float/int로 변환 (unhashable 에러 방지)
        var_index = input_vars[i].item()
        network.setLowerBound(var_index, max(0.0, base_val - epsilon))
        network.setUpperBound(var_index, min(1.0, base_val + epsilon))

    # 3. 출력 제약 조건 설정 (Infinite Bounds 에러 방지)
    print("Setting up output constraints...")
    for var in output_vars:
        network.setLowerBound(var.item(), -100.0)
        network.setUpperBound(var.item(), 100.0)

    # 4. 목적 제약 조건 (Class 1 > Class 0 인 경우가 있는지 확인)
    # output[1] - output[0] > 0
    network.addInequality([output_vars[1].item(), output_vars[0].item()], [1, -1], 0.0) 

    # 5. 실행 
    print("Running Marabou Verification...")
    options = Marabou.createOptions(verbosity=0)
    exitCode, vals, stats = network.solve(options=options)

