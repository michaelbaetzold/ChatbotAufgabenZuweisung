from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionProcessSupportRequest(Action):
    def name(self) -> Text:
        return "action_process_support_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Hier könntest du die Logik implementieren, um die Supportanfrage zu verarbeiten
        dispatcher.utter_message("Ich werde mich um Ihr Problem kümmern.")
        return []

class ActionAskProblemConfirmation(Action):
    def name(self) -> Text:
        return "utter_ask_problem_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Könnten Sie bitte Ihr Problem genauer beschreiben?")
        return []
