# degradation_dataset
2 ways for SR_dataset trans2 LR_dataset using degradation ..使用传统退化算法把SR转成LR---两种方法
the way1 from paper named :Towards Real-World Blind Face Restoration with Generative Facial Prior.
Github:https://github.com/TencentARC/GFPGAN

this paper using a GAN to create SR image for face.
detils for the way to create SR image.
![image](https://github.com/andre20000131/degradation_dataset/assets/95755599/6ce45f0d-8cbd-43bd-8564-2178e95010d3)



the way2 from :https://github.com/cszn/BSRGAN/tree/main/utils

we changed code for direct create dataset for model train.easy to see...


详细用法：
方法1:我们需要在way1目录下，使用python test_ffhq_degradation_dataset.py 去运行脚本。
运行这个脚本需要pip install gfpgan 这个库。安装这个库的时候可能会报错，如果安装失败可以参考这个博客：https://blog.csdn.net/qq_40962125/article/details/134374318?spm=1001.2014.3001.5502
环境没有问题的话运行即可，way1是严格按照论文中的数据集生成方式做的。

方法2:直接运行way2.py即可。
