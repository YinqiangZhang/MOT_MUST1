# 之江实验室行人多目标跟踪方法运行代码
---
# 依赖项
- Cuda 8.0
- Cudnn 7.0
- Python 3.7
- Pytorch 1.0.1
- MATLAB R2017b

*环境配置示例*
<pre><code>conda create -n mot anaconda python=3.7
conda activate mot
conda install -c menpo opencv
conda install pytorch torchvision cudatoolkit=8.0 -c pytorch
</code></pre>

# 使用方法
1. 下载 ReID 已训练神经网络模型
2. 下载之江实验室测试视频，放置于“./TrackingCode/data”文件夹中
3. 生成标准格式的测试数据文件，位于 “./TrackingCode/data/MOT_ZJ” 文件夹中
4. 进入 "ECO/" 文件夹中, 运行脚本 install.m 编译ECO跟踪器
5. 运行服务器脚本
<pre><code>python similarity_calculate.py
</code></pre>
6. 在MATLAB中运行客户端脚本 MUST_demo.m 跟踪结果位于“./TrackingCode/results/ 文件夹中
7. 如获取比赛所需格式的txt结果文件，运行脚本文件，结果文件位于 “./TrackingCode/modified_results/文件夹中
<pre><code>python resultFormatChange.py
</code></pre>

# References
[1] Danelljan, M., Bhat, G., Khan, F.S., Felsberg, M.: ECO: Efficient convolution operators for tracking. In: CVPR (2017)

[2] Xiang, Y., Alahi, A., Savarese, S.: Learning to track: Online multi-object tracking by decision making. In: ICCV (2015)

[3] Zhu, J., Yang, H., Liu, N., Kim, M., Zhang, W., Yang, M.: Online Multi-Object Tracking with Dual Matching Attention Networks. In: ECCV (2018)
