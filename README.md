# degradation_dataset
2 ways for SR_dataset trans2 LR_dataset using degradation ..使用传统退化算法把SR转成LR---两种方法
the way1 from paper named :Towards Real-World Blind Face Restoration with Generative Facial Prior.
Github:https://github.com/TencentARC/GFPGAN

this paper using a GAN to create SR image for face.
detils for the way to create SR image.
![image](https://github.com/andre20000131/degradation_dataset/assets/95755599/6ce45f0d-8cbd-43bd-8564-2178e95010d3)



the way2 from :https://github.com/cszn/BSRGAN/tree/main/utils

we changed code for direct create dataset for model train.easy to see...

EN：
Detailed usage:
Method 1: We need to use Python test in the way1/test_ffhq_degradation_dataset.py to run the script.
Running this script requires the pip install gfpgan library. When installing this library, errors may be reported. If the installation fails, you can refer to this blog: [https://blog.csdn.net/qq_40962125/article/details/134374318?spm=1001.2014.3001.5502](https://blog.csdn.net/qq_40962125/article/details/134374318?spm=1001.2014.3001.5502)
If there are no issues with the environment, it can be run. way1 is strictly generated according to the dataset generation method in the paper.

Method 2: Simply run way2. py.
The method called in Method 2 always has a random effect each time. In fact, you can add a loop before the production effect line of code, and loop 20 times on an image to see the random effect each time. Another point worth noting is that I used sf and lq_ Corresponding to each random selection from 0 and 1, this sf represents the sampling rate, lq_ Represents the size of the patch, and their product is
The resolution of the production image is because all the images I input are 1024 * 1024. In order to generate the corresponding dataset, I need to ensure that the generated result is also 1024 resolution. This can be modified according to the actual situation.

CN：
详细用法：
方法1:我们需要在way1目录下，使用python test_ffhq_degradation_dataset.py 去运行脚本。
运行这个脚本需要pip install gfpgan 这个库。安装这个库的时候可能会报错，如果安装失败可以参考这个博客：https://blog.csdn.net/qq_40962125/article/details/134374318?spm=1001.2014.3001.5502
环境没有问题的话运行即可，way1是严格按照论文中的数据集生成方式做的。

方法2:直接运行way2.py即可。
方法2调用的方法每次都是随机的效果，其实可以在生产效果那一行代码前加入循环，对一张图片循环20次效果看一下每次的随机效果，还有一点值得注意，我是把sf和lq_对应好了从0，1中每次随机选择，这个sf表示采样率，lq_表示patch大小，他们的乘积是
生产图像的分辨率，因为我所有送入的图像都是1024*1024，我为了生成对应的数据集，我要保证生成的结果也是1024分辨率。这是可以根据实际情况修改的。



SR_dataset:
https://pan.baidu.com/s/1zEQ-TPxJFv-f6_qQwuk3MA#list/path=%2Fsharelink891313769-336542142550031%2FFFHQ&parentPath=%2Fsharelink891313769-336542142550031
9bfh

