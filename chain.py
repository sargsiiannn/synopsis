# Passes support requests through multiple handlers
# Each level tries to handle it or passes it on

class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, issue):
        handled = self._handle(issue)
        if not handled and self.next:
            self.next.handle(issue)

    def _handle(self, issue): raise NotImplementedError()

class LevelOneSupport(Handler):
    def _handle(self, issue):
        if issue == "password":
            print("Resetting password...")
            return True
        return False

class LevelTwoSupport(Handler):
    def _handle(self, issue):
        if issue == "server":
            print("Restarting server...")
            return True
        return False

support = LevelOneSupport(LevelTwoSupport())

# Usage
support.handle("server")  
support.handle("password") 
