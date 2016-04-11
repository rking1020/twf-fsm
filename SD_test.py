import rospy
import smach
import smach_ros
from std_msgs.msg import String

def test_listen():
    a = "objectFound"
    rospy.loginfo("dir: " + a)
    return a

#functions to set up subscriber node
def callback(data):
    rospy.loginfo("direction: " + data.data)
    

def listener():
    rospy.init_node('listner', anonymous=True)
    rospy.Subscriber('topic', String, callback)
    rospy.loginfor(String)
    #rospy.spin()
    #return String#rospy.loginfo('state: ' + data.data)
   # rospy.spin()

#default state
class Scanning(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['objectFound'])

    def execute(self, userdata):
        rospy.loginfo('executing state SCANNING')
        #return 'objectFound'
        #return test_listen()
        return listener()
#Object has been found...where do we go?
class Deciding(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['objectRight', 'objectLeft', 'objectFound'])

    def execute(self, userdata):
        rospy.loginfo('executing state DECIDING')
        #implement
        #return 'objectRight'
        return test_listen()

class TurningRight(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['routeClear'])

    def execute(self, userdata):
        rospy.loginfo('executing state TURNING RIGHT')
        #implement
        
        return 'routeClear'

class TurningLeft(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['routeClear'])

    def execute(self, userdata):
        rospy.loginfo('executing state TURNING LEFT')
        #implement
        #return data.data
        return 'routeClear'
        
def main():

    rospy.init_node('smach__state_machine')
    #create top level SMACH state machine
    sm = smach.StateMachine(outcomes=['some_outcome'])
    #open the container !
   
    with sm:
    #    listener()
        
        #Add states to the container
        smach.StateMachine.add('SCANNING', Scanning(),
                               transitions={'objectFound':'DECIDING'})
    


        smach.StateMachine.add('DECIDING', Deciding(),
                               transitions={'objectRight':'TURNINGLEFT',
                                            'objectLeft':'TURNINGRIGHT', 
                                            'objectFound':'SCANNING'}) 
    

        smach.StateMachine.add('TURNINGRIGHT', TurningRight(),
                               transitions={'routeClear':'SCANNING'})

        smach.StateMachine.add('TURNINGLEFT', TurningRight(),
                               transitions={'routeClear':'SCANNING'})

    outcome = sm.execute()

if __name__ == '__main__':
    main()
