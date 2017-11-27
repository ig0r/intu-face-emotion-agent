'''
Copyright 2016 IBM All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from self.agents.agent import Agent
from self.blackboard.blackboard import Blackboard
from self.blackboard.thing import ThingEventType
from self.blackboard.thing import Thing
from self.blackboard.thing import ThingCategory

class FaceEmotionAgent(Agent):
    ''' An example agent implementation that can subscribe to Text objects on
    the blackboard '''
    def __init__(self, agent_name, agent_id):
        super(self.__class__, self).__init__(agent_name, agent_id)

    def on_text(self, payload):
        ''' Handle a received Text object '''
        for key, value in payload['thing'].items():
            print (key,value)
        print("FaceEmotionAgent OnText(): " + payload['thing']['m_Data']['m_Text'])

    def on_start(self):
        ''' Start the agent and subscribe to the Text objects '''
        print("FaceEmotionAgent has started!")
        Blackboard.get_instance().subscribe_to_type("FaceEmotion", ThingEventType.ADDED, "", self.on_text)
        print("subscribed to the events")
        emotion = Thing()
        emotion.category = ThingCategory.PERCEPTION
        emotion.set_type("IThing")
        data = {}
        data['m_Text'] = "sending a test message to itself"
        emotion.data = data
        emotion.data_type = "FaceEmotion"
        print("thing: ", emotion.data)
        Blackboard.get_instance().add_thing(emotion, "")
        return True

    def on_stop(self):
        ''' Put stopping logic here '''
        print("FaceEmotionAgent has stopped!")
        return True
