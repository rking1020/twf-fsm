#!/usr/bin/env python

import rospy 
from std_msgs.msg import String

def talker():
    pub=rospy.Publisher('topic', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate=rospy.Rate(10) #10 hz
    #a = ['objectFound', 'objectRight', 'routeClear']
    a = 'objectFound'
    while not rospy.is_shutdown():
        #for i in a:
        pub.publish(a)
        rate.sleep()
    '''
    while not rospy.is_shutdown():
        hello_str="hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
    '''

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
