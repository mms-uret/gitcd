from simpcli import CliException

from gitcd.git.repository import Repository


class Base(object):

    repository = Repository()
    config = None
    configPersonal = None
    updateRemotes = False

    def __init__(self):
        self.config = self.repository.getConfig()
        self.configPersonal = self.repository.getPersonalConfig()
        if self.updateRemotes == True:
            print('updating remotes')
            self.remoteUpdate()

    def remoteUpdate(self) -> bool:
        remotes = self.repository.getRemotes()

        returnValue = True
        for remote in remotes:
            try:
                remote.update()
            except CliException as e:
                returnValue = False
        return returnValue