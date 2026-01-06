import Place, Transition

class Arc:
    def __init__(self, source, destination):
        if(isInstance(source, Place) and isInstance(destination, Place)):
            raise Exception(f"-=[ Cannot connect Place [ {source.name} ] to Place [ {destination.name} ] ! ]=-")
        if(isInstance(source, Transition) and isInstance(destination, Transition)):
            raise Exception(f"-=[ Cannot connect Transition [ {source.name} ] to Transition [ {destination.name} ] ! ]=-")

        self.source = source
        self.destination = destination
