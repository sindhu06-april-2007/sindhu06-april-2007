from abc import ABC,abstractmethod
class washing:
    def start(self):
        pass
    def stop(self):
        pass
class samsung(washing):
    def start(self):
        print("samsung is starting")
    def stop(self):
        print("samsung is stoping")
a=samsung()
a.start()
a.stop()




from abc import ABC,abstractmethod
class washing(ABC):
    def start(self):
        pass
    def stop(self):
        pass
class samsung(washing):
    def start(self):
        print("samsung is starting")
    def stop(self):
        print("samsung is stoping")
a=samsung()
a.start()
a.stop()

#========================================================================================================================================================================

from abc import ABC,abstractmethod
class washing(ABC):
    def start(self):
        pass
    def stop(self):
        pass
class samsung(washing):
    def starts(self):
        print("samsung is starting")
    def stop(self):
        print("samsung is stoping")
a=samsung()
a.start()
a.stop()


from abc import ABC,abstractmethod
class washing(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
class samsung(washing):
    def starts(self):
        print("samsung is starting")
    def stop(self):
        print("samsung is stoping")
a=samsung()
a.starts()
a.stop()

#============================================================================================================================================================

from abc import ABC,abstractmethod
class washing(ABC):
    def start(self):
        pass
    def stop(self):
        pass
class samsung(washing):
    def start(self):
        print("samsung is starting")
a=samsung()
a.start()


from abc import ABC,abstractmethod
class washing(ABC):
    @abstractmethod
    def start(self):
        pass
     @abstractmethod
    def stop(self):
        pass
class samsung(washing):
    def starts(self):
        print("samsung is starting")
a=samsung()
a.starts()


#=================================================================================================================================================================

#correct
from abc import ABC,abstractmethod
class washingmachine(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def raising(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class samsung(washingmachine):
    def start(self):
        print("samsung is starting")
    def raising(self):
        print("samsung is raising")
    def stop(self):
        print("samsung is stoping")
s=samsung()
s.start()
s.raising()
s.stop()

#====================================================================================================================================================================








