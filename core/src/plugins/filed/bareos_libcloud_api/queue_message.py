class MESSAGE_TYPE(object):
    InfoMessage = 1
    ErrorMessage = 2
    AbortMessage = 3
    ReadyMessage = 4
    DebugMessage = 5

    def __setattr__(self, *_):
        raise Exception("class MESSAGE_TYPE is read only")


class QueueMessageBase(object):
    def __init__(self, worker_id, message):
        self.worker_id = worker_id
        self.message_string = message
        self.type = None


class ErrorMessage(QueueMessageBase):
    def __init__(self, worker_id, message):
        QueueMessageBase.__init__(self, worker_id, message)
        self.type = MESSAGE_TYPE.ErrorMessage


class InfoMessage(QueueMessageBase):
    def __init__(self, worker_id, message):
        QueueMessageBase.__init__(self, worker_id, message)
        self.type = MESSAGE_TYPE.InfoMessage


class DebugMessage(QueueMessageBase):
    def __init__(self, worker_id, level, message):
        QueueMessageBase.__init__(self, worker_id, message)
        self.type = MESSAGE_TYPE.DebugMessage
        self.level = level


class ReadyMessage(QueueMessageBase):
    def __init__(self, worker_id, message=None):
        QueueMessageBase.__init__(self, worker_id, message)
        self.type = MESSAGE_TYPE.ReadyMessage


class AbortMessage(QueueMessageBase):
    def __init__(self, worker_id):
        QueueMessageBase.__init__(self, worker_id, None)
        self.type = MESSAGE_TYPE.AbortMessage