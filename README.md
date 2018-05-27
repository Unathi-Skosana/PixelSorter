# NOTE: This is just a progress Report. Cool Stuff with opencv and Computer Vision Algos and 
# Machine Learning libraries and aglos  Will Come [NOTE THIS CODE WAS NEVER OPTIMISED. MY MAIN AIM WAS TO MAKE THE
# PIXEL SORTER WORK]

### Example Images[TODO LIST FOLLOWS BELLOW AND SOME NOTES WRITTEN TO THE FUTURE ME]
![Alt text](/sample_results/0.png)



![Alt text](/sample_results/1.png)



![Alt text](/sample_results/2.png)



![Alt text](/sample_results/3.png)




![Alt text](/sample_results/4.png)



![Alt text](/sample_results/5.png)



![Alt text](/sample_results/6.png)



![Alt text](/sample_results/7.png)


![Alt text](/sample_results/8.png)


![Alt text](/sample_results/9.png)

![Alt text](/sample_results/10.png)


![Alt text](/sample_results/11.png)


![Alt text](/sample_results/12.png)


![Alt text](/sample_results/13.png)


![Alt text](/sample_results/14.png)


![Alt text](/sample_results/15.png)




![Alt text](/sample_results/16.png)


![Alt text](/sample_results/17.png)


![Alt text](/sample_results/18.png)


![Alt text](/sample_results/19.png)


![Alt text](/sample_results/20.png)


![Alt text](/sample_results/21.png)



![Alt text](/sample_results/22.png)



![Alt text](/sample_results/23.png)


![Alt text](/sample_results/24.png)


![Alt text](/sample_results/25.png)




# NOTES/ TODOS:

## I realized that sorting the whole image is intuitively not a great idea due
## to the fact that one would not achieve great results by doing so. However,
## i will start of by sorting half the image and then take it from there.
## at this stage i would like to use the sobel method for achieving a different
## outcome.

### > the comparative_merge_sort.py implemented by unathi is broken. the primary
###   array is sorted correctly but the secondary array is not sorted accordingly.
###   a certain cell is duplicated when the sorting is in action. I failed to debug
###   it,
### > however, to proceed i am resorting to the sorted built in function. which
###   uses a hybrid sorting algorithm called Timesort, this algorithm is derived
###   from merge sort and insertion sort and it works well with different kinds of
###   data sets.

### > implement or make use of edge detection before sorting ;) cook an art tool
### > debug and reslove RUNTIMEERRORS for two sorting criteria methods.
### > fix methods and rethink the design of the code structure.
### > implement a squre and circle sorter.
### > then use SIFT or SURF for object detection and sort the objects identified.
### > also it would be cool to sort people or faces, this is possible through obj detection.
