#!/usr/bin/env python        
## Every Python ROS Node will have this declaration at the top. The first line makes sure your script is executed as a Python script. 

import rospy                            # You need to import rospy if you are writing a ROS Node. 
from std_msgs.msg import String         # The std_msgs.msg import is so that we can reuse the std_msgs/String message type for publishing. 

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)     # Declares that your node is publishing to the chatter topic using the message type String. String here is actually the class std_msgs.msg.String. The queue_size argument is New in ROS hydro and limits the amount of queued messages if any subscriber is not receiving them fast enough. 
    rospy.init_node('talker', anonymous=True)                   # Tells rospy the name of your node -- until rospy has this information, it cannot start communicating with the ROS Master. anonymous = True ensures that your node has a unique name by adding random numbers to the end of NAME.
    rate = rospy.Rate(10) # 10hz                                # Creates a Rate object rate. With the help of its method sleep(), it offers a convenient way for looping at the desired rate. With its argument of 10, we should expect to go through the loop 10 times per second (as long as our processing time does not exceed 1/10th of a second!) 
    while not rospy.is_shutdown():                              # Check is_shutdown() to check if your program should exit (e.g. if there is a Ctrl-C or otherwise).
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)                                # The messages get printed to screen, it gets written to the Node's log file, and it gets written to rosout.
        pub.publish(hello_str)
        rate.sleep()                                            # The loop calls rate.sleep(), which sleeps just long enough to maintain the desired rate through the loop. 

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
