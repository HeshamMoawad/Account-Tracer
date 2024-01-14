import unittest
import typing
import datetime
import json , time


class ChatDetails(object):
    def __init__(self, account, data: dict) -> None:
        self.account = account
        self.conversation_id = data.get("conversation_id")
        self.chat_datetime = datetime.datetime.fromtimestamp(float(float(data.get("sort_timestamp"))/1000))
        self.status = data.get("status")

    @property
    def data(self):
        return self.__dict__.copy()


class ChatsParser(object):
    INIT = "inbox_initial_state"
    TRUSTED = "inbox_timeline"

    def __init__(self, response: dict, account: typing.Any = None, parse_date: datetime.datetime = datetime.datetime.now()) -> None:
        self.conversations = []
        self.next_entry_id = None
        self.response = response
        self.account = account
        try:
            self.type = list(response.keys())[0]
        except IndexError:
            self.type = None
        if self.type:
            conversations_as_dict = self.response.get(str(self.type)).get("conversations")
            self.conversations: typing.List[ChatDetails] = list(map(
                lambda chat: ChatDetails(
                account="dd",
                data = conversations_as_dict[chat]
                ), 
                conversations_as_dict.keys()
                ))
            if parse_date:
                self.conversations = list(filter(lambda x: x.chat_datetime.date() == parse_date.date(), self.conversations))
        if self.conversations:
            self.next_entry_id = self.get_next_entry_id()

    def get_next_entry_id(self) -> typing.Optional[str]:
        try:
            if self.type == self.INIT:
                return str(self.response.get(str(self.type)).get("inbox_timelines").get("trusted").get("min_entry_id"))
            else:
                return str(self.response.get(str(self.type)).get("min_entry_id"))
        except KeyError:

            return None


class TestCase(unittest.TestCase):

    def test_next_entry_id(self):
        with open("examples.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            file.close()

        chat = ChatsParser(
            data[0],
            account="" , 
            parse_date=None
        )
        self.assertEqual(len(chat.conversations), 11)
        chat = ChatsParser(
            data[1],
            account="" , 
            parse_date=None
        )

        self.assertEqual(len(chat.conversations), 11)
        chat = ChatsParser(
            data[2],
            account="" ,
            parse_date=None
        )
        
        self.assertEqual(len(chat.conversations), 20)
        ######


unittest.main()
