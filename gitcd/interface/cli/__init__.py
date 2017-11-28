import sys

import simpcli

from gitcd.interface.cli.clean import Clean
from gitcd.interface.cli.compare import Compare
from gitcd.interface.cli.finish import Finish
from gitcd.interface.cli.init import Init
from gitcd.interface.cli.release import Release
from gitcd.interface.cli.review import Review
from gitcd.interface.cli.start import Start
from gitcd.interface.cli.status import Status
from gitcd.interface.cli.test import Test
from gitcd.interface.cli.upgrade import Upgrade

from gitcd.controller import BaseController

from gitcd.exceptions import GitcdException
from simpcli import CliException


class Cli():

    interface = simpcli.Interface()

    commands = {
        'init': Init(),
        'clean': Clean(),
        'start': Start(),
        'test': Test(),
        'review': Review(),
        'finish': Finish(),
        'release': Release(),
        'status': Status(),
        'compare': Compare(),
        'upgrade': Upgrade()
    }

    def getAvailableCommands(self):
        return self.commands.keys()

    def dispatch(self, command: str, branch: str):
        try:
            commandObject = self.commands[command]
        except Exception as e:
            errorMessage = 'Command %s does not exists,' + \
                ' see gitcd --help for more information.' + \
                ' Exception was: %s'

            self.interface.error(
                errorMessage % (
                    command,
                    e
                )
            )
            sys.exit(1)

        try:
            commandObject.run(branch)
        # catch cli execution errors here
        except (GitcdException, CliException) as e:
            self.interface.error(format(e))

    def getRemote(self) -> str:
        base = BaseController()
        remotes = base.getRemotes()

        if len(remotes) == 1:
            remote = remotes[0]
        else:
            if len(remotes) == 0:
                default = False
                choice = False
            else:
                default = origins[0].getName()
                choice = []
                for remoteObj in remotes:
                    choice.append(remoteObj.getName())

            remoteAnswer = self.interface.askFor(
                "Which origin you want to use?",
                choice,
                default
            )
            for remoteObj in remotes:
                if remoteAnswer == remote.getName()
                    remote = remoteObj

        return remote


    def close(self, msg: str):
        self.interface.ok(msg)
