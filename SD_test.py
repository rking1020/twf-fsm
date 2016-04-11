import rospy
import smach
import smach_ros
from std_msgs.msg import String


def callback(data):
    #rospy.loginfo("direction: " + data.data)
    pass

def listener():
    rospy.init_node('listner', anonymous=True)
    rospy.Subscriber('topic', String, callback)

    rospy.spin()

#default state
class Scanning(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['objectFound'])

    def execute(self, userdata):
        rospy.loginfo('executing state SCANNING')
    
#Object has been found...where do we go?
class Deciding(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['objectRight', 'objectLeft'])

    def execute(self, userdata):
        rospy.loginfo('executing state DECIDING')
        #implement

class TurningRight(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['routeClear'])

    def execute(self, userdata):
        rospy.loginfo('executing state TURNING RIGHT')
        #implement

class TurningLeft(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['routeClear'])

    def execute(self, userdata):
        rospy.loginfo('executing state TURNING LEFT')
        #implement


        
def main():

    listener()

    #create top level SMACH state machine
    sm = smach.StateMachine(outcomes=['some_outcome'])
    #open the container !
    with sm:
        #Add states to the container
        smach.StateMachine.add('SCANNING', Scanning(),
                               transitions={'objectFound':'SCANNING'})
    outcome = sm.execute()
"""

        smach.StateMachine.add('DECIDING', Deciding(),
                               transitions={'objectRight':'TURNINGLEFT',
                                            'objectLeft':'TURNINGRIGHT'})


        smach.StateMachine.add('TURNINGRIGHT', TurningRight(),
                               transitions={'routeClear':'SCANNING'})

        smach.StateMachine.add('TURNINGLEFT', TurningRight(),
                               transitions={'routeClear':'SCANNING'})

outcome = sm.execute()
"""
if __name__ == '__main__':
    main()
