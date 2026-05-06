import torch
import torch.nn as nn

# Marabou 검증을 위한 작은 외부 모델 정의
class TinyMNIST(nn.Module):
    def __init__(self):
        super(TinyMNIST, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 16)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(16, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = self.relu(self.fc1(x))
        return self.fc2(x)

if __name__ == "__main__":
    model = TinyMNIST()
    # 더미 입력 (1 배치, 1 채널, 28x28 이미지)
    dummy_input = torch.randn(1, 1, 28, 28)
    
    # Marabou에서 지원하는 ONNX 포맷으로 내보내기
    torch.onnx.export(
        model, 
        dummy_input, 
        "mnist_small.onnx", 
        input_names=["input"], 
        output_names=["output"]
    )
    print("mnist_small.onnx 외부 모델이 성공적으로 생성됨.")
