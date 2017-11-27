'''

'''
import uuid

from self.topics.topic_client import TopicClient
from self.agents.face_emotion_agent import FaceEmotionAgent
from self.agents.example_agent import ExampleAgent
from self.agents.agent_society import AgentSociety
from self.gestures.gesture_manager import GestureManager
from self.gestures.speech_gesture import SpeechGesture
from self.blackboard.thing import ThingEventType
from self.blackboard.thing import Thing
from self.blackboard.thing import ThingCategory
from self.blackboard.blackboard import Blackboard

class FaceEmotionClient(object):
    def run_thread(headers):
        print("run_thread")

    def on_connected(self):
        print("On Connected function!")
        agent_id = str(uuid.uuid4())
        print("on_connect(), agent id: " + agent_id)
        agent = FaceEmotionAgent('FaceEmotionAgent', agent_id)
        AgentSociety.get_instance().subscribe()
        AgentSociety.get_instance().add_agent(agent, False)

    def run(self):
        try:
            self_id = str(uuid.uuid4())
            print("self id: " + self_id)
            headers = [('selfId', self_id), ('token', '')]
            topic = TopicClient.start_instance('127.0.0.1', 9443, headers)
            TopicClient.get_instance().setHeaders(self_id, "")
            TopicClient.get_instance().set_callback(self.on_connected)
            topic.start()
        except KeyboardInterrupt:
            exit()
        except ConnectionRefusedError:
            print("connection error: ")


if __name__ == "__main__":
    print("hey")
    FaceEmotionClient().run()
    