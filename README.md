# ComputerVision_TeamProject
간소화된 CUB-200-2011 데이터셋을 이용하여 정확도 끌어올리기 프로젝트.<br>
코랩 환경에서 wandb, data augmentation 기법 등 적용

## Active Learning 1
기본 제공된 resnet18 모델을 활용하여 data augmentation, hyperparameter tuning, wandb, gradCAM 등을 활용해
성능을 올리고 분석.

### Data Augmentation

After applying various augmentation techniques to the original image, learning was performed by creating a combination of the original image and various
techniques.<br>
The analysis conducted through wandb revealed that applying rotation, flip, zoom, and crop techniques for augmentation on the original images resulted in the highest accuracy and the lowest loss.

## Active Learning 2


### Introduction

**1. Goal**: Improve fine-grained classification accuracy by modifying the model with our ideas <br>
**2. Key Idea**
- **a. Augmentation**: By transforming the existing training data in various ways to virtually increase the size of the dataset, overfitting is prevented.
- **b. Resnet-D**: Used a modified version of ResNet-50, known as ResNet-D, to train an image dataset that underwent an augmentation process, resulting in improved accuracy.<br>


**3. Result**: 96.3%

### Model
<img width="487" alt="image" src="https://github.com/9-coding/ComputerVision_TeamProject/assets/127665166/cea8b19d-3184-45d8-8b8f-cccc5ca213a0">

**Architecture** <br><br>
Resnet50-B
- Avoid ignoring 3/4 of the input feature map
- Change the structure of the first two conv blocks of path A in the downsampling block.<br>

Resnet50-C
- Minimize computational cost
- Change the 7x7 conv of the input stem to three 3x3 convs<br>

Resnet50-D<br>
<img width="513" alt="image" src="https://github.com/9-coding/ComputerVision_TeamProject/assets/127665166/83434482-e86f-4c80-994e-cef74dc08aaf">
- Combining ResNet-B and ResNet-C
- Add method of ResNet-D
- Highest performance
- Little increase computational cost (FLOPs)(15%)
- Little increase Training time(3%)
- Prevent information loss
- Change Path B's 1x1 conv to avgpool + 1x1 conv structure

### Experiments
**Setting models**
<img width="951" alt="image" src="https://github.com/9-coding/ComputerVision_TeamProject/assets/127665166/da78e3fb-e6cc-468c-b2cc-855c141526ae"><br>
Compare with resnet50d, resnext101, resnet50, resnet101, resnet152, densenet121, densenet161, vgg16, ViT, efficientnet-b4, efficientnet-b7, efficientnet-v2, and inception_v3.<br>
Then, resnet50d has the highest accuracy.

### Conclusion
![image](https://github.com/9-coding/ComputerVision_TeamProject/assets/127665166/44e02002-3493-4924-a231-bad809433d69)


- GradCAM
![image](https://github.com/9-coding/ComputerVision_TeamProject/assets/127665166/5a544a5e-5474-4cd2-89e4-33ee82a6a42d)

