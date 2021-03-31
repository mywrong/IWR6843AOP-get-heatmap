# IWR6843AOP-get-heatmap
Use IWR6843AOP to collect radar data after one FFT and process it into horizontal or vertical heat map

Please make sure that your radar can run TI's official Out of Box Demo(https://dev.ti.com/tirex/explore/node?node=AIHy77joqu3jXFmjqwkBKQ__VLyFKFf__LATEST).

The parameters of the radar are set as follows：

![image](https://user-images.githubusercontent.com/53046813/113153854-10254a00-926a-11eb-89c8-792e116b8e01.png)



the horizontal heat map like this:

![Figure_1](https://user-images.githubusercontent.com/53046813/113151259-7bb9e800-9267-11eb-86f1-e206d09d5333.png)


You may need to modify this line of code in the radar.py file, because the com port connected to each person's radar may be different：

![image](https://user-images.githubusercontent.com/53046813/113151957-32b66380-9268-11eb-9eba-5d14122c72c3.png)

![image](https://user-images.githubusercontent.com/53046813/113152171-6ee9c400-9268-11eb-9bef-9a6571168849.png)

