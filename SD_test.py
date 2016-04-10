import rospy
import smach
import smach_ros
from std_msgs.msg import String

#default state
class Scanning(smach.State):
    def __init__(self):
        smach.State__init__(self, outcomes=['objectFound'])

    def execute(self, userdata):
        rospy.loginfo('executing state SCANNING')
    
#Object has been found...where do we go?
class Deciding(smach.State):
    def __init__(self):
        smach.State__init__(self, outcomes=['objectRight', 'objectLeft'])

    def execute(self, userdata):
        rospy.loginfo('executing state DECIDING')
        #implement

class TurningRight(smach.State):
    def __init__(self):
        smach.State__init__(self, outcomes=['routeClear'])

    def execute(self, userdata):
        rospy.loginfo('executing state TURNING RIGHT')
        #implement

class TurningLeft(smach.State):
    def __init__(self):
        smach.State__init__(self, outcomes=['routeClear'])

    def execute(self, userdata):
        rospy.loginfo('executing state TURNING LEFT')
        #implement
def save_matrix():
    rospy.loginfo('testing')

#function which sets up FSM node
def listener():
    #don't actually know if I want the msg to be a string
    pub = rospy.Subscriber('matrix_topic', String, save_matrix)
    rospy.init_node('matrix_node', anonymous=True)
    rate = rospy.Rate(10) #10 Hz
    rospy.spin()
        
def main():
    
    #listener()
    rospy.init_node('nav_FSM')

    #create top level SMACH state machine
    sm = smach.StateMachine(outcomes=['some_outcome'])

    #open the container !
    with sm:
        #Add states to the container
        smach.StateMachine.add('SCANNING', Scanning(),
                               transitions={'objectFound':'DECIDING'})

        smach.StateMachine.add('DECIDING', Deciding(),
                               transitions={'objectRight':'TURNINGLEFT',
                                            'objectLeft':'TURNINGRIGHT'})


        smach.StateMachine.add('TURNINGRIGHT', TurningRight(),
                               transitions={'routeClear':'SCANNING'})

        smach.StateMachine.add('TURNINGLEFT', TurningRight(),
                               transitions={'routeClear':'SCANNING'})

        outcome = sm.execute()

if __name__ == '__main__':
    main()
