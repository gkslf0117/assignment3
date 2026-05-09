from maraboupy import Marabou
import numpy as np

def run_verification():
    print("Loading ONNX model into Marabou...")
    # 생성한 모델 로드
    network = Marabou.read_onnx("mnist_small.onnx")

    # 1. 변수 추출 및 Flatten 
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
