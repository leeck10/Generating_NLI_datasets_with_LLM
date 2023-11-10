# Chain-of-Thought와 Program-aided Language Models을 이용한 전제-가설-라벨 삼중항 자동 생성

# Introduction 
자연어 추론은 두 문장(전제, 가설)간의 관계를 이해하고 추론하여 함의, 모순, 중립 세 가지 범주로 분류하며, 전제-가설-라벨(PHL) 데이터셋을 활용하여 자연어 추론 모델을 학습한다. 그러나, 새로운 도메인에 자연어 추론을 적용할 경우 학습 데이터가 존재하지 않거나 이를 구축하는 데 많은 시간과 자원이 필요하다는 문제가 있다. 본 논문에서는 자연어 추론을 위한 학습 데이터인 전제-가설-라벨 삼중항을 자동생성하기 위해 [1]에서 제안한 문장 변환 규칙 대신에 거대 언어 모델과 Chain-of-Thought(CoT),Program-aided Language Models(PaL) 등의 프롬프팅(Prompting) 방법을 이용하여 전제-가설-라벨 삼중항을 자동으로 생성하는 방법을 제안한다. 실험 결과, CoT와 PaL 프롬프팅 방법으로 자동 생성된 데이터의 품질이 기존 규칙이나 기본 프롬프팅 방법보다 더 우수하였다.

# References
조희진, 이창기, 배경만. Chain-of-Thought와 Program-aided Language Models을 이용한 전제-가설-라벨 삼중항 자동 생성, HCLT2023, 352~357
