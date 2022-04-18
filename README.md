<h1 align="center">SafeWay</h1>

## :star: Introduction and Use case
This application is a video analytics pipeline powered by Nvidia's Jetson Nano and TensorRT. It is useful for those who work day in and day out for the safety of roads which are used by us and hence reduce the risk of accidents.<br><br> 
Poor driving areas are caused by a combination of seasonal and traffic conditions. Maintaining these areas are a must since they cause enormous hazard to drivers and may lead to fatal accidents. One of the reason for accidents are the condition of the roads too! <br>
This application helps in segmenting the different kinds of roads such as Paved Road, Unpaved Road, Asphalt Road, Road Marking, potholes, etc. Nowadays we have cameras on all the new cars, facing the road in the front for assisted driving. When images are collected of the road for assisted driving, this application can be simultaneously used to segment areas or parts of the road that are hazardous for the driver. This information can then be passed on to the local body to notify them about the bad condition of the road along with relevant details.<br>
At present, a camera can be mounted on a car such that we get a good view of the road. Then we can have a Nano mounted inside the car which will keep running the inference and keep collecting relevant data. On large scale, Jetson Xavier could be used with multiple camera inputs (say 3 or 4 cameras) which then can be streamed over DeepStream with our TensorRT model to enhance the entire pipeline! <br><br> 
Also, this application can be used by a car to notify other cars behind itself about the condition of the road ahead so that either they can take another route or drive with caution. This can be achieved by V2V or V2X communication systems.<br><br> 
This type of segmented data would not compulsorily be monetized but can be collect in a crowd sourced manner that means anyone with such technology in their car can collect the data and this data can then be initiated to a government body, free of cost for people's safety.
This application can also detect lane markings hence helping local body to mark lanes if absent.<br>
In the case of an accident, this segmented data can be utilized to understand the type of road where accidents take place, whether is it paved or unpaved or asphalt.

## :framed_picture: Demo

https://user-images.githubusercontent.com/39203466/163759582-6ba6ce39-9856-4e33-8397-aea84ea68080.mp4

Same video is available on YouTube too! Watch it [here](https://www.youtube.com/watch?v=yXEIZMEm_uY).

## :hammer_and_wrench: Steps to run this repo

<ol>
    <li>Clone this repo</li>
    <li>Make sure you have <a href="https://github.com/dusty-nv/jetson-inference">this</a> repo setup and is running.</li>
    <li>Move to safeway_inference</li>
    <li>Download my trained weight file from <a href="https://drive.google.com/file/d/1FcWa_sNwL2Jg19GL97ja_LKWbzQ3_L9Q/view?usp=sharing">here</a></li>
    <li>Run : <b>python3 safeway_v1.py --model=road_type_ss.onnx --input_URI path_to_input_video --output_URI output.mp4 </b></li>
</ol>
Note : Other parameters have been passed in the script itself.    

## :hammer_and_wrench: End to End steps followed:

<ol>
    <li>The dataset used is the RTK Dataset and it can be downloaded from <a href="https://lapix.ufsc.br/pesquisas/projeto-veiculo-autonomo/datasets/?lang=en">here</a> </li>
    <li>Next clone this <a href="https://github.com/Resham-Sundar/SafeWay">repo</a>, create a environment and install the requirements</li>
    <li>Further install these - torch, torchvision, pycocotools and onnx</li>
    <li>Next, we go inside training folder and split the dataset into traning and validation images and masks by running <b>python split_custom.py --masks="path/to/your/SegmentationClass" --images="path/to/your/JPEGImages" --output="path/to/your/output/dir"</b>.</li>
    <li>We then create the files named classes.txt and colors.txt. The classes.txt contains names of the classes and the colors.txt contains the R,G,B values of the corresponding classes.</li>
    <li>Run this to train : <b>python train.py /path/to/your/split/data --dataset=custom</b></li>
    <li>After training is finished, we get a file named model_best.pth. We know that the jetson-inference library runs TensorRT and we'll use it further. Convert the model to Onnx before taking it to the Nano</li>
    <li>Run : <b>python onnx_export.py</b></li>
    <li>Move fcn_resnet18.onnx ,classes.txt and colors.txt to the Jetson device.</li>
    <li>In the Jetson, clone the <a href="https://github.com/dusty-nv/jetson-inference">jetson-inference repository</a> and move above three files to to jetson-inference/python/examples.</li> 
</ol>

## :dizzy: References
<ul>
    <li>Dataset : <a href="https://lapix.ufsc.br/pesquisas/projeto-veiculo-autonomo/datasets/?lang=en">RTK Dataset</a></li>
    <li>Jetson Inference : [Segnet](https://github.com/dusty-nv/jetson-inference/tree/master/examples/segnet)</li>
    <li>PyTorch Segmentation : [Training code](https://github.com/Onixaz/pytorch-segmentation)</li>
</ul>

## :fireworks: Extras

This work can be extended by adding more classes to detect. Further on, we use multiple camera inputs and run the same using DeepStream to enhance our inference!
