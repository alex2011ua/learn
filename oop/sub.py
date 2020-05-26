from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()  # При инициализации множество подписчиков задается пустым

    def subscribe(self, subscriber):
        self.__subscribers.add(
            subscriber)  # Для того чтобы подписать пользователя, он добавляется во множество подписчиков

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)  # Удаление подписчика из списка

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)  # Отправка уведомления всем подписчикам


class AbstractObserver(ABC):

    @abstractmethod
    def update(self, dic):
        pass



class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, dic):
        self.achievements.add(dic['title'])



class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, dic):
        if dic not in self.achievements:
            self.achievements.append(dic)

