#!/usr/bin/env python
import rospy
import roslib
from std_msgs.msg import String
import time

f = open('/home/turtlebot/experiments/catkin_ws/results/'+time.strftime('%Y%m%d%H%M%S') + 'data.txt','a')
strt=True
def data_callback(data):
    global strt
    d = data.data
    d = d.split(':')
    if strt:
        f.write(d[0])
        strt = False

    f.write(d[1])

if __name__=='__main__':
    node = rospy.init_node('data_collection',anonymous=True)
    sub_data = rospy.Subscriber('/data_collection',String,data_callback)
    
    try:
        while not rospy.is_shutdown():
            #do nothing
            continue
        f.close()
        print("Shutting down data collector")
    except rospy.ROSInterruptException:
        print('Something went wrong')
    pass

    